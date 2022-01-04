from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .forms import MailingForm
from .models import Mailing, Mailpiece
from .file_handler import handle_uploaded_scans, handle_uploaded_list
from django.views.decorators.csrf import ensure_csrf_cookie
import logging


# Create your views here.
# @ensure_csrf_cookie
def index(request):
    recent_mailings = Mailing.objects.order_by('-id')[:10:-1]
    return render(request, 'index.html', {'recent_mailings': recent_mailings})


# @ensure_csrf_cookie
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


# @ensure_csrf_cookie
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


# @ensure_csrf_cookie
def add_mailing_list(request):
    if request.method == 'POST':
        file = request.FILES['file']
        mailing_id = request.POST.get('mailing_id')
        # logging.error("here")
        # return render(request, 'add_mailing.html')
        # read_headers(file)
        handle_uploaded_list(file, mailing_id)
        return render(request, 'add_scans.html')


# @ensure_csrf_cookie
def mailing_stats(request):
    # mailing_id = 53

    mailing_id = int(request.GET.get('mailing_id'))
    mailing = Mailing.objects.get(id=mailing_id)
    # customer = mailing.customer
    mailing_name = mailing.mailing_name
    logging.error(mailing)
    # mailing_dropoff_date = mailing.mailing_dropoff_date
    # job_number = mailing.job_number
    stats_dict = {}
    zip3_list = mailing.mailpiece_set.all().order_by('zip3').values_list('zip3', flat=True).distinct()
    zip3_list = list(zip3_list)
    zip5_list = mailing.mailpiece_set.all().order_by('zip5').values_list('zip5', flat=True).distinct()
    zip5_list = list(zip5_list)
    pieces = mailing.mailpiece_set.all().order_by('zip5')
    total_pieces = pieces.count()
    stats_dict_zip3 = {}
    total = round(pieces.filter(
        anticipatedDeliveryDate__isnull=False).count() / pieces.count() * 100, 2)
    for zip_partial in zip3_list:
        stats_dict[zip_partial] = round(pieces.filter(
            anticipatedDeliveryDate__isnull=False, zip3__exact=zip_partial).count() / pieces.filter(
            zip3__exact=zip_partial).count() * 100, 2)
    # for zip_partial in zip5_list:
    #     stats_dict[zip_partial] = round(pieces.filter(
    #         anticipatedDeliveryDate__isnull=False, zip5__exact=zip_partial).count() / pieces.filter(
    #         zip5__exact=zip_partial).count() * 100)
    # models.Shop.objects.order_by().values_list('city').distinct()
    # pieces = mailing.mailpiece_set.all().order_by('zip5').values()
    # for piece in pieces:

    return render(request, 'mailing_stats.html',
                  {'zip3s': zip3_list, 'zip5s': zip5_list, 'mailing': mailing, 'stats': stats_dict, 'total': total,
                   'total_pieces': total_pieces})


def receive_data(request):
    if request.method == 'POST':
        logging.error(request)
        return render(request, 'add_scans.html')
        # form = ScansForm(request.POST, request.FILES)
        # if form.is_valid():
    #     handle_uploaded_scans(request.FILES['file'])
    #     return render(request, 'add_scans.html')
    # else:
    #     pass
    #     # form = ScansForm()
    #
    # return render(request, 'add_scans.html')
