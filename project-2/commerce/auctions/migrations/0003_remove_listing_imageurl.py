# Generated by Django 5.0.6 on 2024-05-29 08:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_listing'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='imageUrl',
        ),
    ]