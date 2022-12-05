import re
import PyPDF2

def extract_txt_from_pdf(pdf_file: str) -> [str]:
    with open(pdf_file, 'rb') as pdf:
        reader = PyPDF2.PdfFileReader(pdf, strict=False)
        pdf_text = []

        for page in reader.pages:
            content = page.extractText()
            pdf_text.append(content)

        return pdf_text

if __name__ == '__main__':
    rFileName = '123.pdf'
    extracted_text = extract_txt_from_pdf(rFileName)
    wFileName=rFileName.replace('.pdf', '.txt' ,1)
    with open(wFileName, 'w', encoding="utf-8") as wFile:
        for text in extracted_text:
            wFile.write(text)


