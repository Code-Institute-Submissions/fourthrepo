# Generated by Django 2.2.6 on 2020-08-15 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_course_cost'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='serial',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]