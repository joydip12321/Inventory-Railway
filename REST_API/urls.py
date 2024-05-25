from django.urls import path
from REST_API import views

urlpatterns=[
    path("weather/",views.index)
]