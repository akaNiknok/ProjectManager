from .models import Project, Member, User


def projects_processor(request):
    # Retrieve current logged in user id
    user_id = request.COOKIES.get("user_id")

    if user_id is None:
        return redirect("login")
    
    member_objs = Member.objects.filter(user_id = user_id)
    projects = Project.objects.filter(project_id__in = member_objs.values_list('project__project_id', flat = True)).distinct()

    return {"projects": projects}
