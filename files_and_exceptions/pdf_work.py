"""This file contains code snippets in working with pdf files"""
# extract_doc_info.py

# from PyPDF2 import PdfFileReader, , PdfFileWriter


def extract_information(pdf_path):
    with open(pdf_path, 'rb') as f:
        pdf = PdfFileReader(f)
        information = pdf.getDocumentInfo()
        number_of_pages = pdf.getNumPages()

    txt = f"""
    Information about {pdf_path}: 

    Author: {information.author}
    Creator: {information.creator}
    Producer: {information.producer}
    Subject: {information.subject}
    Title: {information.title}
    Number of pages: {number_of_pages}
    """

    print(txt)
    return information


if __name__ == '__main__':
    path = 'reportlab-sample.pdf'
    extract_information(path)

# rotate_pages.py


def rotate_pages(pdf_path):
    pdf_writer = PdfFileWriter()
    pdf_reader = PdfFileReader(path)
    # Rotate page 90 degrees to the right
    page_1 = pdf_reader.getPage(0).rotateClockwise(90)
    pdf_writer.addPage(page_1)
    # Rotate page 90 degrees to the left
    page_2 = pdf_reader.getPage(1).rotateCounterClockwise(90)
    pdf_writer.addPage(page_2)
    # Add a page in normal orientation
    pdf_writer.addPage(pdf_reader.getPage(2))

    with open('rotate_pages.pdf', 'wb') as fh:
        pdf_writer.write(fh)

if __name__ == '__main__':
    path = 'Jupyter_Notebook_An_Introduction.pdf'
    rotate_pages(path)

# pdf_merging.py


def merge_pdfs(paths, output):
    pdf_writer = PdfFileWriter()

    for path in paths:
        pdf_reader = PdfFileReader(path)
        for page in range(pdf_reader.getNumPages()):
            # Add each page to the writer object
            pdf_writer.addPage(pdf_reader.getPage(page))

    # Write out the merged PDF
    with open(output, 'wb') as out:
        pdf_writer.write(out)

if __name__ == '__main__':
    paths = ['document1.pdf', 'document2.pdf']
    merge_pdfs(paths, output='merged.pdf')

# pdf_splitting.py


def split(path, name_of_split):
    pdf = PdfFileReader(path)
    for page in range(pdf.getNumPages()):
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(pdf.getPage(page))

        output = f'{name_of_split}{page}.pdf'
        with open(output, 'wb') as output_pdf:
            pdf_writer.write(output_pdf)

if __name__ == '__main__':
    path = 'Jupyter_Notebook_An_Introduction.pdf'
    split(path, 'jupyter_page')

# pdf_watermarker.py


def create_watermark(input_pdf, output, watermark):
    watermark_obj = PdfFileReader(watermark)
    watermark_page = watermark_obj.getPage(0)

    pdf_reader = PdfFileReader(input_pdf)
    pdf_writer = PdfFileWriter()

    # Watermark all the pages
    for page in range(pdf_reader.getNumPages()):
        page = pdf_reader.getPage(page)
        page.mergePage(watermark_page)
        pdf_writer.addPage(page)

    with open(output, 'wb') as out:
        pdf_writer.write(out)

if __name__ == '__main__':
    create_watermark(
        input_pdf='Jupyter_Notebook_An_Introduction.pdf',
        output='watermarked_notebook.pdf',
        watermark='watermark.pdf')

"""
create_watermark() accepts three arguments:

input_pdf: the PDF file path to be watermarked
output: the path you want to save the watermarked version of the PDF
watermark: a PDF that contains your watermark image or text
In the code, you open up the watermark PDF and grab just the first page from the
docs as that is where your watermark should reside. Then you create a PDF
reader object using the input_pdf and a generic pdf_writer object for writing 
out the watermarked PDF.

The next step is to iterate over the pages in the input_pdf. This is where the 
magic happens. You will need to call .mergePage() and pass it the 
watermark_page. When you do that, it will overlay the watermark_page on top of 
the current page. Then you add that newly merged page to your pdf_writer object.

Finally, you write the newly watermarked PDF out to disk, and you’re done!
"""

# How to Encrypt a PDF
"""
PyPDF2 currently only supports adding a user password and an owner password to a
preexisting PDF. In PDF land, an owner password will basically give you 
administrator privileges over the PDF and allow you to set permissions on the 
docs. On the other hand, the user password just allows you to open the 
docs.

As far as I can tell, PyPDF2 doesn’t actually allow you to set any permissions 
on the docs even though it does allow you to set the owner password.

Regardless, this is how you can add a password, which will also inherently 
encrypt the PDF:
"""
# pdf_encrypt.py


def add_encryption(input_pdf, output_pdf, password):
    pdf_writer = PdfFileWriter()
    pdf_reader = PdfFileReader(input_pdf)

    for page in range(pdf_reader.getNumPages()):
        pdf_writer.addPage(pdf_reader.getPage(page))

    pdf_writer.encrypt(user_pwd=password, owner_pwd=None,
                       use_128bit=True)

    with open(output_pdf, 'wb') as fh:
        pdf_writer.write(fh)

if __name__ == '__main__':
    add_encryption(input_pdf='reportlab-sample.pdf',
                   output_pdf='reportlab-encrypted.pdf',
                   password='twofish')

