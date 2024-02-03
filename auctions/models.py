from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Listing(models.Model):
    # title
    # description
    # starting bid
    # image_url
    # category
    title = models.CharField(max_length = 64)
    description = models.TextField()
    starting_bid = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.CharField(max_length=512)
    category = models.CharField(max_length=64)

# class Bid(models.Model):
#     bid_price = models.DecimalField(max_digits=10, decimal_places=2)
#     # the bid should be related to a specific listing
#     # specifically, should have details for the listing you're bidding on 

# class Comment(models.Model):
#     comment = models.TextField()