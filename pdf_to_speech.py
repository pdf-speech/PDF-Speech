# importing the modules
import PyPDF2
import pyttsx3
  
# path of the PDF file
path = open('Brief history of time.pdf', 'rb')
  
# creating a PdfFileReader object
pdfReader = PyPDF2.PdfFileReader(path)
  
# the page with which you want to start
# this will read the book of 25th page.
from_page = pdfReader.getPage(30)
  
# extracting the text from the PDF
entry_text = from_page.extractText()
  
# reading the text
# speak = pyttsx3.init()
# speak.say(text)
# speak.runAndWait()