# Generated by Django 5.0.6 on 2024-06-28 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0008_alter_message_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='timestamp',
            field=models.TimeField(auto_now_add=True, null=True),
        ),
    ]
