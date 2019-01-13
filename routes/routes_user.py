from routes import (
    template,
    html_response,
    redirect,
)
from routes.helper import current_user
from urllib.parse import unquote_plus
from utils import log
from models.user import User
from models.session import Session


# 登陆请求处理
def login(request):
    form = request.form()
    u, result = User.login(form)
    log('login post', result)
    if u is None:
        headers = None
        return redirect('/user/login/view?result={}'.format(result), headers)
    else:
        s = Session.make(u.id)
        headers = {
            'Set-Cookie': 'session_id={}; path=/'.format(s.session_id)
        }
        return redirect('/', headers)


# 登陆页面的路由函数
def login_view(request):
    u = current_user(request)
    result = request.query.get('result', ' ')
    result = unquote_plus(result)

    body = template(
        'login.html',
        username=u.username,
        result=result,
    )
    return html_response(body)


# 注册请求处理
def register(request):
    form = request.form()

    u, result = User.register(form)
    log('register post', result)
    if u.is_guest():
        return redirect('/user/register/view?result={}'.format(result))
    else:
        return redirect('/user/login/view?result={}'.format(result))


# 注册页面的路由函数
def register_view(request):
    result = request.query.get('result', ' ')
    result = unquote_plus(result)

    body = template('register.html', result=result)
    return html_response(body)


# 用户相关路由表
def route_dict():
    r = {
        '/user/login': login,
        '/user/login/view': login_view,
        '/user/register': register,
        '/user/register/view': register_view,
    }
    return r
