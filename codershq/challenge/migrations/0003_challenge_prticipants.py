# Generated by Django 3.0.11 on 2021-08-20 13:19

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('challenge', '0002_auto_20210812_0923'),
    ]

    operations = [
        migrations.AddField(
            model_name='challenge',
            name='prticipants',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
