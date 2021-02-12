
from django.urls import path
from . import views
from .views import DestinationDetailView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name="index"),
    path('destination/<int:pk>/', DestinationDetailView.as_view(), name='destination_detail'),
    
]