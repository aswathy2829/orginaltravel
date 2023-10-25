from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name="index"),
    path('about', views.elements, name="elements"),
    path('about', views.destinations, name="destinations"),
    path('about', views.contact, name="contact"),
    path('about', views.news, name="news"),

]


