# Generated by Django 5.0.3 on 2024-06-27 03:19

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_question_liked'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='liked',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='answer',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='liked_answers', to=settings.AUTH_USER_MODEL),
        ),
    ]