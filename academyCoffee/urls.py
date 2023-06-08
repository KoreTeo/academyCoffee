from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('cart/', views.cart, name='cart'),
    path('menu/', views.menu, name='menu'),
    path('account/', views.personalaccount, name='personalaccount'),
    path('stocks/', views.stocks, name='stocks'),
    path('about/', views.about, name='about'),
    path('history/', views.orderhistory, name='orderhistory'),
]
