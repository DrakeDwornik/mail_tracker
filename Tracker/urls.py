from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_mailing', name='add_mailing', view=views.add_mailing),
    path('add_scans', name='add_scans', view=views.add_scans)
]