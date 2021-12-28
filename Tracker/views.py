from django.shortcuts import render
from django.http import HttpResponse
from .forms import MailingForm
# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def add_mailing(request):
    if request.method == 'POST':
        form = MailingForm(request.POST)
        if form.is_valid():
            pass

    else:
        form = MailingForm()

    return render(request, 'add_mailing.html', {'form': form})