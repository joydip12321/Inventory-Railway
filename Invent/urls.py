from django.urls import path
from Invent import views

urlpatterns=[
     path('Category/',views.Category,name="Category"),
     path('category_list/',views.category_list,name="category_list"),
     path('delete_bt/<id>/',views.deletebt,name="deletebt"),
     path('updatebt/<id>/',views.updatebt,name="updatebt"),
     path('',views.home,name="home"),
     path('room/',views.room,name="room"),
     path('room_list/',views.room_list,name="room_list"),
     path('delete_room/<id>/',views.delete_room,name="delete_room"),
     path('update_room/<id>/',views.update_room,name="update_room"),
     path('product/',views.product,name="product"),
     path('base_side/',views.base_side,name="base_side"),
     path('Product_list/',views.Product_list,name="Product_list"),
     path('delete_product/<id>/',views.delete_product,name="delete_product"),
     path('update_product/<id>/',views.update_product,name="update_product"),
     path('Dashboard/',views.Dashboard,name="Dashboard"),
     path('message/',views.message,name="message"),
     path('log_in/',views.Log_in,name="log_in"),
     path('register_in/',views.Register_invent,name="register"),
     path('log_out/',views.Log_out,name="log_out"),
     path('admin_log_in/',views.Admin_log_in,name="admin_log_in")


]