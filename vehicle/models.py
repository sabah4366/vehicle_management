from django.db import models


class Vehicle(models.Model):
    options= [
        ('Two wheeler', 'Two Wheeler'),
        ('Three wheeler', 'Three Wheeler'),
        ('Four wheeler', 'Four Wheeler'),
    ]
    
    vehicle_number = models.CharField(max_length=50)
    vehicle_type = models.CharField(max_length=100, choices=options)
    vehicle_model = models.CharField(max_length=100)
    vehicle_description = models.TextField()
    
    def __str__(self):
        return self.vehicle_number
    
    def save(self, *args, **kwargs):
        
        super(Vehicle, self).save(*args, **kwargs)

