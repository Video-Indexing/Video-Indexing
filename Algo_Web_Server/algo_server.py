import http.server
import socketserver
import urllib.parse
from functions import *
import json

PORT = 8080


class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_url = urllib.parse.urlparse(self.path)
        
        if parsed_url.path == '/index_video':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            query_params = urllib.parse.parse_qs(parsed_url.query)
            my_url = query_params.get('link', [''])[0]
            index_results = index_video(my_url)
            # result = f'<html><body><h1>{str(my_url)}</h1></body></html>'
            # result = f'<html><body><h1>{json.dump(index_results)}</h1></body></html>'
            # self.wfile.write(result.encode())
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(index_results).encode('utf-8'))
        elif self.path == '/goodbye':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'<html><body><h1>Goodbye, world!</h1></body></html>')
        else:
            self.send_error(404)

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data_dict = json.loads(post_data.decode('utf-8'))
        response_data = {'message': 'Received data successfully', 'data': data_dict}
        my_url = data_dict['link']
        index_results = index_video(my_url)
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(index_results).encode('utf-8'))


with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
