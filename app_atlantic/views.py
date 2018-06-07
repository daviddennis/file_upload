from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# from .forms import UploadFileForm
from app_atlantic.lib.upload import process_file_upload


def index(request):
    return render(request, 'app_atlantic/index.html')

def upload(request):
    context = {
        'upload_status': 'failed'
    }
    data_file = request.FILES.get('daily_file')
    filename = data_file.name
    if data_file:
        context['upload_status'] = 'success'
        process_file_upload(filename, data_file)
    return render(request, 'app_atlantic/upload_complete.html', context)