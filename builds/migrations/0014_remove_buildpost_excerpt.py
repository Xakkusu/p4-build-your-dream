# Generated by Django 4.2.17 on 2025-01-26 19:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('builds', '0013_alter_buildpost_money_spent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buildpost',
            name='excerpt',
        ),
    ]
