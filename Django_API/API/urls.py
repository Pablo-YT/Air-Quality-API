from django.contrib import admin
from django.urls import path,include
from API import views

urlpatterns = [
    path("",views.API, name='api'),
    path("api/",views.API, name="api"),
    path("about/",views.about, name="about"),
    path("world_api/", views.world_api, name='world_api')
]