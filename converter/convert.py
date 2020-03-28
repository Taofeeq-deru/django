# from django.shortcuts import render
# from PIL import Image
# import img2pdf
from django.core.files.storage import FileSystemStorage
from django.core.files.base import ContentFile
from django.utils.crypto import get_random_string

# rom PyPDF2 import PdfFileMerger


# def converter(photos):
#     pdf_list = []
#     pdf_url_list = []
#     fs = FileSystemStorage()
#     pdf_file = get_random_string(length=32)
#     # # pdf_file_url
#     # # tt
#     # # pdf_url_list = []

#     for photo in photos:
#         im = photo.open()
#         img_to_pdf = im.convert("RGB")
#         pdf_list.append(img_to_pdf)
#     #     # return "new"

#     if len(pdf_list) == 1:
#         pdf1 = pdf_list[0]
#         file_name = fs.save(f"{pdf_file}.pdf", pdf1)
#         pdf_file_url = fs.url(file_name)
#         pdf_url_list.append(pdf_file_url)
#     #     # tt = "one pdf"
#     #     # return "one"
#     elif len(pdf_list) > 1:
#         pdf1 = pdf_list[0]
#         new_list = pdf_list[1:]
#         file_name = fs.save(
#             f"{pdf_file}.pdf", pdf1, save_all=True, append_images=new_list
#         )
#         pdf_file_url = fs.url(file_name)
#         pdf_url_list.append(pdf_file_url)
#     #     # tt = "multiple pdf"
#     #     # return "two"

#     pdf_url = pdf_url_list[0]

#     return pdf_url

#     # pdf_file = get_random_string(length=32)
#     # img_file = get_random_string(length=32)


def converter(photo):
    # pdf1_file = get_random_string(length=7)
    # main_pdf_file = get_random_string(length=8)
    fs = FileSystemStorage()
    # the_pdf1 = f"{pdf1_file}.pdf"
    # main_pdf = f"{main_pdf_file}.pdf"
    # merger = PdfFileMerger()
    # pdfs = []
    # the_img = f"{img_file}.jpg"
    # img_list = []

    # pdf1 = photos.chunks()
    x = ContentFile("Hello world!")
    file = fs.save("file.pdf", x)
    path = fs.path(file)

    # for photo in photos:
    pdf1 = photo.read()

    with open(path, "wb") as f:
        f.write(pdf1)

        # pdfs.append(f"{pdf1_file}.pdf")

    # for pdf in pdfs:
    #     merger.append(pdf)

    # merger.write(main_pdf)

    # pdf = pdfs[0]

    # file_name = fs.save("my_pdf.pdf", pdf)

    pdf = fs.save("document.pdf", ContentFile(path))

    pdf_url = fs.url(pdf)

    # file_name = fs.save(main_pdf)

    # pdf_url = fs.url(file_name)

    # merger.close()

    return pdf_url


#     # new_photo = img2pdf.convert(photo)

#     new_photo = photo.read()

#     with open(the_img, "wb") as e:
#         e.write(new_photo)

#     img_list.append(the_img)

# pdf1 = img2pdf.convert(img_list)

# pdf1 = photos.read()

# with open(the_pdf, "wb") as f:
#     f.write(pdf1)

# file_name = fs.save(the_pdf)

# pdf_file_url = fs.url(file_name)
# return pdf_file_url

#    return render(request, "index.html", {"pdf_file_url": pdf_file_url})
