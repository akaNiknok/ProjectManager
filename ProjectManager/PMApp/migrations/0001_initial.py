# Generated by Django 5.0.1 on 2024-02-05 15:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('project_id', models.AutoField(primary_key=True, serialize=False)),
                ('project_name', models.CharField(max_length=255)),
                ('project_desc', models.TextField()),
                ('project_start', models.DateField()),
                ('project_end', models.DateField()),
                ('project_status', models.IntegerField(choices=[(0, 'Ongoing'), (1, 'Finished')], default=0)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('staff_type', models.CharField(choices=[('X', 'Executive'), ('M', 'Manager'), ('Em', 'Employee')], default='Em', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('member_id', models.AutoField(primary_key=True, serialize=False)),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PMApp.project')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PMApp.user')),
            ],
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('expense_id', models.AutoField(primary_key=True, serialize=False)),
                ('expense_date', models.DateField()),
                ('expense_description', models.TextField()),
                ('expense_amount', models.DecimalField(decimal_places=2, max_digits=11)),
                ('member_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PMApp.member')),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PMApp.project')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('task_id', models.AutoField(primary_key=True, serialize=False)),
                ('task_name', models.CharField(max_length=255)),
                ('task_notes', models.TextField()),
                ('task_status', models.IntegerField(choices=[(0, 'In Progress'), (1, 'For Review'), (3, 'Completed')], default=0)),
                ('task_priority', models.CharField(choices=[('H', 'High'), ('M', 'Medium'), ('L', 'Low')], max_length=1)),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PMApp.project')),
            ],
        ),
        migrations.CreateModel(
            name='IndividualTaskAssignment',
            fields=[
                ('task_assignment_id', models.AutoField(primary_key=True, serialize=False)),
                ('member_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PMApp.member')),
                ('task_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PMApp.task')),
            ],
        ),
    ]
