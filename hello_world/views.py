'''
    Collection of functions that handles the logic that gets processed 
    each time a different URL is visited
'''

from django.shortcuts import render


def hello_world(request):
    return render(request, 'hello_world.html', {})
