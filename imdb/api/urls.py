from django.urls import path,include
from django.conf.urls import url
from rest_framework.authtoken import views
from .views import home,SearchView
from rest_framework import routers





urlpatterns = [
    path('',home,name='api.movies'),
    path('search',SearchView.as_view(),name='api.search')
    
    
    
    
    
]