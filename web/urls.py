from django.urls import path
from . import views

app_name = 'web'

urlpatterns = [
    path('', views.index,name="index"),
    path('index-2/', views.index,name="index_2"),
    path('about/', views.about,name="about"),
    path('blog/', views.blog,name="blog"),
    path('blog-right/', views.blogright,name="blogright"),
    path('blog-left/', views.blogleft,name="blogleft"),
    path('checkout/', views.checkout,name="checkout"),
    path('contact/', views.contact,name="contact"),
    path('wishlist/', views.wishlist,name="wishlist"),
    path('news/', views.news,name="news"),
    path('shop-left/', views.shopleft,name="shopleft"),
    path('shop-detalis/', views.shopdetalis,name="shopdetalis"),
    path('shop-detalis-left/', views.shopdetalisleft,name="shopdetalisleft"),
    path('shop-detalis-right/', views.shopdetalisright,name="shopdetalisright"),
    path('shopping-cart/', views.shoppingcart,name="shoppingcart"),
    path('shopgrid-left/', views.shopgridleft,name="shopgridleft"),
    path('shopgrid-right/', views.shopgridright,name="shopgridright"),
    path('shopgrid/', views.shopgrid,name="shopgrid"),
    path('shoplist/', views.shoplist,name="shoplist"),
    path('shoplist-right/', views.shoplistright,name="shoplistright"),
    path('shoplist-left/', views.shoplistleft,name="shoplistleft"),
    path('404/', views.error,name="error"),
]