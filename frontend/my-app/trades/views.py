from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import ServiceRequest

def service_list(request):
    # Fetch all active service requests from the database, newest first
    services = ServiceRequest.objects.all().order_by('-created_at')
    
    # Render the template and pass the data context
    return render(request, 'trades/service_list.html', {'services': services})