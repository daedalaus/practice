# Generated by Django 2.0.7 on 2019-12-29 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20191229_2154'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='account',
        ),
        migrations.AddField(
            model_name='contact',
            name='accounts',
            field=models.ManyToManyField(to='app.Account'),
        ),
    ]
