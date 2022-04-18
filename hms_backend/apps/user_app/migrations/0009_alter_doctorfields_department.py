# Generated by Django 4.0.3 on 2022-04-13 15:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0002_alter_departments_table'),
        ('user_app', '0008_remove_customuser_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctorfields',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='staff', to='departments.departments'),
        ),
    ]
