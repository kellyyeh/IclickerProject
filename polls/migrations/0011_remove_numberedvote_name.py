# Generated by Django 2.1.2 on 2018-10-29 22:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0010_auto_20181029_0628'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='numberedvote',
            name='name',
        ),
    ]