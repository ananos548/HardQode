# Generated by Django 4.2.5 on 2023-09-22 18:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0003_alter_product_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='LessonAccess',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('view_time_seconds', models.IntegerField(default=0)),
                ('is_completed', models.BooleanField(default=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='is_viewed',
        ),
        migrations.DeleteModel(
            name='ProductAccess',
        ),
        migrations.AddField(
            model_name='lessonaccess',
            name='lesson',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.lesson'),
        ),
        migrations.AddField(
            model_name='lessonaccess',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
