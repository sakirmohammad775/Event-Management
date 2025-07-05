
from django.contrib import admin
from django.urls import path,include
from events.views import home

# this is the main url file for the project where all the url patterns are defined
urlpatterns = [
    path('admin/', admin.site.urls), # admin panel
    path('',home), # home page   
    path('events/',include('events.urls')) # including the url patterns from the events app
]
