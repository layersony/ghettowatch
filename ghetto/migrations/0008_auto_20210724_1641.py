# Generated by Django 2.1 on 2021-07-24 13:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ghetto', '0007_auto_20210723_1852'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='business',
            name='info',
        ),
        migrations.AddField(
            model_name='postii',
            name='timeuploaded',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='business',
            name='category',
            field=models.ManyToManyField(blank=True, null=True, to='ghetto.Category'),
        ),
    ]
