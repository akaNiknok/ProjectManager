# Generated by Django 5.0.1 on 2024-02-11 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PMApp', '0005_alter_project_project_end_alter_task_task_deadline_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='expense',
            old_name='expense_description',
            new_name='expense_desc',
        ),
    ]
