from django.urls import path

from . import views

urlpatterns = [
    path('', name='index', view=views.index),
    path('add_mailing', name='add_mailing', view=views.add_mailing),
    path('add_scans', name='add_scans', view=views.add_scans),
    path('add_mailing_list', name='add_mailing_list', view=views.add_mailing_list),
    path('mailing_stats', name='mailing_stats', view=views.mailing_stats),
    path('receive_data', name='receive_data', view=views.receive_data)
]
