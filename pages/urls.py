from django.urls import path
from .views import index_view, contact_view

urlpatterns = [
    path('', index_view, name="index_view"),
    path('contact/', contact_view, name="index_view"),
]