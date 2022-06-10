'''
    Collection of functions that handles the logic that 
    gets processed each time a different URL is visited
'''
from django.shortcuts import redirect, render
from django.contrib.auth import login
from django.urls import reverse
from users.forms import CustomerUserCreationForm


def dashboard(request):
    return render(request, "users/dashboard.html")


def register(request):
    if request.method == "GET":
        return render(
            request, "users/register.html",
            {"form": CustomerUserCreationForm}
        )
    elif request.method == "POST":
        form = CustomerUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("dashboard"))
