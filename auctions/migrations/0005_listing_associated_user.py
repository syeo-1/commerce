# Generated by Django 5.0.1 on 2024-02-15 22:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_rename_starting_bid_listing_current_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='associated_user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='listing_creator', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]