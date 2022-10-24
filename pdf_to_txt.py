import PyPDF2


class PDFToText:
    def __init__(self):
        # create file object variable
        # opening method will be rb
        self.pdf_file_obj = open('assets/gd.pdf', 'rb')

    def translate_pdf(self):
        # create reader variable that will read the pdf_file_obj
        pdfreader = PyPDF2.PdfFileReader(self.pdf_file_obj)

        # This will store the number of pages of this pdf file
        x = pdfreader.numPages
        # print(x)

        # create a variable that will select the selected number of pages
        page_obj = pdfreader.getPage(x-1)

        # (x+1) because python indentation starts with 0.
        # create text variable which will store all text data from pdf file
        text = page_obj.extractText()
        return text

        # save the extracted data from pdf to a txt file
        # we will use file handling here
        # don't forget to put r before you put the file path
        # go to the file location copy the path by right-clicking on the file
        # click properties and copy the location path and paste it here.
        # put "\\your_txt-filename"
        # file1 = open(r"C:\Users\Yash\AppData\Local\Programs\Python\Python310\gd.txt", "w")
        # file1 = open("assets\gd.txt", "w")
        # file1.writelines(text)
