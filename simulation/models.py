from django.db import models
from django.utils import timezone

class SimulationResult(models.Model):
    diameter = models.FloatField()
    velocity = models.FloatField()
    density = models.FloatField()
    impact_angle = models.FloatField()
    impact_location = models.CharField(max_length=20)
    impact_energy = models.FloatField()
    tnt_equivalent = models.FloatField()
    crater_diameter = models.FloatField()
    seismic_magnitude = models.FloatField()
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"Simulation {self.id} - {self.tnt_equivalent:.2f} MT"
