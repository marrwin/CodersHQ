# Generated by Django 3.0.11 on 2021-08-05 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210805_0856'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserScoreCategories',
            new_name='UserScoreCategory',
        ),
    ]
