import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

from .models import ServiceRequest


@csrf_exempt
def service_list(request):

    # GET — load all listings
    if request.method == "GET":
        services = ServiceRequest.objects.all().order_by("-created_at")

        data = []

        for service in services:
            data.append({
                "id": service.id,
                "title": service.title,
                "description": service.description,
                "category": service.category,
                "barter_target": service.barter_target,
                "created_at": service.created_at.isoformat(),
                "username": service.user.username,
            })

        return JsonResponse(data, safe=False)

    # POST — create a new listing
    if request.method == "POST":
       try:
            data = json.loads(request.body)
 
            username = data.get("username", "Guest")
user, created = User.objects.get_or_create(username=username)

     if user is None:
                return JsonResponse(
                    {"error": "No user exists in the database."},
                    status=400
                )

            service = ServiceRequest.objects.create(
                user=user,
                title=data.get("title", ""),
                description=data.get("description", ""),
                category=data.get("category", "OFFER"),
                barter_target=data.get("barter_target", "")
            )

            return JsonResponse({
                "id": service.id,
                "title": service.title,
                "description": service.description,
                "category": service.category,
                "barter_target": service.barter_target,
                "username": service.user.username,
            }, status=201)  
         except Exception as error:                                                                                                                                                                                                                                              
            return JsonResponse(
                {"error": str(error)},
                status=400
            )

            return JsonResponse({"error": "Method not allowed"}, status=405)