# Generated by Django 2.1.5 on 2019-01-24 16:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sport', '0006_auto_20190124_1710'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='footballgame',
            name='teams',
        ),
    ]