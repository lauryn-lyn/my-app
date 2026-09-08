from django.db import models
from django.contrib.auth.models import User

# Extended User Profile
class UserProfile(models.Model):
    # Links profile directly to Django's built-in User system
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    
    # Profile picture field
    profile_picture = models.ImageField(upload_to='profile_pics/', default='default_avatar.png')
    
    # Short summary for browsing
    skill_summary = models.CharField(max_length=255, help_text="Short 1-line summary of what you can do")
    
    # Detailed bio text
    full_bio = models.TextField(blank=True, null=True)

    def __str__(self):
        # Python requires this return statement to be indented by 4 spaces
        return f"{self.user.username}s Profile"
    # 2. Service Requests (Offers & Requests for Trades)
class ServiceRequest(models.Model):
    # Defines whether the user is offering a service or requesting one
    CATEGORY_CHOICES = [
        ('OFFER', 'Offering a Service'),
        ('REQUEST', 'Requesting a Service'),
    ]

    # Links the post to the user who created it
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='service_requests')
    
    # Title of the skill/service (e.g., "Web Design", "Guitar Lessons")
    title = models.CharField(max_length=200)
    
    # Full description of what is offered or needed
    description = models.TextField()
    
    # Category dropdown selection
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default='OFFER')
    
    # Skill or item desired in return
    barter_target = models.CharField(max_length=200, help_text="What skill or service do you want in exchange?")
    
    # Automatic timestamp when created
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_category_display()}: {self.title} by {self.user.username}"


    # 3. Trade Offers (Proposals sent between users)
class TradeOffer(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('ACCEPTED', 'Accepted'),
        ('REJECTED', 'Rejected'),
    ]

    # Links to the specific service post being offered on
    service_request = models.ForeignKey(ServiceRequest, on_delete=models.CASCADE, related_name='offers')
    
    # User who is sending the trade offer
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_offers')
    
    # Proposed skill/service description offered in exchange
    proposed_exchange = models.TextField(help_text="Describe what you offer in return")
    
    # Current status of the barter proposal
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')
    
    # Timestamp when the offer was submitted
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Offer by {self.sender.username} on '{self.service_request.title}' [{self.status}]"
