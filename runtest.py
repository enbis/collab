import yaml
import numpy as np
from matplotlib import pyplot as plt
from http.server import BaseHTTPRequestHandler, HTTPServer
import logging
import urllib.parse

#read config as cfg
with open("configs/config.yml", "r") as ymlfile:
    cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)

class Serve(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Received')

    def do_POST(self):
        self.send_response(200)
        self.end_headers()

        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_body = self.rfile.read(content_length) # <--- Gets the data itself
        #logging.info("POST request,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\nVersion:\n%s",
        #        str(self.path), str(self.headers), post_data.decode('utf-8'), self.request_version)
        logging.info("POST Body: \n%s\n", str(post_body.decode('utf-16')))
        self.wfile.write("received post request:<br>{}".format(post_body))

def run(server_class=HTTPServer, handler_class=Serve, port=9070):
    server_address = (cfg["webserver"]["host"], cfg["webserver"]["port"])
    httpd = server_class(server_address, handler_class)
    logging.info('Starting httpd...\n')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info('Stopping httpd...\n')

if __name__ == "__main__":
    logger = logging.basicConfig(level=logging.INFO)
    logging.info('Launching webserver...')
    run()