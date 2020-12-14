from PyPDF2 import PdfFileReader
import os

import pdfplumber 

class TextExtractor:

    def __init__(self):
        self.current_location = os.path.dirname(__file__)

    # Works well.
    def pdfplumber_extract(self, file_location):
        with pdfplumber.open(self.current_location+file_location) as file :
            page = file.pages[0]
            return page.extract_text()

    # Does not work with scanned documents at all.
    def PyPDF2(self, file_location):
        pdfFile = PdfFileReader(self.current_location+file_location)
        page = pdfFile.getPage(0)
        return page.extractText()

if __name__ == "__main__":
    textExtractor = TextExtractor()
    # Simple document
    #print(textExtractor.pdfplumber_extract('../ssoar_dataset/ssoar_datasetniehaus_et_al-gestandnismotivierung_in_beschuldigtenvernehmungen-ocr.pdf'))

    # Slightly complicated document
    #print(textExtractor.pdfplumber_extract('../ssoar_dataset/ssoar_datasetssoar-1986-reichertz_et_al-kontaktanzeigen_-_auf_der_suche.pdf'))

    # Super complicated document + multi column. 
    # A problem here is that multi column is treated as single column because it is a scanned document.
    print(textExtractor.pdfplumber_extract('../ssoar_dataset/ssoar_datasetssoar-1992-sfb_186_report_nr_1.pdf'))