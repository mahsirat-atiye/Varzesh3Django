# Generated by Django 2.1.5 on 2019-01-28 07:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sport', '0015_auto_20190128_1015'),
    ]

    operations = [
        migrations.AddField(
            model_name='basketballimage',
            name='team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sport.BasketballTeam'),
        ),
        migrations.AddField(
            model_name='footballimage',
            name='team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sport.FootballTeam'),
        ),
    ]
