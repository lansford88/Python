# Generated by Django 3.1.1 on 2020-09-20 23:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='djangoclasses',
            name='Course_Number',
        ),
    ]
