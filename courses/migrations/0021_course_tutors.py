# Generated by Django 2.2.6 on 2020-08-16 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0020_auto_20200816_0722'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='tutors',
            field=models.ManyToManyField(to='courses.Tutor'),
        ),
    ]