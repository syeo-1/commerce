from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path('listings/<int:listing_id>/add_to_watchlist', views.add_to_watchlist, name='add_to_watchlist'),
    path('listings/<int:listing_id>/remove_from_watchlist', views.remove_from_watchlist, name='remove_from_watchlist'),
    path("listings/<int:listing_id>", views.listing, name='listing'),
    path('create_listing', views.create_listing, name='create_listing'),
    path('watchlist', views.watchlist, name='watchlist')
]
