# Generated by Django 2.2.6 on 2019-12-20 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab4', '0004_auto_20191220_1524'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topicstarter',
            name='idu',
        ),
        migrations.AddField(
            model_name='topicstarter',
            name='authorization',
            field=models.BooleanField(default=False),
        ),
    ]
