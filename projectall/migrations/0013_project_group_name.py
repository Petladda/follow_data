# Generated by Django 4.1.5 on 2024-01-28 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectall', '0012_remove_project_project_name_remove_subject_amount_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='group_name',
            field=models.CharField(default='', max_length=255),
        ),
    ]
