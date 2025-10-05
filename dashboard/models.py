from django.db import models
from django.utils import timezone

class Asteroid(models.Model):
    neo_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=200)
    diameter_min = models.FloatField(null=True, blank=True)
    diameter_max = models.FloatField(null=True, blank=True)
    is_potentially_hazardous = models.BooleanField(default=False)
    absolute_magnitude = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.name

class CloseApproach(models.Model):
    asteroid = models.ForeignKey(Asteroid, on_delete=models.CASCADE, related_name='close_approaches')
    approach_date = models.DateTimeField()
    velocity_kmh = models.FloatField()
    velocity_kms = models.FloatField()
    miss_distance_km = models.FloatField()
    miss_distance_au = models.FloatField()
    orbiting_body = models.CharField(max_length=50, default='Earth')
    
    class Meta:
        ordering = ['approach_date']
    
    def __str__(self):
        return f"{self.asteroid.name} - {self.approach_date.date()}"

