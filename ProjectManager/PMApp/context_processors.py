from .models import Project, User


def projects_processor(request):

    # Validate and retrieve current logged in user id
    user_id = request.COOKIES.get("user_id")
    if user_id is None:
        return {"projects": None}
    
    # Retrieve user obj
    user_obj = User.objects.get(user_id=user_id)

    # Retrieve all projects that the user is part of
    project_objs = Project.objects.filter(member__user=user_obj)

    return {"projects": project_objs, "user": user_obj}