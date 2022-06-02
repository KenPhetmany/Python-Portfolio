'''
    Registers any URLS defined there
'''
from django.urls import path
from django.conf .urls import include, url
from . import views

urlpatterns = [
    url("", include("django.contrib.auth.urls")),
    url(r"^dashboard/", views.dashboard, name="dashboard"),
]
