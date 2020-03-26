# from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import FormView
from django.contrib import messages
from .forms import ImageForm
from .convert import converter


class FileFieldView(FormView):
    form_class = ImageForm
    template_name = "index.html"  # Replace with your template.
    success_url = "/"  # Replace with your URL or reverse().

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist("file_field")
        # not seeing the files
        print(files)
        if form.is_valid():
            # if len(files) == 1:
            # for f in files:
            # Do something with each file.
            do = converter(files)
            # print(converter(files))

            # print(do)
            messages.info(request, "PDF ready for download")

            return self.form_valid(form)

        else:
            return self.form_invalid(form)
