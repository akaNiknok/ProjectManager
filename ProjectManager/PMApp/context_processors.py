from .models import Project


def projects_processor(request):
    projects = Project.objects.all()
    return {"projects": projects}