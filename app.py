import os


def app(environ, start_response):
    url_path = environ['PATH_INFO']

    if url_path == '/' or url_path == '/static/':
        url_path = '/index.html'

    if url_path[1:] in os.listdir('static'):
        response = route(environ, url_path)
    else:
        response = not_found()

    body, headers, status = response
    start_response(status, headers)
    return [body]


def not_found():
    body = b'404: Nothing here'
    headers = [('Content-Type', 'text/plain')]
    status = '404 Not Found'
    return body, headers, status


def route(environ, url_path):
    if environ['REQUEST_METHOD'] == 'POST':
        read_bytes = environ['wsgi.input'].read()
        read_str = read_bytes.decode('utf-8')
        save_info(read_str)

    body = read_body(url_path)
    headers = [('Content-Type', mime(url_path))]
    status = '200 OK'
    return body, headers, status


def save_info(read_str):
    with open('content/register.txt', 'a+') as f:
        f.write(read_str + '\n')


def read_body(url_path):
    local_path = 'static' + url_path
    with open(local_path, 'rb') as f:
        return f.read()


def mime(url_path):
    types = {
        'bmp': 'image',
        'gif': 'image',
        'jpeg': 'image',
        'png': 'image',
        'tiff': 'image',
        'css': 'text',
        'csv': 'text',
        'html': 'text',
        'calendar': 'text',
        'javascript': 'text',
        'plain': 'text',
        'json': 'application',
        'pdf': 'application',
        'xhtml+xml': 'application'
        }

    extension = url_path.split('.')[-1]
    return types[extension] + '/' + extension
