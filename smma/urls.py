from django.urls import path
from .views import *

urlpatterns = [
    path('', smma, name="smma"),
     path('services/', services, name="services")
]