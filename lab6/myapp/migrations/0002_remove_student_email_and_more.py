# Generated by Django 4.2.5 on 2023-11-04 16:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(model_name="student", name="email",),
        migrations.RemoveField(model_name="student", name="registration_date",),
    ]