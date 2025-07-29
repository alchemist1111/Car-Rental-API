from django.db import models
from django.contrib.auth.models import AbstractUser

# User model inheriting from AbstractUser
class User(AbstractUser):
    # Additional fields
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    
    # Sensitive information optional using signup
    license_number = models.CharField(max_length=50, null=True, blank=True)
    license_issue_date = models.DateField(null=True, blank=True)
    licanse_expiry_date = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return f"Name: {self.first_name} {self.last_name}"
    

# UserProfile model to extend user information
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    address = models.CharField(max_length=255, null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    
    def __str__(self):
        return f"Profile of {self.user.first_name} {self.user.last_name}"
