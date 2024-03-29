# Generated by Django 4.1.7 on 2023-02-26 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appname', models.CharField(max_length=50)),
                ('logo', models.ImageField(upload_to='logo')),
                ('carousel1', models.ImageField(upload_to='carousel1')),
                ('carousel2', models.ImageField(upload_to='carousel2')),
                ('carousel3', models.ImageField(upload_to='carousel3')),
                ('banner', models.ImageField(upload_to='banner')),
                ('copyright', models.IntegerField()),
            ],
        ),
    ]
