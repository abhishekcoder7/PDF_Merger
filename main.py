import PyPDF2

pdf_set = ["sample1.pdf", "sample2.pdf", "sample3.pdf", "sample4.pdf"]

merger =PyPDF2.PdfMerger()
for i in pdf_set:
    pdfFile = open(i, 'rb')
    pdfReader = PyPDF2.PdfReader(pdfFile)
    merger.append(pdfReader)
    pdfFile.close()

merger.write(("Output.pdf"))
merger.close()