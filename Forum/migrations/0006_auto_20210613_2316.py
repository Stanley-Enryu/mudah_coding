# Generated by Django 3.2.4 on 2021-06-13 16:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Forum', '0005_auto_20210613_2314'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postreply',
            old_name='body',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='postreply',
            old_name='timestamp',
            new_name='time_created',
        ),
    ]