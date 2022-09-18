from django.urls import path
from shop.views import *
app_name = 'shop'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about', AboutView.as_view(), name = 'about'),
    path('contact', ContactView.as_view(), name = 'contact'),
    path('signup', signup, name = 'signup'),
    path('login', login, name = 'login'),
    path('logout', logout, name = 'logout'),
    path('shop/<slug>', ShopView.as_view(), name='shop'),
    path('item_detail/<slug>', ItemDetailView.as_view(), name='item_detail'),
    path('search', ItemSearchView.as_view(), name='search'),
]
