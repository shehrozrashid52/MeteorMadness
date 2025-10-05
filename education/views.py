from django.shortcuts import render

def education(request):
    """Educational content about asteroids and impact science"""
    
    educational_content = {
        'orbital_elements': {
            'title': 'Orbital Elements',
            'description': 'The mathematical parameters that define the orbit of an asteroid around the Sun.',
            'details': [
                'Semi-major axis: Average distance from the Sun',
                'Eccentricity: How elliptical the orbit is',
                'Inclination: Tilt of the orbit relative to Earth\'s orbit',
                'Argument of perihelion: Orientation of the orbit',
                'Longitude of ascending node: Where orbit crosses Earth\'s orbital plane'
            ]
        },
        'impact_energy': {
            'title': 'Impact Energy',
            'description': 'The kinetic energy released when an asteroid hits Earth.',
            'details': [
                'Calculated using E = ½mv² (kinetic energy formula)',
                'Depends on mass and velocity of the asteroid',
                'Converted to TNT equivalent for comparison',
                'Larger asteroids and higher velocities create exponentially more energy'
            ]
        },
        'deflection_techniques': {
            'title': 'Deflection Techniques',
            'description': 'Methods to change an asteroid\'s trajectory to prevent Earth impact.',
            'details': [
                'Kinetic Impactor: Spacecraft collision to change velocity',
                'Gravity Tractor: Spacecraft uses gravity to slowly pull asteroid',
                'Nuclear Explosion: Last resort for large asteroids',
                'Ion Beam Shepherd: Continuous low-thrust propulsion'
            ]
        },
        'impact_effects': {
            'title': 'Impact Effects',
            'description': 'The various consequences of an asteroid impact on Earth.',
            'details': [
                'Crater formation: Direct excavation of material',
                'Seismic waves: Earthquake-like effects',
                'Atmospheric effects: Dust and debris blocking sunlight',
                'Tsunamis: If impact occurs in ocean',
                'Climate change: Long-term cooling from dust'
            ]
        }
    }
    
    context = {
        'educational_content': educational_content,
    }
    
    return render(request, 'education/education.html', context)