from django import forms


class MailingForm(forms.Form):
    customer = forms.CharField(label='customer name', max_length=100)
    mailing_name = forms.CharField(label='mailing name', max_length=50)
    mailing_dropoff_date = forms.DateField(label='mailing dropoff date')
    mailing_type_description = forms.CharField(label='mailing type', max_length=50)
    job_number = forms.CharField(label='job_number', max_length=15)
    file = forms.FileField(label='Mailing File')
