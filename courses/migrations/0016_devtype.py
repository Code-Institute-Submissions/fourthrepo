# Generated by Django 2.2.6 on 2020-08-16 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0015_course_dev_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Devtype',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
    ]