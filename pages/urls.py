from django.urls import path
from .views import index_view, error_404

urlpatterns = [
    path('', index_view, name="index_view"),
    path('contact/', error_404, name="error_404"),
]