# Generated by Django 2.2.6 on 2020-08-13 08:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_auto_20200813_0855'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='date',
            new_name='datetime',
        ),
    ]