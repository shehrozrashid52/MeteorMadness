from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta
from dashboard.models import Asteroid, CloseApproach

class Command(BaseCommand):
    help = 'Populate database with sample asteroid data'

    def handle(self, *args, **options):
        # Clear existing data
        Asteroid.objects.all().delete()
        
        # Sample asteroid data
        sample_asteroids = [
            {
                'neo_id': '2021001',
                'name': 'Apophis',
                'diameter_min': 0.325,
                'diameter_max': 0.375,
                'is_potentially_hazardous': True,
                'absolute_magnitude': 19.7
            },
            {
                'neo_id': '2021002', 
                'name': 'Bennu',
                'diameter_min': 0.492,
                'diameter_max': 0.565,
                'is_potentially_hazardous': True,
                'absolute_magnitude': 20.9
            },
            {
                'neo_id': '2021003',
                'name': 'Ryugu',
                'diameter_min': 0.865,
                'diameter_max': 0.915,
                'is_potentially_hazardous': False,
                'absolute_magnitude': 19.2
            },
            {
                'neo_id': '2021004',
                'name': 'Itokawa',
                'diameter_min': 0.318,
                'diameter_max': 0.535,
                'is_potentially_hazardous': False,
                'absolute_magnitude': 19.4
            },
            {
                'neo_id': '2021005',
                'name': 'Eros',
                'diameter_min': 16.84,
                'diameter_max': 16.84,
                'is_potentially_hazardous': False,
                'absolute_magnitude': 10.4
            }
        ]
        
        for asteroid_data in sample_asteroids:
            asteroid = Asteroid.objects.create(**asteroid_data)
            
            # Create sample close approaches
            for i in range(3):
                approach_date = timezone.now() + timedelta(days=30 + i*60)
                CloseApproach.objects.create(
                    asteroid=asteroid,
                    approach_date=approach_date,
                    velocity_kmh=50000 + i*10000,
                    velocity_kms=15 + i*5,
                    miss_distance_km=5000000 + i*2000000,
                    miss_distance_au=0.033 + i*0.013,
                    orbiting_body='Earth'
                )
        
        self.stdout.write(
            self.style.SUCCESS(f'Successfully created {len(sample_asteroids)} asteroids with close approaches')
        )