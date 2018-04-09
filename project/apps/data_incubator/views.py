from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from project import settings


class UploadImageView(TemplateView):
    template_name = "upload_image.html"

    def post(self, request):
        if request.method == 'POST' and request.FILES['my_file']:
            my_file = request.FILES['my_file']
            fs = FileSystemStorage()
            filename = fs.save(my_file.name, my_file)
            uploaded_file_url = fs.url(filename)
            return redirect(settings.MEDIA_URL + my_file.name)

        return render(request, self.template_name, {})
