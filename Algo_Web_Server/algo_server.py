import http.server
import socketserver
import urllib.parse
from functions import index_video
import json

PORT = 8080


class MyHandler(http.server.BaseHTTPRequestHandler):
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
