'''
    Collection of functions that handles the logic that gets processed 
    each time a different URL is visited
'''
from django.shortcuts import render
from projects.models import Project


def project_index(request):
    # Get all objects from the project database
    projects = Project.objects.all()
    # Dictionary context to send information to the template
    context = {
        'projects': projects
    }
    # Any entries in the context dictionary is available in the template
    return render(request, 'project_index.html', context)


def project_detail(request, pk):
    # PK is the primary key to find the project.
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)
