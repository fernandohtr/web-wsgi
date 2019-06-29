def app(environ, start_response):

    path = environ['PATH_INFO']
    files = os.listdir('static')

    if path == '/':
        path = '/static/texto.html'
        route(environ, start_response, )
    elif path[1:] in files:
        pass
    else:


        rote(environ, path)
            or path == '/' \
            or path == '/static/texto.html' \
            or path == '/static/':
        return page(environ, start_response, 'static/texto.html', 'text/html')

    if path == '/texto.html' \
            or path == '/' \
            or path == '/static/texto.html' \
            or path == '/static/':
        return page(environ, start_response, 'static/texto.html', 'text/html')

    elif path == '/style.css' \
            or '/static/style.css':
        return page(environ, start_response, 'static/style.css', 'text/css')

    else:
        return not_found(start_response)


def page(environ, start_response, file, c_type):
    with open(file, 'rb') as f:
        body = f.read()
        headers = [('Content-Type', c_type)]
        status = '200 OK'
    start_response(status, headers)
    return [body]


def not_found(start_response):
    body = b'404: Nothing here'
    headers = [('Content-Type', 'text/plain')]
    status = '404 Not Found'
    start_response(status, headers)
    return [body]


def route(environ):
    pass
