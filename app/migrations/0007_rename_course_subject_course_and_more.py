# Generated by Django 5.0.7 on 2024-07-15 18:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_subject'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subject',
            old_name='Course',
            new_name='course',
        ),
        migrations.RenameField(
            model_name='subject',
            old_name='Staff',
            new_name='staff',
        ),
    ]