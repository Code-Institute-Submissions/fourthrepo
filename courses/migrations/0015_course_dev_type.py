# Generated by Django 2.2.6 on 2020-08-16 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0014_delete_devtype'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='dev_type',
            field=models.CharField(default='frontend', max_length=100),
            preserve_default=False,
        ),
    ]