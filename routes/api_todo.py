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


@login_required
def delete(request):
    todo_id = int(request.query['id'])
    Todo.delete(todo_id)
    d = dict(
        message="成功删除 todo"
    )
    return json_response(d)


@login_required
def update(request):
    form = request.json()
    todo_id = int(form['id'])
    content = form['content']
    t = Todo.update(todo_id, content=content)
    return json_response(t.json())


def route_dict():
    d = {
        '/api/todo/all': all,
        '/api/todo/add': add,
        '/api/todo/delete': delete,
        '/api/todo/update': update,
    }
    return d
