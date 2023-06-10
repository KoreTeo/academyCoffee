from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('cart/', views.cart, name='cart'),
    path('menu/', views.menu, name='menu'),
    path('account/', views.profile, name='profile'),
    path('stocks/', views.stocks, name='stocks'),
    path('registration/', views.registration, name='registration'),
    path('about/', views.about, name='about'),
    path('history/', views.orderhistory, name='orderhistory'),
    path('logout/', views.logout, name='logout'),
    path('login/', views.login, name='login'),
    path('baskets/add/<int:product_id>/', views.basket_add, name='basket_add'),
    path('baskets/deletion/<int:product_id>/', views.basket_deletion, name='basket_deletion'),
]
