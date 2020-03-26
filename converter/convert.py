# from django.shortcuts import render
from PIL import Image
from django.core.files.storage import FileSystemStorage
from django.utils.crypto import get_random_string


def converter(images):
    pdf_list = []
    pdf_url_list = []
    fs = FileSystemStorage()
    pdf_file = get_random_string(length=32)
    # pdf_file_url
    # tt
    # pdf_url_list = []

    for image in images:
        im = Image.open(image)
        img_to_pdf = im.convert("RGB")
        pdf_list.append(img_to_pdf)
        # return "new"

    if len(pdf_list) == 1:
        pdf1 = pdf_list[0]
        file_name = fs.save(pdf_file, pdf1)
        pdf_file_url = fs.url(file_name)
        pdf_url_list.append(pdf_file_url)
        # tt = "one pdf"
        # return "one"
    elif len(pdf_list) > 1:
        new_list = pdf_list[1:]
        file_name = fs.save(pdf_file, pdf1, save_all=True, append_images=new_list)
        pdf_file_url = fs.url(file_name)
        pdf_url_list.append(pdf_file_url)
        # tt = "multiple pdf"
        # return "two"

    # pdf_url = pdf_url_list[0]

    return images

    #    return render(request, "index.html", {"pdf_file_url": pdf_file_url})
