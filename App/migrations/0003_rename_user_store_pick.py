# Generated by Django 3.2.9 on 2021-11-18 21:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_alter_user_dob'),
    ]

    operations = [
        migrations.RenameField(
            model_name='store',
            old_name='user',
            new_name='pick',
        ),
    ]