"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from home.views import *
from vege.views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from Invent.views import*

urlpatterns = [
    #  path('', , name="home"),
     path('receipe/' , receipe , name="receipe"),
     path('room/',room,name="room"),
     path('delete_btn/<id>/',deletebtn,name="deletebtn"),
     path('updatebtn/<id>/',updatebtn,name="updatebtn"),
     path('login/',log_in,name="log_in"),
     path('logout/',log_out,name="log_out"),
     path('register/',register,name="register"),
     path('contact/',contact,name="contact"),
     path('about/',about,name="about"),
     path('admin/', admin.site.urls),
    #  path('sellerReg/',sellerReg,name="sellerReg"),
    #  path('customerReg/',customerReg,name="customerReg"),
     path('Category/',Category,name="Category"),
     path('category_list/',category_list,name="category_list"),
     path('delete_bt/<id>/',deletebt,name="deletebt"),
     path('updatebt/<id>/',updatebt,name="updatebt"),
     path('',home,name="home"),
     path('room/',room,name="room"),
     path('room_list/',room_list,name="room_list"),
     path('delete_room/<id>/',delete_room,name="delete_room"),
     path('update_room/<id>/',update_room,name="update_room"),
     path('product/',product,name="product"),
     path('base_side/',base_side,name="base_side"),
     path('Product_list/',Product_list,name="Product_list"),
     path('delete_product/<id>/',delete_product,name="delete_product"),
     path('update_product/<id>/',update_product,name="update_product"),

     path('Dashboard/',Dashboard,name="Dashboard"),
     path('message/',message,name="message"),
    path('', include('REST_API.urls')),  # Include the new app URLs

    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns += staticfiles_urlpatterns()

