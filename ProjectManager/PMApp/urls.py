from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create_project", views.create_project, name="create_project"),
    path("view_project/<int:project_id>", views.view_project, name="view_project"),
    path("update_project/<int:project_id>", views.update_project, name="update_project"),
    path("delete_project/<int:project_id>", views.delete_project, name="delete_project"),
    path("view_task", views.view_task, name="view_task"),
    path("create_task", views.create_task, name="create_task"),
    path("update_task", views.update_task, name="update_task"),
    path("delete_task", views.delete_task, name="delete_task")
]