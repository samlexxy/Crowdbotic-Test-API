# Generated by Django 3.2.8 on 2021-10-18 11:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20211018_1017'),
    ]

    operations = [
        migrations.RenameField(
            model_name='app',
            old_name='screenshoot',
            new_name='screenshot',
        ),
    ]
