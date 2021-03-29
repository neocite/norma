from http.server import BaseHTTPRequestHandler
from models import category
from urlparse import urlparse


class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        query = urlparse(self.path).query
        query_components = dict(qc.split("=") for qc in query.split("&"))
        text = query_components["text"]
        category.classify(text)
        self.send_response(200, text)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        return
