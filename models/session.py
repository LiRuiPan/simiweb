import time
import random
from models import Model


def random_string():
    """
    生成一个随机的字符串
    """
    seed = 'sdfsdafasfsdfsdwtfgjdfghfg'
    s = ''
    for i in range(16):
        random_index = random.randint(0, len(seed) - 2)
        s += seed[random_index]
    return s


class Session(Model):
    """
    Session 是用来保存 session 的 model
    """

    def __init__(self, form):
        super().__init__(form)
        self.session_id = form['session_id']
        self.user_id = form['user_id']
        self.expired_time = form.get('expired_time', time.time() + 3600)

    # 构造session
    @classmethod
    def make(cls, user_id):
        session_id = random_string()
        form = dict(
            session_id=session_id,
            user_id=user_id,
        )
        s = cls.new(form)
        return s

    # 过期判断
    def expired(self):
        now = time.time()
        result = self.expired_time < now
        if result is True:
            self.delete(self.id)
        return result
