# Generated by Django 3.2.4 on 2021-06-11 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Browse_Course', '0005_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='sub_step_course',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]
