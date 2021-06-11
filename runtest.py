import sys
import os
import numpy as np
import openpyxl
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


def process_row0(firstrow):
    outcome_end_index = len(firstrow) - 1
    for i, cell in enumerate(firstrow, start=0):
        if i == 0 or cell.ctype == 0:
            continue
        if cell.ctype == 1 and cell.value.lower() == "income":
            income_start_index = i
        if cell.ctype == 1 and cell.value.lower() == "outcome":
            income_end_index = i-1
            outcome_start_index = i         
         
    print("Income_Start {}, Income_End {}, Outcome_Start {}, Outcome_End {}".format(income_start_index, income_end_index, outcome_start_index, outcome_end_index))
    return (income_start_index, income_end_index, outcome_start_index, outcome_end_index)

def process_row(row):
    res = np.array([])
    for i, cell in enumerate(row, start=0):
        if cell.ctype == 1 and i!=0:
            res = np.append(res, cell.value)
    return res

#need to process the indexes
def process_col(col):
    res = np.array([])
    for i, cell in enumerate(col, start=0):
        if cell.ctype == 1 and i>1:
            res = np.append(res, cell.value)
    return res

def test_pyprocsal():
    
    excel_sheet = openpyxl.load_workbook("local/input.xlsx")
    #starting from the first sheet
    zero_sheet = excel_sheet.sheetnames[0]

    print(zero_sheet[1])

    # headers = process_row(sheet.row(1))
    # print(headers)

    # months = process_col(sheet.col(0)) 
    # print(months)

    # nr = sheet.nrows
    
    # for cx in range(data.ncols):
    #     print(data.col(cx))
    ##x = np.array(data.Salary)
    ##print(x[0])
    ##plt.plot(x)
    ##plt.show()

    
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