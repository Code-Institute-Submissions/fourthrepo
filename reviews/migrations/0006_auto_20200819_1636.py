# Generated by Django 2.2.6 on 2020-08-19 16:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0005_comment_datetime'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='text',
            new_name='comment',
        ),
    ]
