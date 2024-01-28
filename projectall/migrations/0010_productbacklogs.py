# Generated by Django 4.1.5 on 2024-01-28 02:01

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projectall', '0009_dailyscrum'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductBacklogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_to_do', models.DateField(default=datetime.date.today)),
                ('status', models.CharField(choices=[('todo', 'To Do'), ('doing', 'Doing'), ('done', 'Done')], default='todo', max_length=5)),
                ('date_done', models.DateField(default=datetime.date.today)),
                ('important', models.CharField(choices=[('low', 'ต่ำ'), ('mid', 'ปานกลาง'), ('hight', 'มาก')], default='low', max_length=5)),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='projectall.project')),
            ],
        ),
    ]
