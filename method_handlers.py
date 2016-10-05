import settings
import cgi
from http.server import HTTPStatus
from git_template import template
from data import DateAccess


def handle_index(request):
    DateAccess.DataAccessor().initial()
    posts = DateAccess.DataAccessor().Posts
    users = DateAccess.DataAccessor.Users['1']
    name = users['Name']
    fname = users['Fname']
    lname = users['Lname']
    head = """<html>
                <head><title>AlimovTILLO</title></head>
                <body>
                <p>%s</p>
                <p>%s</p>
                <p>%s</p>
                <form action="/post/" method="POST">
                <p>Title<input type="text" name="title"></p>
                <p>Text <textarea name="text" id="" cols="30" rows="10"></textarea></p>
                <p><input type="submit"></p>
                </form>
                """ % (name, fname, lname)

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
    user_id = DateAccess.DataAccessor.Users['1']
    data = 'poka ego netu)))'
    post_id = DateAccess.DataAccessor.Posts['3']
    DateAccess.DataAccessor().insert(user_id=user_id, post_id=post_id, title=data['title'], text=data['text'])
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


def return_value_from_post():
    form = cgi.FieldStorage()
    print(form["name"])
