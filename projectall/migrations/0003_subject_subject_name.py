# Generated by Django 4.1.5 on 2024-01-27 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectall', '0002_subject_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='subject_name',
            field=models.CharField(default='', max_length=255),
        ),
    ]
