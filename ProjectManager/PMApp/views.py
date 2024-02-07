from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # TODO: Index
    return HttpResponse("Index")

def view_project(request):
    # TODO: View project
    return HttpResponse("View Project")

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