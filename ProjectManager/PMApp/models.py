from django.db import models
from django.utils.translation import gettext_lazy as _


class Project(models.Model):

    class Status(models.IntegerChoices):
        ONGOING = 0, _("Ongoing")
        FINISHED = 1, _("Finished")

    project_id = models.AutoField(primary_key=True)
    project_name = models.CharField(max_length=255)
    project_desc = models.TextField()
    project_start = models.DateField()
    project_end = models.DateField()
    project_status = models.IntegerField(choices=Status, default=Status.ONGOING)


class User(models.Model):

    class sType(models.TextChoices):
        EXECUTIVE = "X", _("Executive")
        MANAGER = "M", _("Manager")
        EMPLOYEE = "Em", _("Employee")

    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)  # TODO: password encryption
    # TODO: profile pics
    staff_type = models.CharField(max_length=2, choices=sType, default=sType.EMPLOYEE)


class Member(models.Model):
    member_id = models.AutoField(primary_key=True)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)


class Task(models.Model):

    class Status(models.IntegerChoices):
        INPROGRESS = 0, _("In Progress")
        FORREVIEW = 1, _("For Review")
        COMPLETED = 3, _("Completed")
    
    class Priority(models.TextChoices):
        HIGH = "H", _("High")
        MEDIUM = "M", _("Medium")
        LOW = "L", _("Low")

    task_id = models.AutoField(primary_key=True)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=255)
    task_notes = models.TextField()
    task_status = models.IntegerField(choices=Status, default=Status.INPROGRESS)
    task_priority = models.CharField(max_length=1, choices=Priority)


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
    expense_amount = models.DecimalField(max_digits=11, decimal_places=2)  # TODO: Change in data dictionary
