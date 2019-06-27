def app(environ, start_response):

    if environ['PATH_INFO'] == '/style.css':
        with open('style.css', 'rb') as f:
            body = f.read()
            headers = [('Content-Type', 'text/css')]
            status = '200 OK'

    elif environ['PATH_INFO'] == '/favicon.ico':
        body = b'404: Nothing here'
        headers = [('Content-Type', 'text/plain')]
        status = '404 Not Found'

    else:
        with open('texto.html', 'rb') as f:
            body = f.read()
            headers = [('Content-Type', 'text/html')]
            status = '200 OK'

    start_response(status, headers)

    return [body]
