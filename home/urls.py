from django.urls import path
from home import views

urlpatterns = [
    path('',views.index,name = 'home'),
    path('about',views.about,name = 'about'),
    path('contact',views.contact,name = 'contact'),
    path('register',views.register,name = 'register'),
    path('login',views.login,name = 'login'),
    path('logout',views.logout,name='logout'),
    path('cart',views.cart,name='cart'),
    path('shop',views.shop,name = 'shop')
]