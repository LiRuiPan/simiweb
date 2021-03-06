from models.user import User
from models.session import Session
from functools import wraps
from utils import log
from routes import redirect


# 当前用户判断
def current_user(request):
    if 'session_id' in request.cookies:
        session_id = request.cookies['session_id']
        s = Session.find_by(session_id=session_id)
        if s is None or s.expired():
            return User.guest()
        else:
            user_id = s.user_id
            u = User.find_by(id=user_id)
            return u
    else:
        return User.guest()


# 登陆判断
def login_required(route_function):
    @wraps(route_function)
    def f(request):
        log('login_required')
        u = current_user(request)
        if u.is_guest():
            log('游客用户')
            return redirect('/user/login/view')
        else:
            log('登录用户', route_function)
            return route_function(request)
    return f