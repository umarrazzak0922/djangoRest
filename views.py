from django.shortcuts import render
from django.http import HttpResponse
from .forms import uploadFileForm
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.conf import settings
from django.core.files.storage import default_storage
import os


def index(request):
    return HttpResponse("Welcome this is emissions index page.")


def emissionreport(request, year):
    print(year, "THIS IS URL PARAMETER Year")
    return HttpResponse("Welcome this is emissions reporting page.")


def searchemissionreport(request, year):
    if (request.method == 'POST'):
        print(year, "THIS IS QUERY PARAMETER Year")
        print(request.GET['message'], "WEAWEDRSDFD")
        print(request.GET['rt'], "44444444444")
    else:
        print("Request method not allowed")
    return HttpResponse("Welcome this is emissions reporting page.")


def renderEmissionFileUploadPage(request):
    if (request.method == "GET"):
        print(os.path.join(settings.BASE_DIR, '/emissions', '/media/'))
        print(settings.BASE_DIR)
        return render(request, 'emissions_upload_file.html')


@csrf_exempt
def uploadEmissionFile(request):
    if (request.method == 'POST'):
        # print(request.FILES['emission_file'].save(), "These are the files")
        # uploadFileForm()
        file = request.FILES['emission_file']
        file_name = default_storage.save(file.name, file)
        # file = default_storage.open(file_name)
        file_url = default_storage.url(file_name)
        # print(file_url, "FILE URL")

    else:
        print("Request method not allowed")
    return HttpResponse('''
            <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>UPLOAD FILE DEMO DJANGO</title>
</head>
<body>
   <img src="http://localhost:8000/static/uploads/{file_url}"/>

</body>
</html>
        '''.format(file_url=file_url))
