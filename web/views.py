from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context = {
        "is_index" : True
    }
    return render(request, 'web/index.html',context)

  
def about(request):
    context = {
        "is_about" : True
    }
    return render(request, 'web/about_us.html',context)

def index_2(request):
    context = {
        "is_index_2" : True
    }
    return render(request, 'web/index_2.html',context)
    

def blog(request):
    context = {
        "is_blog" : True
    }
    return render(request, 'web/blog.html',context)

def blogright(request):
    context = {
        "is_blogright" : True
    }
    return render(request, 'web/blog_right_sidebar.html',context)

def blogleft(request):
    context = {
        "is_blogleft" : True
    }
    return render(request, 'web/blog-left_sidebar.html',context)

def checkout(request):
    context = {
        "is_checkout" : True
    }
    return render(request, 'web/checkout_page.html',context)

def contact(request):
    context = {
        "is_contact" : True
    }
    return render(request, 'web/contact_page.html',context)

def wishlist(request):
    context = {
        "is_wishlist" : True
    }
    return render(request, 'web/my_wishlist.html',context)

def news(request):
    context = {
        "is_news" : True
    }
    return render(request, 'web/news_detalis.html',context)

def shopleft(request):
    context = {
        "is_shopleft" : True
    }
    return render(request, 'web/shop_detalis_left_sidebar.html',context)

def shopright(request):
    context = {
        "is_shopright" : True
    }
    return render(request, 'web/shop_detalis_right_sidebar.html',context)

def shopdetalis(request):
    context = {
        "is_shopdetalis" : True
    }
    return render(request, 'web/shop_detalis.html',context)

def shopdetalisleft(request):
    context = {
        "is_shopdetalisleft" : True
    }
    return render(request, 'web/shop_detalis_left_sidebar.html',context)

def shopdetalisright(request):
    context = {
        "is_shopdetalisright" : True
    }
    return render(request, 'web/shop_detalis_right_sidebar.html',context)

def shopgridleft(request):
    context = {
        "is_shopgridleft" : True
    }
    return render(request, 'web/shop_grid_left_sidebar.html',context)

def shopgridright(request):
    context = {
        "is_shopgridright" : True
    }
    return render(request, 'web/shop_grid_right_sidebar.html',context)    

def shopgrid(request):
    context = {
        "is_shopgrid" : True
    }
    return render(request, 'web/shop_grid.html',context)

def error(request):
    context = {
        "is_error" : True
    }
    return render(request, 'web/404.html',context)

def shoplist(request):
    context = {
        "is_shoplist" : True
    }
    return render(request, 'web/shop_list.html',context)

def shoplistright(request):
    context = {
        "is_shoplistright" : True
    }
    return render(request, 'web/shop_list_right_sidebar.html',context)

def shoplistleft(request):
    context = {
        "is_shoplistleft" : True
    }
    return render(request, 'web/shop_list_left_sidebar.html',context)    
   
def shoppingcart(request):
    context = {
        "is_shoppingcart" : True
    }
    return render(request, 'web/shopping_cart.html',context)    
   
