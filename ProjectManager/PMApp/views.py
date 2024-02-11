from django.shortcuts import render, redirect, Http404
from django.http import HttpResponse

from .models import Project, User, Member, Task, IndividualTaskAssignment, Expense


# TODO: Rename to dashboard and create a new index
def index(request):

    # Retrieve all objects
    # TODO: Retrieve only user related projects
    project_objs = Project.objects.all()

    # Retrieve selected projected
    selected_id = request.GET.get("id")

    # Default to the first project, when not specified
    if selected_id is None:
        selected_project = project_objs[0]
    else:
        selected_project = Project.objects.get(project_id=selected_id)

    return render(request,
                  "dashboard.html",
                  {"projects": project_objs,
                   "selected_project": selected_project})


def create_project(request):

    # Create project when user clicks submit
    if (request.method == "POST"):

        # Get submitted form values
        project_name = request.POST.get("project_name")
        project_desc = request.POST.get("project_desc")
        project_start = request.POST.get("project_start")
        project_end = request.POST.get("project_end")
        project_status = request.POST.get("project_status")

        # Set project end date to None if none specified
        if project_end == "":
            project_end = None

        # Create and save the new project
        new_project = Project.objects.create(
            project_name=project_name,
            project_desc=project_desc,
            project_start=project_start,
            project_end=project_end,
            project_status=project_status
        )

        return redirect("view_project", project_id=new_project.project_id)

    # Otherwise, display the form
    else:
        return render(request,
                    "create_project.html")


def view_project(request, project_id):
    try:
        project_obj = Project.objects.get(project_id=project_id)
    except:
        raise Http404("Project does not exist")

    return render(request,
                  "view_project.html",
                  {"project": project_obj})


def update_project(request, project_id):

    # Update project details when user clicks submit
    if (request.method == "POST"):

        # Get submitted form values
        project_name = request.POST.get("project_name")
        project_desc = request.POST.get("project_desc")
        project_start = request.POST.get("project_start")
        project_end = request.POST.get("project_end")
        project_status = request.POST.get("project_status")

        # Create and save the new project
        if project_end == "":
            project_end = None

        # Retrieve and edit the values of the project
        project_obj = Project.objects.get(project_id=project_id)

        project_obj.project_name = project_name
        project_obj.project_desc = project_desc
        project_obj.project_start = project_start
        project_obj.project_end = project_end
        project_obj.project_status = project_status

        project_obj.save()

        return redirect("view_project", project_id=project_obj.project_id)

    # Otherwise, display the form
    else:
        try:
            project_obj = Project.objects.get(project_id=project_id)
        except:
            raise Http404("Project does not exist")

        return render(request,
                    "update_project.html",
                    {"project": project_obj})


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