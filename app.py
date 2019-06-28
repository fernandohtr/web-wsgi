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
        return [body]

    if environ['PATH_INFO'] == '/favicon.ico':
        return not_found()

    elif environ['PATH_INFO'] == '/style.css':
        return page(environ, 'style.css', 'text/css')

    else:
        return page(environ, 'texto.html', 'text/html')

