from routes import (
    template,
    html_response,
)
from routes.helper import (
    login_required,
    current_user,
)


@login_required
def index(request):
    u = current_user(request)
    body = template('todo_index.html', username=u.username)
    return html_response(body)


def route_dict():
    d = {
        '/todo/index': index
    }
    return d
