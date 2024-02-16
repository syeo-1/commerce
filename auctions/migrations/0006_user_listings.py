# Generated by Django 5.0.1 on 2024-02-15 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_listing_associated_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='listings',
            field=models.ManyToManyField(blank=True, related_name='watchlist', to='auctions.listing'),
        ),
    ]
