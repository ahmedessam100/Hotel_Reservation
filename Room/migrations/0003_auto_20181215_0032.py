# Generated by Django 2.1.4 on 2018-12-14 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Room', '0002_auto_20181214_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='number',
            field=models.IntegerField(default=0, unique=True),
        ),
    ]
