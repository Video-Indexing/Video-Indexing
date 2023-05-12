import http.server
import socketserver
import urllib.parse
from functions import index_video
import json
import requests

PORT = 8080

WEB_SERVER_PORT = 5050
WEB_SERVER_IP = '127.0.0.1'
WEB_SERVER_FULL_URL = f"http://{WEB_SERVER_IP}:{WEB_SERVER_PORT}/uploadVideoAlgo"


class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data_dict = json.loads(post_data.decode('utf-8'))
        response_data = {'message': 'Received data successfully', 'data': data_dict}
        my_url = data_dict['link']
        vid_name = data_dict['name']
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.send_results_to_web_server(my_url,vid_name)

    def send_results_to_web_server(self,url,name):
        indexing = index_video(url)
        params = {"url": url, "name": name, "indexing": indexing}
        headers = {'Content-type': 'application/json'}
        response = requests.post(WEB_SERVER_FULL_URL, data=json.dumps(params), headers=headers)
        print(f"response from Web Server: \n {str(response)}")


with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()