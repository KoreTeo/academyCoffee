from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('cart/', views.cart, name='cart'),
    path('menu/', views.menu, name='menu'),
    path('account/<int:pk>/', login_required(views.UserProfileView.as_view()), name='profile'),
    path('stocks/', views.stocks, name='stocks'),
    path('registration/', views.UserRegistrationView.as_view(), name='registration'),
    path('about/', views.about, name='about'),
    path('history/', views.orderhistory, name='orderhistory'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('baskets/add/<int:product_id>/', views.basket_add, name='basket_add'),
    path('baskets/deletion/<int:product_id>/', views.basket_deletion, name='basket_deletion'),
]
