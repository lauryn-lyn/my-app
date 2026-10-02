from django.urls import path
from . import views

urlpatterns = [
    # Homepage URL mapping
    path('', views.service_list, name='service_list'),
]