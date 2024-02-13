from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # This defines the root URL pattern
    # Other URL patterns go here
]
