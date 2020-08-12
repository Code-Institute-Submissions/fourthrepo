# Generated by Django 2.2.6 on 2020-08-12 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='tutors',
            field=models.ManyToManyField(to='courses.Tutor'),
        ),
        migrations.AddField(
            model_name='tutor',
            name='courses',
            field=models.ManyToManyField(to='courses.Course'),
        ),
    ]
