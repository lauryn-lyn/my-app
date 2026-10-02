from django.contrib import admin
from django.urls import path
from trades.views import service_requests_api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/service-requests/', service_requests_api),
]
