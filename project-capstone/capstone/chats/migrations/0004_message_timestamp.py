# Generated by Django 5.0.6 on 2024-06-27 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0003_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
