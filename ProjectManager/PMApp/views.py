from django.shortcuts import render, redirect, Http404
from django.http import HttpResponse

from .models import Project, User, Member, Task, TaskAssignment, Expense

def index(request):
    # TODO: Login
    return redirect("dashboard")


def dashboard(request):

    # Retrieve all objects
    # TODO: Retrieve only user related projects
    project_objs = Project.objects.all()

    # Default to the first project, when not specified
    try:
        project_id = request.session["current_project_id"]
        project_obj = Project.objects.get(project_id=project_id)
    except:
        request.session["current_project_id"] = 0
        project_obj = project_objs[0]
        project_id = project_obj.project_id
    
    # Get tasks and expenses
    task_objs = Task.objects.filter(project_id=project_id)
    expense_objs = Expense.objects.filter(project_id=project_id)
        
    return render(request,
                  "dashboard.html",
                  {"project": project_obj, "tasks": task_objs, "expenses": expense_objs})


def switch_project(request, project_id):
    request.session["current_project_id"] = int(project_id)

    previous_url = request.META.get("HTTP_REFERER")
    previous_view = previous_url.rstrip('/').split('/')[-1]

    # If user was in update_project, redirect to view_project to prevent unwanted changes
    if previous_view == "update_project":
        previous_url = "view_project"

    return redirect(previous_url)


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

        return redirect("view_project")

    # Otherwise, display the form
    else:
        return render(request,
                    "create_project.html")


def view_project(request):

    project_id = request.session["current_project_id"]

    try:
        project_obj = Project.objects.get(project_id=project_id)
    except:
        raise Http404("Project does not exist")

    return render(request,
                  "view_project.html",
                  {"project": project_obj})


def update_project(request):

    project_id = request.session["current_project_id"]

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

        return redirect("view_project")

    # Otherwise, display the form
    else:
        try:
            project_obj = Project.objects.get(project_id=project_id)
        except:
            raise Http404("Project does not exist")

        return render(request,
                    "update_project.html",
                    {"project": project_obj})


def archive_project(request):

    project_id = request.session["current_project_id"]

    # Get project object
    try:
        project_obj = Project.objects.get(project_id=project_id)
    except:
        raise Http404("Project does not exist")

    # Update project status to "Archived"
    project_obj.project_status = 2
    project_obj.save()

    return redirect("view_project")


def delete_project(request):

    project_id = request.session["current_project_id"]

    # Get project object
    try:
        project_obj = Project.objects.get(project_id=project_id)
    except:
        raise Http404("Project does not exist")

    # Delete object
    project_obj.delete()

    return redirect("dashboard")


def create_task(request):
    # Create task when user clicks submit
    if (request.method == "POST"):

        # Get submitted form values
        task_name = request.POST.get("task_name")
        task_notes = request.POST.get("task_notes")
        task_priority = request.POST.get("task_priority")
        task_deadline = request.POST.get("task_deadline")

        # Set deadline to None if not specified
        if task_deadline == "":
            task_deadline = None

        # Get current selected projected using the session variable
        current_project = Project.objects.get(project_id=request.session["current_project_id"])

        # Create and save the new project
        Task.objects.create(
            project=current_project,
            task_name=task_name,
            task_notes=task_notes,
            task_priority=task_priority,
            task_deadline=task_deadline
        )

        return redirect("dashboard")

    # Otherwise, redirect to dashboard 
    else:
        return redirect("dashboard")


def update_task(request):
    # TODO: Update task 
    return HttpResponse("Create Task")


def delete_task(request):
    # TODO: Delete task
    return HttpResponse("Delete Task")


def view_members(request):
    # TODO: View members
    return render(request, "view_members.html")


def create_expense(request):
    # TODO: Create expense 
    return HttpResponse("Create expense")


def update_expense(request):
    # TODO: Update expense 
    return HttpResponse("Update expense")


def delete_expense(request):
    # TODO: Delete expense
    return HttpResponse("Delete expense")