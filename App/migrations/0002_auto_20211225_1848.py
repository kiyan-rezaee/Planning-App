# Generated by Django 3.2.10 on 2021-12-25 18:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='Category',
        ),
        migrations.RemoveField(
            model_name='course',
            name='study_goal',
        ),
    ]