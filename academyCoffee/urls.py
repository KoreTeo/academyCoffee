from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('cart/', views.cart, name='cart'),
    path('menu/', views.menu, name='menu'),
    path('account/', views.profile, name='profile'),
    path('account2/', views.profile2, name='profile2'),
    path('stocks/', views.stocks, name='stocks'),
    path('registration/', views.registration, name='registration'),
    path('login/', views.login, name='login'),
    path('about/', views.about, name='about'),
    path('history/', views.orderhistory, name='orderhistory'),
    path('logout/', views.logout, name='logout'),
    path('baskets/add/<int:product_id>/', views.basket_add, name='basket_add'),
    path('baskets/remove/<int:basket_id>/', views.basket_remove, name='basket_remove'),
    path('baskets/deletion/<int:product_id>/', views.basket_deletion, name='basket_deletion'),
]
