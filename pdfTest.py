import os
import sys
import re
import time
import PyPDF2 as pdf

def getPageCount(file):
    pdfFileObj = open(file, 'rb')
    pdfReader = pdf.PdfFileReader(pdfFileObj)
    return pdfReader.numPages

def extractData(file, page):
    pdfFileObj = open(file, 'rb')
    pdfReader = pdf.PdfFileReader(pdfFileObj)
    pageObj = pdfReader.getPage(page)
    return pageObj.extractText()

def getWordCount(data):
    data = data.split()
    return len(data)

def main():
    if len(sys.argv) != 2:
        print('Usage: python pdfTest.py Filename')
        exit(2)
    else:
        pdfFile = sys.argv[1]
        try:
            if os.path.exists(pdfFile):
                print('File is found.')
        except OSError as err:
            print(err.reason)
            exit(2)
        totalWords = 0
        numPages = getPageCount(pdfFile)
        for i in range(numPages):
            text = extractData(pdfFile, i)
            totalWords += getWordCount(text)
        print('There are ' + str(totalWords) + ' in total')
        print('There are ' + str(numPages) + ' pages in this document.')

if __name__ == '__main__':
    main()

