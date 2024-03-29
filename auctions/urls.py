from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('categories', views.categories, name='categories'),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path('listings/<int:listing_id>/close_listing', views.close_listing, name='close_listing'),
    path('listings/<int:listing_id>/add_comment', views.add_comment, name='add_comment'),
    path('listings/<int:listing_id>/add_to_watchlist', views.add_to_watchlist, name='add_to_watchlist'),
    path('listings/<int:listing_id>/remove_from_watchlist', views.remove_from_watchlist, name='remove_from_watchlist'),
    path('listings/<int:listing_id>/bid', views.bid, name='bid'),
    path("listings/<int:listing_id>", views.listing, name='listing'),
    path('create_listing', views.create_listing, name='create_listing'),
    path('watchlist', views.watchlist, name='watchlist'),
    path('<str:category>', views.display_category, name='display_category')
]
