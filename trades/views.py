from django.shortcuts import render
from django.http import JsonResponse
from .models import ServiceRequest


def service_list(request):
    services = ServiceRequest.objects.all().order_by('-created_at')

    return render(
        request,
        'trades/service_list.html',
        {'services': services}
    )


def service_requests_api(request):
    services = ServiceRequest.objects.all().order_by('-created_at')

    data = []

    for service in services:
        data.append({
            'id': service.id,
            'title': service.title,
            'description': service.description,
            'category': service.category,
            'barter_target': service.barter_target,
            'username': service.user.username,
        })

    return JsonResponse(data, safe=False)
