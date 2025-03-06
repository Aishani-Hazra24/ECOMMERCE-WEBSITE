from django.urls import path
from . import views

urlpatterns = [
    
    # path('register/', views.register, name='register'),
    path('', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('home/', views.home, name='home'),  # Home page after login
    path('cart/', views.cart, name='cart'),
] 
