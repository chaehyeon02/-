from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('home/', views.home, name='home'),
    path('lotto/', views.lotto_index, name='lotto_index'),
    path('lotto/result/', views.lotto_result, name='lotto_result'),
]