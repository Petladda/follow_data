# Generated by Django 4.1.5 on 2024-03-04 12:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projectall', '0031_alter_dailyscrum_date'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DailyScrum',
            new_name='StandUpMeeting',
        ),
    ]