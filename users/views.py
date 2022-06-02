'''
    Collection of functions that handles the logic that 
    gets processed each time a different URL is visited
'''
from django.shortcuts import render


def dashboard(request):
    return render(request, "users/dashboard.html")
