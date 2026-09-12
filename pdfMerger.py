import PyPDF2
import os

merger = PyPDF2.PdfMerger()

for file in os.listdir(os.curdir):
    if file.endswith(".pdf"):
        print(file)
        merger.append(file)
# Save all the merged PDFs into one file named "combinedDocs.pdf"
# You can change the name in the quotes below to whatever you'd like
merger.write("combinedDocs.pdf")
merger.close()