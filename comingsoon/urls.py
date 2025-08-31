from django.urls import path
from .views import coming_soon_view

urlpatterns = [
    path('', coming_soon_view, name='coming_soon'),
]