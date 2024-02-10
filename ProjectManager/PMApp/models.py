from django.db import models
from django.utils.translation import gettext_lazy as _
from datetime import date


class Project(models.Model):

    class Status(models.IntegerChoices):
        ONGOING = 0, _("Ongoing")
        FINISHED = 1, _("Finished")

    project_id = models.AutoField(primary_key=True)
    project_name = models.CharField(max_length=255)
    project_desc = models.TextField()
    project_start = models.DateField(default=date.today)
    project_end = models.DateField(default=None)
    project_status = models.IntegerField(choices=Status, default=Status.ONGOING)

    def __str__(self):
        return "{}: {} ({})".format(self.project_id, self.project_name, self.project_status)


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

    def __str__(self):
        return "{}: {} ({})".format(self.user_id, self.name, self.staff_type)


class Member(models.Model):
    member_id = models.AutoField(primary_key=True)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "{} is a member of {}".format(self.user_id.name, self.project_id.project_name)


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
    task_deadline = models.DateField(default=date.today)
    task_status = models.IntegerField(choices=Status, default=Status.INPROGRESS)
    task_priority = models.CharField(max_length=1, choices=Priority)

    def __str__(self):
        return "{}: {} ({} - {})".format(
            self.task_id,
            self.task_name,
            self.task_status,
            self.task_priority
        )


class IndividualTaskAssignment(models.Model):
    task_assignment_id = models.AutoField(primary_key=True)
    task_id = models.ForeignKey(Task, on_delete=models.CASCADE)
    member_id = models.ForeignKey(Member, on_delete=models.CASCADE)

    def __str__(self):
        return "{} is tasked to {}".format(self.member_id.user_id.name, self.task_id.task_name)


class Expense(models.Model):
    expense_id = models.AutoField(primary_key=True)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    member_id = models.ForeignKey(Member, on_delete=models.CASCADE)
    expense_date = models.DateField(default=date.today)
    expense_description = models.TextField()
    expense_amount = models.DecimalField(max_digits=11, decimal_places=2)  # TODO: Change in data dictionary

    def __str__(self):
        return "{}: PHP {} to {}".format(
            self.expense_id,
            self.expense_amount,
            self.project_id.project_name
        )