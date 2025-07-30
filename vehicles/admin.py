from django.contrib import admin
from .models import Vehicle, CarType, CarReview

# Vehicle model registration
@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ( 'car_type', 'make', 'model', 'year', 'registration_number', 'available', 'price_per_day')
    search_fields = ('make', 'model', 'registration_number')
    list_filter = ('available', 'year', 'car_type')
    ordering = ('-year',)
    
    
# CarType model registration
@admin.register(CarType)
class CarTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
    ordering = ('name',)
    
    
# CarReview model registration
@admin.register(CarReview)
class CarReviewAdmin(admin.ModelAdmin):
    list_display = ('vehicle', 'user', 'rating', 'comment')
    search_fields = ('vehicle__make', 'comment')
    list_filter = ('rating',)
    ordering = ('-rating',)        



