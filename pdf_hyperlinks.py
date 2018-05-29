import PyPDF2 as pyPdf

PDFFile = open('test.pdf','rb')

PDF = pyPdf.PdfFileReader(PDFFile)
pages = PDF.getNumPages()
key = '/Annots'
uri = '/URI'
dest = '/Dest'

#print(PDF.getOutlines())
destinations = PDF.getNamedDestinations()
print(destinations)

for name in destinations:
    print(name)

for page in range(14, 25):

    pageSliced = PDF.getPage(page)
    pageObject = pageSliced.getObject()

    if key in pageObject:
        ann = pageObject[key]
        for a in ann:
            u = a.getObject()
            if dest in u:
               # print(u[dest])
               pass
