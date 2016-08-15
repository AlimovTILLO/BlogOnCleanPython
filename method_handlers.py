import settings
from template_engine.template import Template
from http.server import HTTPStatus
from git_template import template


def handle_index(request):
    f = open(settings.TEMPLATES_DIR + 'index.html')
    read = f.read()
    data = [(2, 'Tillo', 'Alimov', 'alimovtillo', '123', True)]
    print(data[0][1])
    html = template.Template(read).render(name=data[0][1], lastname=data[0][2])

    request.send_response(HTTPStatus.OK)
    request.send_header('Content-Type', 'text/html')
    request.end_headers()
    request.wfile.write(str.encode(html))
    return request


def handle_404(request):
    request.send_response(HTTPStatus.NOT_FOUND)
    request.send_header('Content-Type', 'text/html')
    request.end_headers()
    return request
# jkhgug