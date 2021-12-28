from django.contrib import admin

from .models import Mailing, Mailpiece, Scan

# Register your models here.
admin.site.register(Mailing)
admin.site.register(Mailpiece)
admin.site.register(Scan)