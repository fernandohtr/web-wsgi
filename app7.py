def app(environ, start_response):
    with open('texto.html', 'rb') as f:
        body = f.read()
    status = '200 OK'
    headers = [('Content-Type', 'text/html')]
    start_response(status, headers)
    return [body]
