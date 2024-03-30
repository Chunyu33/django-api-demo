from django.urls import path

from app_user.views import register, login

# 命名空间
app_name = 'user'

urlpatterns = [
    path('register', register),
    path('login', login)
]
