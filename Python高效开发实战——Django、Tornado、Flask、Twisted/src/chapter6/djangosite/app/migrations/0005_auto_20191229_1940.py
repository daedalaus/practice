# Generated by Django 2.0.7 on 2019-12-29 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='level',
        ),
        migrations.AddField(
            model_name='comment',
            name='body_text',
            field=models.TextField(default='default_body'),
        ),
        migrations.AddField(
            model_name='comment',
            name='headline',
            field=models.CharField(default='default_headline', max_length=255),
        ),
        migrations.AddField(
            model_name='comment',
            name='n_visits',
            field=models.IntegerField(default=99),
        ),
        migrations.AddField(
            model_name='comment',
            name='pub_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='moment',
            name='content',
            field=models.CharField(max_length=300, verbose_name='内容'),
        ),
        migrations.AlterField(
            model_name='moment',
            name='user_name',
            field=models.CharField(default='匿名', max_length=20, verbose_name='username'),
        ),
    ]
