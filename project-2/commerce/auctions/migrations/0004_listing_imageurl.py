# Generated by Django 5.0.6 on 2024-05-29 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_remove_listing_imageurl'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='imageUrl',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]