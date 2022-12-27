from django.urls import path
from app2.views import *
app_name = 'kingstone'

urlpatterns = [
    path('banglore/', banglore, name='banglore'),
    path('tuesday/', tuesday, name='tuesday'),
]


