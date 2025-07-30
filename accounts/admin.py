from django.contrib import admin
from .models import User, UserProfile

# User admin registration
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_active')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)
    
    
# UserProfile admin registration
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'address', 'profile_picture')
    search_fields = ('user__email', 'address')
    ordering = ('user__email',)    
