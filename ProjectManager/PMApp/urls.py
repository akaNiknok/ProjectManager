from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("dashboard/", views.dashboard, name="dashboard"),

    path("switch_project/", views.switch_project, name="switch_project"),
    path("switch_project/<int:project_id>", views.switch_project, name="switch_project"),
    path("create_project/", views.create_project, name="create_project"),
    path("view_project/", views.view_project, name="view_project"),
    path("update_project/", views.update_project, name="update_project"),
    path("archive_project/", views.archive_project, name="archive_project"),
    path("delete_project/", views.delete_project, name="delete_project"),
    path("view_members/", views.view_members, name="view_members"),

    path("create_task/", views.create_task, name="create_task"),
    path("update_task/", views.update_task, name="update_task"),
    path("delete_task/", views.delete_task, name="delete_task"),

    path("create_expense/", views.create_expense, name="create_expense"),
    path("update_expense/", views.update_expense, name="update_expense"),
    path("delete_expense/", views.delete_expense, name="delete_expense"),
]