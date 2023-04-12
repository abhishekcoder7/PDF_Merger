import PyPDF2

pdf_set = ["Assets\\sample1.pdf", "Assets\\sample2.pdf", "Assets\\sample3.pdf", "Assets\\sample4.pdf"]

merger =PyPDF2.PdfMerger()
for i in pdf_set:
    pdfFile = open(i, 'rb')
    pdfReader = PyPDF2.PdfReader(pdfFile)
    merger.append(pdfReader)
    pdfFile.close()

merger.write(("Output.pdf"))
merger.close()