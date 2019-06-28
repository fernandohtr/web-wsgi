def app(environ, start_response):

    def page(environ, file, c_type):
        with open(file, 'rb') as f:
            body = f.read()
            headers = [('Content-Type', c_type)]
            status = '200 OK'
        start_response(status, headers)
        return [body]

    def not_found():
        body = b'404: Nothing here'
        headers = [('Content-Type', 'text/plain')]
        status = '404 Not Found'
        start_response(status, headers)
        return [body]

    path = environ['PATH_INFO']

    if path == '/texto.html' \
            or path == '/' \
            or path == '/static/texto.html' \
            or path == '/static/':
        return page(environ, 'static/texto.html', 'text/html')

    elif path == '/style.css' \
            or '/static/style.css':
        return page(environ, 'static/style.css', 'text/css')

    else:
        return not_found()
