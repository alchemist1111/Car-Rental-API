from django.models.signals import post_save
from django.dispatch import receiver
from .models import User, UserProfile

# Signal to create a UserProfile when a new User is created
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        # Create a UserProfile when a new User is created
        UserProfile.objects.create(user=instance)
        
        
# Signal to save the UserProfile when the User is saved
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    # Save the associated UserProfile when the User is saved
    instance.profile.save()        