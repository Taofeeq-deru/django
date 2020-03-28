# from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import FormView
from django.contrib import messages
from .forms import ImageForm
from .convert import converter


class ImageView(FormView):
    form_class = ImageForm
    template_name = "index.html"  # Replace with your template.
    success_url = "/"  # Replace with your URL or reverse().

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        images = request.FILES["image"]
        # not seeing the files
        print(images)
        if form.is_valid():
            # if len(files) == 1:
            # for f in files:
            # Do something with each file.
            pdf_url = converter(images)

            print(pdf_url)
            messages.info(request, "PDF ready for download")

            return render(request, "index.html", {"pdf_url": pdf_url})

        else:
            return self.form_invalid(form)


# def image_upload(request):
#     if request.method = 'POST':
