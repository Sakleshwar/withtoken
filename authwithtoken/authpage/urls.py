from django.urls import path
from .views import *

urlpatterns = [
    path('users/create/', UserCreateView.as_view(), name='user_create'),
    path('users/login/', UserLoginView.as_view(), name='user_login'),
]

