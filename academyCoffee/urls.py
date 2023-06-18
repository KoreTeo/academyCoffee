from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('cart/', views.OrderCreateView.as_view(), name='cart'),
    path('menu/', views.menu, name='menu'),
    path('account/<int:pk>/', login_required(views.UserProfileView.as_view()), name='profile'),
    path('stocks/', views.stocks, name='stocks'),
    path('registration/', views.UserRegistrationView.as_view(), name='registration'),
    path('about/', views.about, name='about'),
    path('addcart/', views.CreateUserCardView.as_view(), name='addcart'),
    path('current/', views.currentorder, name='currentorder'),
    path('history/', views.OrderListView.as_view(), name='orderhistory'),
    path('currentorder/', views.currentorder, name='currentorder'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('baskets/add/<int:product_id>/', views.basket_add, name='basket_add'),
    path('baskets/deletion/<int:product_id>/', views.basket_deletion, name='basket_deletion'),
    path('card/makebase/<int:card_id>/', views.make_base_card, name='make_base_card'),
    path('cart/success', views.SuccessTemplateView.as_view(), name='order_success'),
    path('cart/caceled/', views.CanceledTemplateView.as_view(), name='order_canceled'),
    path('profile/makecashpayment', views.make_cash_payment, name='make_cash_payment'),
]
