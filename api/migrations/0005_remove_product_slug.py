# Generated by Django 4.2.5 on 2023-09-22 19:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_lessonaccess_remove_lesson_is_viewed_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='slug',
        ),
    ]
