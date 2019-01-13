import hashlib
from models import Model
from models.user_role import UserRole


class User(Model):
    """
    User 是一个保存用户数据的 model
    """

    def __init__(self, form):
        super().__init__(form)
        self.username = form.get('username', '')
        self.password = form.get('password', '')
        self.role = form.get('role', UserRole.normal)

    @staticmethod
    def guest():
        form = dict(
            role=UserRole.guest,
            username='【游客】',
            id=-1,
        )
        u = User(form)
        return u

    def is_guest(self):
        return self.role == UserRole.guest

    def is_admin(self):
        return self.role == UserRole.admin

    @staticmethod
    def salted_password(password, salt='$!@><?>HUI&DWQa`'):
        """$!@><?>HUI&DWQa`"""
        salted = password + salt
        hashed = hashlib.sha256(salted.encode()).hexdigest()
        return hashed

    @classmethod
    def register(cls, form):
        valid = len(form['username']) > 4 and len(form['password']) > 4
        if valid:
            form['password'] = cls.salted_password(form['password'])
            u = User.new(form)
            result = '注册成功，请登录'
            return u, result
        else:
            result = '用户名或者密码长度必须大于5'
            return User.guest(), result

    @classmethod
    def login(cls, form):
        salted = cls.salted_password(form['password'])
        u = User.find_by(username=form['username'], password=salted)
        if u is not None:
            result = '登录成功'
        else:
            result = '用户名或者密码错误'
        return u, result
