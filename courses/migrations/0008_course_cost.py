# Generated by Django 2.2.6 on 2020-08-14 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_auto_20200813_0307'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='cost',
            field=models.DecimalField(decimal_places=2, default=10, max_digits=10),
            preserve_default=False,
        ),
    ]