from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .forms import MailingForm
from .models import Mailing, Mailpiece
from .file_handler import handle_uploaded_scans, handle_uploaded_list
import logging


# Create your views here.
def index(request):
    recent_mailings = Mailing.objects.order_by('-id')[:10:-1]
    return render(request, 'index.html', {'recent_mailings': recent_mailings})


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
            # handle_uploaded_list(request.FILES['file'], mailing.pk)
            return render(request, 'add_mailing_list.html', {'mailing_id': mailing.pk})
        return render(request, 'add_mailing.html', {'form': form})
    else:
        form = MailingForm()

    return render(request, 'add_mailing.html', {'form': form})


def add_scans(request):
    if request.method == 'POST':
        # form = ScansForm(request.POST, request.FILES)
        # if form.is_valid():
        handle_uploaded_scans(request.FILES['file'])
        return render(request, 'add_scans.html')
    else:
        pass
        # form = ScansForm()

    return render(request, 'add_scans.html')


def add_mailing_list(request):
    if request.method == 'POST':
        file = request.FILES['file']
        mailing_id = request.POST.get('mailing_id')
        logging.error("here")
        # return render(request, 'add_mailing.html')
        # read_headers(file)
        handle_uploaded_list(file, mailing_id)
        return render(request, 'add_scans.html')
