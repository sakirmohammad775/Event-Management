from django.urls import path
from events.views import manager

urlpatterns = [
    path('manager/',manager)
]
 