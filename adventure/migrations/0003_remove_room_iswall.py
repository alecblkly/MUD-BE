# Generated by Django 3.0.3 on 2020-03-05 03:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adventure', '0002_auto_20200303_1635'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='isWall',
        ),
    ]