'''
    Registers any URLS defined there
'''
from django.urls import path, include
from . import views

urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path(r"dashboard/", views.dashboard, name="dashboard"),
    path(r"register/", views.register, name="register"),

]
