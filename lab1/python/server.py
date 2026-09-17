from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

ROUTES = {
    '/': 'index.html',
    '/about': 'about.html',
    '/styles.css': 'styles.css'
}


class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        path = self.path.split('?')[0]
        filename = ROUTES.get(path)

        # Handling non existent pages
        if filename is None:
            filename = '404.html'
            status = 404
        else:
            status = 200

        file_path = BASE_DIR / 'public' / filename
        content = file_path.read_text(encoding='utf-8')

        if filename.endswith('.css'):
            content_type = 'text/css; charset=utf-8'
        else:
            content_type = 'text/html; charset=utf-8'

        self.send_response(status)
        self.send_header('Content-type', content_type)
        self.end_headers()
        self.wfile.write(content.encode('utf-8'))





httpd = HTTPServer(('localhost', 3002), Handler)
httpd.serve_forever()
