from django.db import models


class Project(models.Model):
    project_id = models.AutoField(primary_key=True)
    project_name = models.CharField(max_lenth=255)
    project_desc = models.TextField()
    project_start = models.DateField()
    project_end = models.DateField()
    project_status  # TODO: Enum


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_lenth=255)
    username = models.CharField(max_lenth=255)
    password = models.CharField(max_lenth=255)  # TODO: password encryption
    profile_pic  # TODO: profile pics
    staff_type   # TODO: staff type


class Member(models.Model):
    member_id = models.AutoField(primary_key=True)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)


class Task(models.Model):
    task_id = models.AutoField(primary_key=True)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    task_name = models.CharField(max_lenth=255)
    task_notes = models.TextField()
    task_status  # TODO: task status
    task_priority  # TODO: task status


class IndividualTaskAssignment(models.Model):
    task_assignment_id = models.AutoField(primary_key=True)
    task_id = models.ForeignKey(Task, on_delete=models.CASCADE)
    member_id = models.ForeignKey(Member, on_delete=models.CASCADE)


class Expense(models.Model):
    expense_id = models.AutoField(primary_key=True)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    member_id = models.ForeignKey(Member, on_delete=models.CASCADE)
    expense_date = models.DateField()
    expense_description = models.TextField()
    expense_amount = models.DecimalField()  # TODO: Change in data dictionary
