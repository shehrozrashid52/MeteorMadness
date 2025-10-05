from django.shortcuts import render, get_object_or_404
from dashboard.models import Asteroid

def visualizer(request):
    """3D visualization page"""
    asteroids = Asteroid.objects.filter(close_approaches__isnull=False).distinct()[:20]
    
    context = {
        'asteroids': asteroids,
    }
    
    return render(request, 'visualizer/visualizer.html', context)

def orbit_view(request, asteroid_id):
    """Detailed orbit visualization for specific asteroid"""
    asteroid = get_object_or_404(Asteroid, neo_id=asteroid_id)
    
    context = {
        'asteroid': asteroid,
        'close_approaches': asteroid.close_approaches.all()[:5]
    }
    
    return render(request, 'visualizer/orbit_view.html', context)