# AUDIOBOOK READER

# Step 1 - Download and install the package pyttsx3. (pip install pyttsx)
#  This package is the speech to text converter.
#  Documentation -https://pypi.org/project/pyttsx3/

# Step 2 - Download and install the package PyPDF2
#  This package will extract text from your pdf files.
#  Documentation - https://pythonhosted.org/PyPDF2/

# Step 3 - Import the packages

import pyttsx3
import PyPDF2

# Step 4 - Import the book you want this application to read

book=open('ME.pdf','rb')
pdfReader=PyPDF2.PdfFileReader(book)
pages=pdfReader.numPages

# Step 5- initialise the speaker object.

speaker= pyttsx3.init()
rate = speaker.getProperty('rate')   # getting details of current speaking rate
print(rate)                          #printing current voice rate
speaker.setProperty('rate', 160)

# Step 6- Run the code in a loop from the page you want the reader to read.
for num in range(2,pages):
    page=pdfReader.getPage(0)
    text=page.extractText()
    speaker.say(text)
    speaker.runAndWait()

speaker.stop()


