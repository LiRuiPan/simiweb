import json


# 响应错误请求
def error(request, code=404):
    """
    根据 code 返回不同的错误响应
    目前只有 404
    """
    e = {
        404: b'HTTP/1.x 404 NOT FOUND\r\n\r\n<h1>NOT FOUND</h1>',
    }
    return e.get(code, b'')


# 读取模板
def template(name, **kw):
    """
    根据名字读取 templates 文件夹里的一个文件并返回
    """
    path = 'templates/' + name
    with open(path, 'r', encoding='utf-8') as f:
        r = f.read()
        for k, v in kw.items():
            f = '{{ %s }}' % k
            r = r.replace(f, v)
        return r


# 格式化响应头
def formatted_header(headers, code=200):
    header = 'HTTP/1.1 {} OK \r\n'.format(code)
    header += ''.join([
        '{}: {}\r\n'.format(k, v) for k, v in headers.items()
    ])
    return header


# 构造html响应
def html_response(body, headers=None):
    h = {
        'Content-Type': 'text/html',
    }
    if headers is None:
        headers = h
    else:
        headers.update(h)
    header = formatted_header(headers)
    r = header + '\r\n' + body
    return r.encode()


# 构造json响应
def json_response(data, headers=None):
    """
    本函数返回 json 格式的 body 数据
    前端的 ajax 函数就可以用 JSON.parse 解析出格式化的数据
    """
    h = {
        'Content-Type': 'application/json',
    }
    if headers is None:
        headers = h
    else:
        headers.update(h)
    header = formatted_header(headers)
    body = json.dumps(data, ensure_ascii=False, indent=2)
    r = header + '\r\n' + body
    return r.encode()


# 重定向
def redirect(url, headers=None):
    h = {
        'Location': url,
    }
    if headers is None:
        headers = h
    else:
        headers.update(h)
    header = formatted_header(headers, 302)
    r = header + '\r\n'
    return r.encode()