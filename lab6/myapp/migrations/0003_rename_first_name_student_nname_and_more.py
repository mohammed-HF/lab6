# Generated by Django 4.2.5 on 2023-11-04 16:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0002_remove_student_email_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="student", old_name="first_name", new_name="nname",
        ),
        migrations.RemoveField(model_name="student", name="last_name",),
    ]
