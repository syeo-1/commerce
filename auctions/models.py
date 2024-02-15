from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime


class User(AbstractUser):
    listings = models.ManyToManyField('Listing', blank=True, related_name='watchlist')

class Listing(models.Model):
    # title
    # description
    # starting bid
    # image_url
    # category
    current_time = datetime.now()
    title = models.CharField(max_length = 64)
    description = models.TextField()
    current_price = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.CharField(max_length=512)
    category = models.CharField(max_length=64)
    creation_time = models.DateTimeField(auto_now_add=True)
    associated_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='listing_creator')


# class Bid(models.Model):
#     bid_price = models.DecimalField(max_digits=10, decimal_places=2)
#     # the bid should be related to a specific listing
#     # specifically, should have details for the listing you're bidding on 

# class Comment(models.Model):
#     comment = models.TextField()