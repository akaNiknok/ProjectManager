from django.shortcuts import render, Http404
from django.http import HttpResponse

from .models import Project, User, Member, Task, IndividualTaskAssignment, Expense


def index(request):
    # TODO: Index
    return HttpResponse("Index")

def view_project(request, project_id):
    try:
        project_obj = Project.objects.get(project_id=project_id)
    except:
        raise Http404("Project does not exist")

    return render(request,
                  "view_project.html",
                  {"project": project_obj})

def create_project(request):
    # TODO: Create project 
    return HttpResponse("Create Project")

def update_project(request):
    # TODO: Update project 
    return HttpResponse("Create Project")

def delete_project(request):
    # TODO: Delete project
    return HttpResponse("Delete Project")

def view_task(request):
    # TODO: View task
    return HttpResponse("View Task")

def create_task(request):
    # TODO: Create task 
    return HttpResponse("Create Task")

def update_task(request):
    # TODO: Update task 
    return HttpResponse("Create Task")

def delete_task(request):
    # TODO: Delete task
    return HttpResponse("Delete Task")