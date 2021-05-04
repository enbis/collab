import sys
import os
import PyPDF2
import textract

def test_pyprocsal():
    print(sys.argv)
    files = os.listdir('local/')
    print(files)
    for f in files:
        import textract
        text = textract.process('local/{file}'.format(file=f))
        print(text)

        # pdfObj = open('local/{file}'.format(file=f), 'rb')
        # pdfReader = PyPDF2.PdfFileReader(pdfObj)
        # print(pdfReader.isEncrypted)
        # pdfPage = pdfReader.getPage(0)
        # print(pdfPage.extractText())

if __name__ == "__main__":
    test_pyprocsal()
