# Generated by Django 4.1.5 on 2024-02-09 05:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projectall', '0018_rename_users_project_members_remove_subject_amount'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProductBacklogs',
            new_name='ProductBacklog',
        ),
        migrations.RenameField(
            model_name='productbacklog',
            old_name='product',
            new_name='project',
        ),
        migrations.RenameField(
            model_name='tasks',
            old_name='product_backlogs',
            new_name='product_backlog',
        ),
    ]
