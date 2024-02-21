from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime


class User(AbstractUser):
    # lazy initialization for Listing since normally should be run top to bottom
    listings = models.ManyToManyField('Listing', blank=True, related_name='watchlist')

class Listing(models.Model):
    current_time = datetime.now()
    title = models.CharField(max_length = 64)
    description = models.TextField()
    current_price = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.CharField(max_length=512)
    category = models.CharField(max_length=64)
    creation_time = models.DateTimeField(auto_now_add=True)
    associated_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='listing_creator')
    is_active = models.BooleanField(default=True)

class Bid(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2)
    bid_placer = models.ForeignKey(User, on_delete=models.CASCADE)
    associated_listing = models.ForeignKey(Listing, on_delete=models.CASCADE)

class Comment(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
