# Generated by Django 4.0.3 on 2022-04-13 08:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0006_alter_usercontacts_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='email',
        ),
    ]
