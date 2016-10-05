import settings
from http.server import HTTPStatus
from git_template import template
from data import DateAccess


def handle_index(request):
    DateAccess.DataAccessor().initial()
    posts = DateAccess.DataAccessor().Posts
    head = """<html>
                <head><title>AlimovTILLO</title></head>
                <body>"""

    body = """</body>
                </html>"""

    All = """<br><br><br> %s """ % posts
    request.send_response(HTTPStatus.OK)
    request.send_header('Content-Type', 'text/html')
    request.end_headers()
    request.wfile.write(str.encode(head))
    for i in posts:
        title = posts['%s' % i]['Title']
        text = posts['%s' % i]['Text']
        post = """%s %s <br>""" % (title, text)
        request.wfile.write(str.encode(post))
    request.wfile.write(str.encode(All))
    request.wfile.write(str.encode(body))
    return request


def post(request):
    DateAccess.DataAccessor().insert()
    redirect(request, '/')
    request.send_header('Content-Type', 'text/html')
    request.end_headers()
    return request


def delete(request):

    DateAccess.DataAccessor().delete()
    redirect(request, '/')
    request.send_header('Content-Type', 'text/html')
    request.end_headers()
    return request


def handle_404(request):
    request.send_response(HTTPStatus.NOT_FOUND)
    request.send_header('Content-Type', 'text/html')
    request.end_headers()
    return request


def redirect(request, path):
    request.send_response(HTTPStatus.SEE_OTHER)
    request.send_header('Location', path)
