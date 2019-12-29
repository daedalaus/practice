# Generated by Django 2.0.7 on 2019-12-29 13:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20191229_1940'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=80)),
                ('password', models.CharField(max_length=255)),
                ('reg_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='app.Account')),
                ('zip_code', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=80)),
                ('mobile', models.CharField(max_length=20)),
            ],
        ),
    ]
