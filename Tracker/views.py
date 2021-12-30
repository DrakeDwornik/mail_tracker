from django.shortcuts import render
from django.http import HttpResponse
from .forms import MailingForm
from .models import Mailing
from .file_handler import handle_uploaded_file
# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def add_mailing(request):
    if request.method == 'POST':
        form = MailingForm(request.POST, request.FILES)
        if form.is_valid():
            mailing = Mailing()
            mailing.customer = request.POST.get('customer')
            mailing.mailing_dropoff_date = request.POST.get('mailing_dropoff_date')
            mailing.mailing_type_description = request.POST.get('mailing_type_description')
            mailing.job_number = request.POST.get('job_number')
            mailing.save()
            handle_uploaded_file(request.FILES['file'], mailing.pk)
        return render(request, 'add_mailing.html', {'form': form})
    else:
        form = MailingForm()

    return render(request, 'add_mailing.html', {'form': form})