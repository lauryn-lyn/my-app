from django.urls import path
from . import views

urlpatterns = [
    path('api/services/', views.service_list, name='service_list'),
]