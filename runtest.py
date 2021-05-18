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

        # ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
        # if ctype == 'multipart/form-data':
        #     postvars = cgi.parse_multipart(self.rfile, pdict)
        # elif ctype == 'application/x-www-form-urlencoded':
        #     length = int(self.headers.getheader('content-length'))
        #     postvars = cgi.parse_qs(self.rfile.read(length), keep_blank_values=1)
        # else:
        #     postvars = {}

        self.send_response(200)
        self.end_headers()

        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        logging.info("POST request,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\nVersion:\n%s",
                str(self.path), str(self.headers), post_data.decode('utf-8'), self.request_version)

        #self.wfile.write("POST request for {}".format(self.path).encode('utf-8'))

        self.wfile.write(b'Hello world')
        #test_pyprocsal()


def test_pyprocsal():
    files = os.listdir('local/')
    first = 'John\n'
    last = 'Doe'
    street = 'Main Street'
    number = 123
    city = 'AnyCity'
    state = 'AS'
    zipcode = '09876'
    testtext = 'SALARY SLIP\n\nTADAWEB S.A.\n\nAPRIL 2021\n\n1, AVENUE DU SWING\n\nINDEX : 834,76\n\nL-4367 BELVAUX\n\nWD : 22 - CD : 30 - TD : 25\nRegistration number\nSocial Security number\nTax card n\xc3\x82\xc2\xb0\nD00000956961\n\n: 1021-1064\n: 19861213 028 83\n: I 00\n\nMr. BISON ENRICO\n90, RUE CHARLES DARWIN\n\n: 04/05/2020\n: 04/05/2020\n:\n\nEntry date\nSeniority date\nExit date\nSOFTWARE DEVELOPER\nMonthly\nHourly Rate\n\nL-1433 LUXEMBOURG\n\n: 4 583,33\n: 26,4932\n\nCode\n\nWording\n\nNbr. Hours\n\nRate\n\nAmount\n\n173,00\n\nMonthly gross\n\n4 583,33\n\nTotal gross\n\nContributions for illness in kind 2,8000%\n\n4 583,33\n\n128,33\n\nContributions for illness cash 0,2500%\n\n4 583,33\n\n11,46\n\nPension contributions 8,0000%\n\n4 583,33\n\n366,67\n\nDependance Insurance 1,4000%\n\n4 032,85\n\n56,46\n\n4 583,33\n\n-562,92\n\nTotal Social Security\nTax card ded.\n\n99,00\n\nTravel allowance\n\n3 977,87\n\nTaxable amount\nTaxes\nTax credit\n\n-696,50\n36,25\nNet\n\n540\n\n-50,40\n\nDED. LUNCH VOUCHERS\nNet to be paid\n\nING LUXEMBOURG, Account Nr. LU64 0141 3716 1690 0000\n\n:\n:\n:\n\n18 333,32\n18 333,32\n559,16\n\nBase Pension\n\n:\n\n18 333,32\n\nPension Contrib.\nBase DI\n\n:\n:\n\n1 466,68\n16 131,40\n\nDI\n\n:\n\n225,84\n\nSpecial Contrib.\n\n:\n\n0,00\n\nDED. TA\nDED. OA\nDED. SE\nDED. EC\nDED. SA\nDED. SH\nDED. SH\nDED. N.S.PH\nDED. AE\nFFO\nFDS\n\n:\n:\n:\n:\n:\n:\n:\n:\n:\n:\n:\n\n396,00\n0,00\n0,00\n0,00\n0,00\n0,00\n0,00\n0,00\n0,00\n0,00\n0,00\n\n3 309,76\n3 309,76\n\nAnnual amount up to 30/04/2021 Included\nGross\nBase Illness\nIllness Contrib.\n\n3 360,16\n\n15 911,48\n2 786,00\n145,01\n0,00\n0,00\n13 440,65\n\nTaxable\nTaxes\nCIS\nCIM\nCISSM\nNet\n\n:\n:\n:\n:\n:\n:\n\nOther +\n\n:\n\n0,00\n\nOther -\n\n:\n\n-232,60\n\nTo pay\n\n:\n\n13 208,05\n\n\x0c'
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

    run()
    print("Server stopped.")