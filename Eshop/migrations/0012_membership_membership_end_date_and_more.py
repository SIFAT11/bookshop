# Generated by Django 5.0.4 on 2024-04-25 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Eshop', '0011_alter_membership_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='membership',
            name='membership_end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='membership',
            name='membership_start_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
