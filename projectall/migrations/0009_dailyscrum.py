# Generated by Django 4.1.5 on 2024-01-28 01:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projectall', '0008_student_group'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyScrum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('yesterday', models.CharField(max_length=1000)),
                ('today', models.CharField(max_length=1000)),
                ('problem', models.CharField(max_length=1000)),
                ('note', models.CharField(choices=[('work', 'วันนี่ทำงาน'), ('sick', 'ป่วย'), ('busy', 'ติดธุระ'), ('pass', 'ตกลงกันว่าวันนี้ไม่ทำงาน')], max_length=4)),
                ('others', models.TextField(max_length=255)),
                ('student', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
