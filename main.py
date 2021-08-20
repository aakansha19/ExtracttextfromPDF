import PyPDF2
pdfFileObject= open('C:/Users/hp/Desktop/name.pdf','rb')
pdfReadObject= PyPDF2.PdfFileReader(pdfFileObject)
print(pdfReadObject.numPages)
for i in range(pdfReadObject.numPages):
    firstPageObject= pdfReadObject.getPage(i)
    print(firstPageObject.extractText())


