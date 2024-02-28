# Generated by Django 5.0.1 on 2024-02-12 14:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PMApp', '0010_alter_expense_expense_id_alter_member_member_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('notif_id', models.SmallAutoField(primary_key=True, serialize=False)),
                ('notif_datetime', models.DateTimeField()),
                ('notif_text', models.TextField()),
                ('notif_status', models.IntegerField(choices=[(0, 'Unread'), (1, 'Read')], default=0)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PMApp.user')),
            ],
        ),
    ]