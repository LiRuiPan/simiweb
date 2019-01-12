from routes import (
    template,
    html_response
)


def index(request):
    """
    主页的处理函数, 返回主页的响应
    """
    body = template('index.html')
    r = html_response(body)
    return r


def static(request):
    """
    静态资源的处理函数, 读取图片并生成响应返回
    """
    filename = request.query['file']
    path = 'static/{}'.format(filename)
    with open(path, 'rb') as f:
        header = b'HTTP/1.x 200 OK\r\nContent-Type: image/gif\r\n\r\n'
        img = header + f.read()
        return img


def route_dict():
    d = {
        '/': index,
        '/static': static,
    }
    return d
