# Generated by Django 5.0.4 on 2024-04-25 07:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Sellbook', '0005_profile_membership_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='membership_status',
        ),
    ]
