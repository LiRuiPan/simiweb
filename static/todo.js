// TODO API
// 获取所有todo
var apiTodoAll = function(callback) {
    var path = '/api/todo/all'
    ajax('GET', path, '', callback)
}

// 添加todo
var apiTodoAdd = function(form, callback) {
    var path = '/api/todo/add'
    ajax('POST', path, form, callback)
}

// todo模板
var todoTemplate = function(todo) {
    var t = `
        <div class="todo-cell" data-id="${todo.id}">
            <span class="todo-content">${todo.content}</span>
            <span>创建时间：${todo.created_time}</span>
            <span>更新时间：${todo.updated_time}</span>
            <button class="todo-edit">编辑</button>
            <button class="todo-delete">完成</button>
        </div>
    `
    return t
}

// 插入todo
var insertTodo = function(todo) {
    var todoCell = todoTemplate(todo)
    // 插入 todo-list
    var todoList = e('#id-todo-list')
    todoList.insertAdjacentHTML('beforeend', todoCell)
}

// 加载所有todo
var loadTodos = function() {
    // 调用 ajax api 来载入数据
    apiTodoAll(function(todos) {
        log('load all todos', todos)
        // 循环添加到页面中
        for(var i = 0; i < todos.length; i++) {
            var todo = todos[i]
            insertTodo(todo)
        }
    })
}

// 监听添加事件
var bindEventTodoAdd = function() {
    var b = e('#id-button-add')
    b.addEventListener('click', function(){
        var input = e('#id-input-todo')
        var content = input.value
        if (content == '') {
            alert('内容不能为空')
        } else {
            log('click add', content)
            var form = {
                content: content,
            }
            apiTodoAdd(form, function(todo) {
                // 收到返回的数据, 插入到页面中
                insertTodo(todo)
            })
        }
    })
}

// 监听事件
var bindEvents = function() {
    bindEventTodoAdd()
}

var __main = function() {
    bindEvents()
    loadTodos()
}

__main()
