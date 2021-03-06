from django import forms
import datetime


class MailingForm(forms.Form):
    customer = forms.CharField(label='customer name', max_length=100,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    mailing_name = forms.CharField(label='mailing name', max_length=50,
                                   widget=forms.TextInput(attrs={'class': 'form-control'}))
    mailing_dropoff_date = forms.DateField(label='mailing dropoff date',
                                           widget=forms.widgets.DateInput(
                                               attrs={'type': 'date', 'class': 'form-control col-3'}),
                                           initial=datetime.date.today)
    mailing_type_description = forms.CharField(label='mailing type', max_length=50,
                                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    job_number = forms.CharField(label='job_number', max_length=15,
                                 widget=forms.TextInput(attrs={'class': 'form-control'}))
    # file = forms.FileField(label='Mailing File')


# class FileDrop(forms.Form):
#     pass
#     # file = forms.FileField(label="Scans JSON", widget=forms.FileInput())
