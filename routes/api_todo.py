from routes import (
    json_response,
)
from routes.helper import (
    current_user,
    login_required,
)
from models.todo import Todo


@login_required
def all(request):
    u = current_user(request)
    todos = Todo.find_all(user_id=u.id)
    todos = [t.json() for t in todos]
    return json_response(todos)


@login_required
def add(request):
    # 得到浏览器发送的表单, 浏览器用 ajax 发送 json 格式的数据过来
    # 所以这里用json 函数来获取格式化后的 json 数据
    form = request.json()
    u = current_user(request)
    t = Todo.add(form, u.id)
    return json_response(t.json())


def route_dict():
    d = {
        '/api/todo/all': all,
        '/api/todo/add': add,
    }
    return d
