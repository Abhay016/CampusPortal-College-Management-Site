# Generated by Django 5.0.7 on 2024-07-18 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_rename_attendace_attendance'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attendance',
            old_name='session_year',
            new_name='session_year_id',
        ),
        migrations.AlterField(
            model_name='attendance',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='attendancereport',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]