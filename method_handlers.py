import settings
from http.server import HTTPStatus
from git_template import template
from data import DateAccess


def handle_index(request):
    f = open(settings.TEMPLATES_DIR + 'index.html')
    read = f.read()
    posts = DateAccess.DataAccessor().conn['users']['user1']['posts']
    # html = template.Template(read).render(name=data[0][1], lname=data[0][2], username=data[0][3], posts=posts)
    print(posts)

    head = """<html>
                <head><title>AlimovTILLO</title></head>
                <body>"""

    body = """</body>
                </html>"""

    request.send_response(HTTPStatus.OK)
    request.send_header('Content-Type', 'text/html')
    request.end_headers()
    request.wfile.write(str.encode(head))
    for i in posts:
        title = DateAccess.DataAccessor().conn['users']['user1']['posts']['%s' % i]['Title']
        text = DateAccess.DataAccessor().conn['users']['user1']['posts']['%s' % i]['text']
        post = """%s %s <br>""" % (title, text)
        request.wfile.write(str.encode(post))
    request.wfile.write(str.encode(body))
    return request


def handle_404(request):
    request.send_response(HTTPStatus.NOT_FOUND)
    request.send_header('Content-Type', 'text/html')
    request.end_headers()
    return request


def redirect(request, path):
    request.send_response(HTTPStatus.SEE_OTHER)
    request.send_header('Location', path)
