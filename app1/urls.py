from django.urls import path
from .views import *

urlpatterns = [
    path('api/Login/',LoginView.as_view(), name='login'),
    # Add other app-specific URLs here
]