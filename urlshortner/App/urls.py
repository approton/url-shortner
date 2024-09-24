from django.urls import path
from .views import shorten_url, redirect_to_long_url, index

urlpatterns = [
    path('', index, name='index'),  # Main page
    path('api/shorten/', shorten_url, name='shorten_url'),
    path('<str:short_url>/', redirect_to_long_url, name='redirect_url'),
]
