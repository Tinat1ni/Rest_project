# Generated by Django 5.1.3 on 2024-11-17 12:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Menu',
            new_name='MainMenuCategory',
        ),
    ]
