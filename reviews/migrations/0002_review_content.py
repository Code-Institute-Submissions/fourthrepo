# Generated by Django 2.2.6 on 2020-08-13 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='content',
            field=models.TextField(default='Great!'),
            preserve_default=False,
        ),
    ]
