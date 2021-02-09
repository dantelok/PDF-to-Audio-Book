import pyttsx3
import pdfplumber
import PyPDF2

file = r'util\Introduction_to_algorithms-3rd-Edition.pdf'

pdfFileObj = open(file, 'rb')

pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

pages = pdfReader.numPages

with pdfplumber.open(file) as pdf:
    # Loop through the number of pages
    # can skip the cover, preface, content page etc.
    for i in range(23, pages):
        page = pdf.pages[i]
        text = page.extract_text()
        print(text)
        speaker = pyttsx3.init()
        speaker.say(text)
        speaker.runAndWait()