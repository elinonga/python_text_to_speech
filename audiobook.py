import PyPDF2
import pyttsx3

# Read the pdf & specify the path
pdfFileObj = PyPDF2.PdfFileReader(open('./attachments/sample.pdf', 'rb'))

# Get the handle to the text-to-speech engine
engine = pyttsx3.init()

# Get the number of pages in the pdf
num_pages = pdfFileObj.numPages

# Loop through each page
for i in range(num_pages):

    # Get the page
    page = pdfFileObj.getPage(i)

    # Get the text from the page
    text = page.extractText()

    # Speak the text
    engine.say(text)
    engine.runAndWait()

# stop the engine
engine.stop()

# save the audio file
engine.save_to_file(text, './attachments/sample.mp3')
engine.runAndWait()
    
