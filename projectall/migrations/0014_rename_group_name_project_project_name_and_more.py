# Generated by Django 4.1.5 on 2024-01-28 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectall', '0013_project_group_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='group_name',
            new_name='project_name',
        ),
        migrations.RemoveField(
            model_name='subject',
            name='project_name',
        ),
        migrations.AddField(
            model_name='subject',
            name='amount',
            field=models.PositiveBigIntegerField(default=0),
        ),
    ]
