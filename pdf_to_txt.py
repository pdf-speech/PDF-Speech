from tkinter import filedialog
import PyPDF2


class PDFToText:
    def __init__(self):
        self.pdf_file_obj = open(filedialog.askopenfilename(initialdir="C:/",
                                                            title="Nilay",
                                                            filetypes=(("PDF files", "*.pdf*"), ("all files", "*.*"))),
                                 'rb')

    def translate_pdf(self):
        pdfreader = PyPDF2.PdfFileReader(self.pdf_file_obj)
        x = pdfreader.numPages
        page_obj = pdfreader.getPage(x - 1)
        text = page_obj.extractText()
        return text

