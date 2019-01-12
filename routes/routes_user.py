from urllib.parse import unquote_plus
from routes import (
    template,
    html_response,
    redirect
)

from utils import log
from models.user import User


def register(request):
    """
    注册页面的路由函数
    """
    form = request.form()

    u, result = User.register(form)
    log('register post', result)

    return redirect('/user/register/view?result={}'.format(result))


def register_view(request):
    result = request.query.get('result', ' ')
    result = unquote_plus(result)

    body = template('register.html')
    body = body.replace('{{ result }}', result)
    return html_response(body)


def route_dict():
    r = {
        '/user/register': register,
        '/user/register/view': register_view,
    }
    return r
