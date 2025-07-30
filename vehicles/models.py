from django.db import models
from accounts.models import User


# CarType Model
class CarType(models.Model):
    name = models.CharField(max_length=100, db_index=True) # SUV, Sedan, Hatchback, etc.
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.name  

# Vehicle Model
class Vehicle(models.Model):
    car_type = models.ForeignKey(CarType, on_delete=models.CASCADE)
    make = models.CharField(max_length=100, db_index=True)
    model = models.CharField(max_length=100, db_index=True)
    year = models.PositiveIntegerField(db_index=True)
    color = models.CharField(max_length=100)
    registration_number = models.CharField(max_length=15, unique=True, db_index=True)
    seats = models.PositiveIntegerField()
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2, db_index=True)
    available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='vehicles/', null=True, blank=True)
    
    def __str__(self):
        return f"{self.make} {self.model} ({self.year})"
     
    
    
# Car review Model
class CarReview(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveIntegerField(choices=[(i, str(i)) for i in range(1, 6)]) # rating between 1 and 5 stars
    comment = models.TextField(blank=True, null=True)
    
    
    def __str__(self):
        return f"Review for {self.vehicle} by {self.user} - {self.rating} star(s)"
