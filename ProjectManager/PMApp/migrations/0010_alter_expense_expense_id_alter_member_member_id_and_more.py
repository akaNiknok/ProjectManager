# Generated by Django 5.0.1 on 2024-02-11 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PMApp', '0009_rename_individualtaskassignment_taskassignment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='expense_id',
            field=models.SmallAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='member',
            name='member_id',
            field=models.SmallAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_id',
            field=models.SmallAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='task',
            name='task_id',
            field=models.SmallAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='taskassignment',
            name='assignment_id',
            field=models.SmallAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_id',
            field=models.SmallAutoField(primary_key=True, serialize=False),
        ),
    ]
