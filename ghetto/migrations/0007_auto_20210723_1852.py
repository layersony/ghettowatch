# Generated by Django 2.1 on 2021-07-23 15:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ghetto', '0006_auto_20210723_1844'),
    ]

    operations = [
        migrations.RenameField(
            model_name='business',
            old_name='Neighborhood',
            new_name='neighborhood',
        ),
    ]
