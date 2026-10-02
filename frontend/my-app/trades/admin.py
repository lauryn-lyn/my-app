from django.contrib import admin

# Register your models here.
from django.contrib import admin  # Import Django's admin framework
from .models import UserProfile, ServiceRequest, TradeOffer  # Import our database models

# 1. Customize how UserProfile appears in Admin
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    # Columns shown in the admin table view
    list_display = ('user', 'skill_summary')
    # Search bar fields
    search_fields = ('user__username', 'skill_summary')


# 2. Customize how ServiceRequest appears in Admin
@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):
    # Columns shown in the admin table view
    list_display = ('title', 'user', 'category', 'created_at')
    # Right-side filter panel options
    list_filter = ('category', 'created_at')
    # Search bar fields
    search_fields = ('title', 'description', 'user__username')


# 3. Customize how TradeOffer appears in Admin
@admin.register(TradeOffer)
class TradeOfferAdmin(admin.ModelAdmin):
    # Columns shown in the admin table view
    list_display = ('service_request', 'sender', 'status', 'created_at')
    # Right-side filter panel options
    list_filter = ('status', 'created_at')
    # Search bar fields
    search_fields = ('sender__username', 'proposed_exchange')