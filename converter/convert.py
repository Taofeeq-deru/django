# from django.shortcuts import render
# from PIL import Image
import img2pdf
from django.core.files.storage import FileSystemStorage
from django.utils.crypto import get_random_string


def converter(photos):
    # pdf_list = []
    # pdf_url_list = []
    # fs = FileSystemStorage()
    # pdf_file = get_random_string(length=32)
    # # pdf_file_url
    # # tt
    # # pdf_url_list = []

    # for photo in photos:
    #     # im = Image.open(photo)
    #     img_to_pdf = photo.convert("RGB")
    #     pdf_list.append(img_to_pdf)
    #     # return "new"

    # if len(pdf_list) == 1:
    #     pdf1 = pdf_list[0]
    #     file_name = fs.save(pdf_file.pdf, pdf1)
    #     pdf_file_url = fs.url(file_name)
    #     pdf_url_list.append(pdf_file_url)
    #     # tt = "one pdf"
    #     # return "one"
    # elif len(pdf_list) > 1:
    #     new_list = pdf_list[1:]
    #     file_name = fs.save(pdf_file.pdf, pdf1, save_all=True, append_images=new_list)
    #     pdf_file_url = fs.url(file_name)
    #     pdf_url_list.append(pdf_file_url)
    #     # tt = "multiple pdf"
    #     # return "two"

    # pdf_url = pdf_url_list[0]

    pdf_file = get_random_string(length=32)
    img_file = get_random_string(length=32)
    fs = FileSystemStorage()
    the_pdf = f"{pdf_file}.pdf"
    the_img = f"{img_file}.jpg"
    img_list = []

    # pdf1 = photos.chunks()

    for photo in photos:

        new_photo = img2pdf.convert(photo)

        with open(the_img, "wb") as e:
            e.write(new_photo)

        img_list.append(the_img)

    pdf1 = img2pdf.convert(img_list)

    with open(the_pdf, "wb") as f:
        f.write(pdf1)

    file_name = fs.save(the_pdf)

    pdf_file_url = fs.url(file_name)

    return pdf_file_url

    #    return render(request, "index.html", {"pdf_file_url": pdf_file_url})
