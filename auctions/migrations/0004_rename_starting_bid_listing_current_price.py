# Generated by Django 5.0.1 on 2024-02-04 21:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_listing_creation_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='starting_bid',
            new_name='current_price',
        ),
    ]
