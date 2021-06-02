import sys
import os
import PyPDF2
import textract
import tabula
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from http.server import BaseHTTPRequestHandler, HTTPServer
import logging

class MyServer(BaseHTTPRequestHandler):
    def do_POST(self):
        self.send_response(200)
        self.end_headers()

        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_body = self.rfile.read(content_length) # <--- Gets the data itself
        #logging.info("POST request,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\nVersion:\n%s",
        #        str(self.path), str(self.headers), post_data.decode('utf-8'), self.request_version)
        logging.info("POST Body: \n%s\n", str(post_body.decode('utf-16')))
        self.wfile.write("received post request:<br>{}".format(post_body))


def test_pyprocsal():
    files = os.listdir('local/')
    first = 'John\n'
    last = 'Doe'
    street = 'Main Street'
    number = 123
    city = 'AnyCity'
    state = 'AS'
    zipcode = '09876'
    print (("{0} {1}\n{2} {3}\n{4}, {5} {6}").format(first, last, number, street, city, state, zipcode))
    
    data = pd.read_excel('local/input.xlsx', sheet_name='Test', usecols=['Salary', 'Month'])
    print(data)
    x = np.array(data.Salary)
    print(x[0])
    plt.plot(x)
    plt.show()

    
    # for f in files:
    #     print(f)
    #     # dirpdf = textract.process('local/{file}'.format(file=f))
    #     # fmtext = str(text)[1:].replace('\'', '')
    #     # print(("{0}").format(dirpdf))

    #     fullpath = 'local/{name}'.format(name=f)
    #     df = tabula.read_pdf(fullpath, output_format="json", multiple_tables=True, pages="all")
    #     print(df)

    #     # pdfObj = open('local/{file}'.format(file=f), 'rb')
    #     # pdfReader = PyPDF2.PdfFileReader(pdfObj)
    #     # print(pdfReader.isEncrypted)
    #     # pdfPage = pdfReader.getPage(0)
    #     # print(pdfPage.extractText())

def run(server_class=HTTPServer, handler_class=MyServer, port=9070):
    logging.basicConfig(level=logging.INFO)
    server_address = ('127.0.0.1', port)
    httpd = server_class(server_address, handler_class)
    logging.info('Starting httpd...\n')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info('Stopping httpd...\n')

if __name__ == "__main__":

    test_pyprocsal()

    # run()
    # print("Server stopped.")