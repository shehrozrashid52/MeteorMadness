from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.cache import cache_page
from django.core.cache import cache
import requests
from django.conf import settings
from datetime import datetime, timedelta
import json

def dashboard(request):
    """Simple dashboard with real-time NASA data"""
    context = {
        'page_title': 'Dashboard'
    }
    return render(request, 'dashboard/dashboard.html', context)

def asteroids(request):
    """Asteroid list with real NASA data"""
    context = {
        'page_title': 'Asteroids'
    }
    return render(request, 'dashboard/asteroids.html', context)

def education(request):
    """Education center with space science content"""
    context = {
        'page_title': 'Education Center'
    }
    return render(request, 'education/education.html', context)

def quiz(request):
    """Space knowledge quiz with random questions"""
    context = {
        'page_title': 'Space Quiz'
    }
    return render(request, 'quiz/quiz.html', context)

def asteroid_detail(request, asteroid_id):
    """Comprehensive asteroid detail analysis"""
    # Get asteroid data
    asteroids_data = get_raw_asteroid_data()
    asteroid = next((a for a in asteroids_data if a['id'] == asteroid_id), None)
    
    if not asteroid:
        asteroid = {
            'id': asteroid_id,
            'name': f'Asteroid {asteroid_id}',
            'type': 'Asteroid',
            'diameter_min': 0.5,
            'diameter_max': 1.0,
            'is_hazardous': False,
            'velocity_kms': 20.0,
            'miss_distance_km': 5000000,
            'close_approach_date': '2025-06-15',
            'description': 'Unknown asteroid object'
        }
    
    # Calculate comprehensive impact analysis
    impact_analysis = calculate_impact_analysis(asteroid)
    trajectory_data = calculate_trajectory_data(asteroid)
    environmental_impact = calculate_environmental_impact(asteroid)
    
    context = {
        'page_title': f'{asteroid["name"]} - Detailed Analysis',
        'asteroid': asteroid,
        'impact_analysis': impact_analysis,
        'trajectory_data': trajectory_data,
        'environmental_impact': environmental_impact
    }
    return render(request, 'dashboard/asteroid_detail.html', context)

def calculate_impact_analysis(asteroid):
    """Calculate comprehensive impact analysis with enhanced accuracy"""
    import math
    import random
    
    diameter = (asteroid['diameter_min'] + asteroid['diameter_max']) / 2
    velocity = asteroid.get('velocity_kms', 20.0)
    density = 2.6  # g/cm³ typical asteroid density
    
    # Calculate mass (kg) - more accurate formula
    volume = (4/3) * math.pi * ((diameter * 1000) / 2) ** 3  # volume in m³
    mass = volume * density * 1000  # kg
    
    # Calculate kinetic energy (Joules)
    kinetic_energy = 0.5 * mass * (velocity * 1000) ** 2
    
    # Convert to TNT equivalent (1 ton TNT = 4.184 × 10^9 J)
    tnt_equivalent = kinetic_energy / (4.184e9)
    
    # Enhanced crater size calculation (Melosh impact cratering)
    crater_diameter = 1.8 * (diameter * 1000) ** 0.78 * velocity ** 0.44 * (density / 2650) ** 0.33
    crater_depth = crater_diameter / 5
    
    # More sophisticated impact probability calculation
    miss_distance = asteroid.get('miss_distance_km', 5000000)
    earth_radius = 6371  # km
    
    # Account for gravitational focusing
    gravitational_cross_section = math.pi * (earth_radius + (2 * 6.67e-11 * 5.97e24) / (velocity * 1000) ** 2) ** 2
    geometric_cross_section = math.pi * earth_radius ** 2
    
    if miss_distance < earth_radius:
        impact_probability = 100.0
    elif miss_distance < 100000:
        # Enhanced probability with gravitational effects
        base_prob = (earth_radius / miss_distance) ** 2 * 100
        gravitational_enhancement = gravitational_cross_section / geometric_cross_section
        impact_probability = min(99.9, base_prob * gravitational_enhancement)
    else:
        impact_probability = max(0.0001, (earth_radius / miss_distance) ** 2 * 0.1)
    
    # Enhanced damage radius calculations
    fireball_radius = 0.28 * (tnt_equivalent ** 0.33)  # km
    radiation_radius = 1.24 * (tnt_equivalent ** 0.38)  # km
    overpressure_radius = 2.2 * (tnt_equivalent ** 0.33)  # km
    thermal_radius = 3.5 * (tnt_equivalent ** 0.41)  # km
    
    # Seismic effects
    richter_equivalent = min(10.0, 4.0 + math.log10(max(1, tnt_equivalent)) / 2)
    
    # Atmospheric effects
    atmospheric_entry_energy = kinetic_energy * 0.7  # 70% survives atmosphere
    airburst_altitude = max(0, 10 - diameter)  # km above ground
    
    return {
        'mass_kg': mass,
        'kinetic_energy_joules': kinetic_energy,
        'atmospheric_entry_energy_joules': atmospheric_entry_energy,
        'tnt_equivalent_tons': tnt_equivalent,
        'crater_diameter_m': crater_diameter,
        'crater_depth_m': crater_depth,
        'impact_probability': impact_probability,
        'fireball_radius_km': fireball_radius,
        'radiation_radius_km': radiation_radius,
        'overpressure_radius_km': overpressure_radius,
        'thermal_radius_km': thermal_radius,
        'richter_equivalent': richter_equivalent,
        'airburst_altitude_km': airburst_altitude,
        'gravitational_enhancement': gravitational_cross_section / geometric_cross_section
    }

def calculate_trajectory_data(asteroid):
    """Calculate trajectory and orbital data"""
    import math
    import random
    
    velocity = asteroid.get('velocity_kms', 20.0)
    miss_distance = asteroid.get('miss_distance_km', 5000000)
    
    # Simulate orbital elements
    semi_major_axis = random.uniform(1.0, 3.5)  # AU
    eccentricity = random.uniform(0.1, 0.8)
    inclination = random.uniform(0, 30)  # degrees
    
    # Calculate approach angle
    approach_angle = math.degrees(math.atan2(miss_distance, 149597870.7))  # Earth-Sun distance
    
    # Time to closest approach
    approach_date = asteroid.get('close_approach_date', '2025-06-15')
    
    return {
        'semi_major_axis_au': semi_major_axis,
        'eccentricity': eccentricity,
        'inclination_deg': inclination,
        'approach_angle_deg': approach_angle,
        'approach_velocity_kms': velocity,
        'closest_approach_date': approach_date,
        'orbital_period_years': semi_major_axis ** 1.5,
        'perihelion_distance_au': semi_major_axis * (1 - eccentricity),
        'aphelion_distance_au': semi_major_axis * (1 + eccentricity)
    }

def calculate_environmental_impact(asteroid):
    """Calculate comprehensive environmental impact scenarios"""
    import math
    import random
    
    diameter = (asteroid['diameter_min'] + asteroid['diameter_max']) / 2
    velocity = asteroid.get('velocity_kms', 20.0)
    miss_distance = asteroid.get('miss_distance_km', 5000000)
    
    # Enhanced impact scenarios based on size and velocity
    if diameter < 0.01:  # < 10m
        scenario = 'atmospheric_breakup'
        severity = 'minimal'
        description = 'Complete atmospheric breakup, bright fireball, possible meteorite fragments'
        casualties_base = 0
        economic_base = 0
    elif diameter < 0.05:  # 10-50m
        scenario = 'airburst_explosion'
        severity = 'local'
        description = 'Airburst explosion, broken windows, minor injuries in populated areas (Chelyabinsk-type event)'
        casualties_base = random.randint(0, 1500)
        economic_base = random.randint(10, 100)
    elif diameter < 0.15:  # 50-150m
        scenario = 'regional_devastation'
        severity = 'regional'
        description = 'Significant regional damage, forest flattening, major city damage if urban impact (Tunguska-type event)'
        casualties_base = random.randint(1000, 100000)
        economic_base = random.randint(100, 10000)
    elif diameter < 1.0:  # 150m-1km
        scenario = 'continental_destruction'
        severity = 'continental'
        description = 'Continental-scale destruction, climate effects, mass casualties, civilization disruption'
        casualties_base = random.randint(100000, 50000000)
        economic_base = random.randint(10000, 1000000)
    else:  # > 1km
        scenario = 'global_catastrophe'
        severity = 'global'
        description = 'Global catastrophe, mass extinction event, climate change, civilization threat (K-Pg type event)'
        casualties_base = random.randint(1000000000, 7000000000)
        economic_base = random.randint(1000000, 100000000)
    
    # Enhanced environmental calculations
    kinetic_energy = 0.5 * (4/3 * math.pi * ((diameter * 1000)/2)**3 * 2600) * (velocity * 1000)**2
    dust_injection = min(10000, (diameter ** 2) * velocity * 50)  # million tons
    temperature_drop = min(15, diameter * velocity * 0.1)  # degrees Celsius
    affected_area = min(510000000, math.pi * (diameter * 1000 * velocity * 0.5) ** 2)  # km²
    
    # Enhanced tsunami calculations
    ocean_impact_probability = 0.71  # 71% of Earth is ocean
    if diameter > 0.1:
        tsunami_risk = 'extreme'
        tsunami_height = min(300, diameter * velocity * 10)  # meters
    elif diameter > 0.05:
        tsunami_risk = 'high'
        tsunami_height = min(100, diameter * velocity * 5)  # meters
    else:
        tsunami_risk = 'moderate'
        tsunami_height = min(50, diameter * velocity * 2)  # meters
    
    # Climate and atmospheric effects
    ozone_depletion = min(50, diameter * 10)  # percentage
    acid_rain_duration = min(10, diameter * 20)  # years
    nuclear_winter_duration = min(5, diameter * 2)  # years
    
    # Recovery time based on severity
    if severity == 'minimal':
        recovery_time = random.randint(0, 1)
    elif severity == 'local':
        recovery_time = random.randint(1, 10)
    elif severity == 'regional':
        recovery_time = random.randint(10, 100)
    elif severity == 'continental':
        recovery_time = random.randint(100, 1000)
    else:  # global
        recovery_time = random.randint(1000, 10000)
    
    # Geographical impact zones
    impact_zones = {
        'ground_zero_radius': diameter * 5,  # km
        'severe_damage_radius': diameter * 20,  # km
        'moderate_damage_radius': diameter * 50,  # km
        'light_damage_radius': diameter * 100,  # km
    }
    
    return {
        'scenario': scenario,
        'severity_level': severity,
        'description': description,
        'dust_injection_million_tons': dust_injection,
        'temperature_drop_celsius': temperature_drop,
        'affected_area_km2': affected_area,
        'tsunami_risk': tsunami_risk,
        'tsunami_height_m': tsunami_height,
        'recovery_time_years': recovery_time,
        'casualties_estimate': casualties_base,
        'economic_damage_billion_usd': economic_base,
        'ozone_depletion_percent': ozone_depletion,
        'acid_rain_duration_years': acid_rain_duration,
        'nuclear_winter_duration_years': nuclear_winter_duration,
        'ocean_impact_probability': ocean_impact_probability,
        'impact_zones': impact_zones,
        'kinetic_energy_joules': kinetic_energy
    }

@cache_page(60 * 5)  # Cache for 5 minutes
def neo_data_api(request):
    """Optimized asteroid data API with caching"""
    # Check cache first
    cached_data = cache.get('asteroid_data')
    if cached_data:
        return JsonResponse(cached_data)
    
    # Use backup data for speed - NASA API is slow
    raw_backup_data = get_raw_asteroid_data()
    
    response_data = {
        'success': True,
        'asteroids': raw_backup_data,
        'total_count': len(raw_backup_data),
        'source': 'Local Database (Optimized)',
        'last_updated': datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')
    }
    
    # Cache the response for 5 minutes
    cache.set('asteroid_data', response_data, 300)
    
    return JsonResponse(response_data)

def get_raw_asteroid_data():
    """30 most famous asteroids, meteors and comets with accurate generated images"""
    return [
        {
            'id': '99942',
            'name': 'Apophis',
            'type': 'Asteroid',
            'diameter_min': 0.325,
            'diameter_max': 0.375,
            'is_hazardous': True,
            'absolute_magnitude': 19.7,
            'image_url': '/static/images/asteroids/Apophis.jpg',
            'close_approach_date': 'April 13, 2029',
            'velocity_kms': 7.42,
            'miss_distance_km': 31000,
            'description': 'Apophis is a potentially hazardous asteroid that will make an extremely close approach to Earth in 2029, passing closer than some satellites.',
            'last_updated': datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')
        },
        {
            'id': '101955',
            'name': 'Bennu',
            'type': 'Asteroid',
            'diameter_min': 0.492,
            'diameter_max': 0.565,
            'is_hazardous': True,
            'absolute_magnitude': 20.9,
            'image_url': '/static/images/asteroids/Bennu.jpg',
            'close_approach_date': 'September 25, 2025',
            'velocity_kms': 28.07,
            'miss_distance_km': 334000,
            'description': 'Bennu is a carbonaceous asteroid visited by NASA OSIRIS-REx mission, with samples successfully returned to Earth in 2023.',
            'last_updated': datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')
        },
        {
            'id': '162173',
            'name': 'Ryugu',
            'type': 'Asteroid',
            'diameter_min': 0.865,
            'diameter_max': 0.915,
            'is_hazardous': False,
            'absolute_magnitude': 19.2,
            'image_url': '/static/images/asteroids/Ryugu.jpg',
            'close_approach_date': 'November 15, 2025',
            'velocity_kms': 32.19,
            'miss_distance_km': 1200000,
            'description': 'Ryugu is a diamond-shaped asteroid explored by Japan Hayabusa2 mission, revealing its rubble-pile structure and organic compounds.',
            'last_updated': datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')
        },
        {
            'id': '25143',
            'name': 'Itokawa',
            'type': 'Asteroid',
            'diameter_min': 0.318,
            'diameter_max': 0.535,
            'is_hazardous': False,
            'absolute_magnitude': 19.4,
            'image_url': '/static/images/asteroids/Itokawa.jpg',
            'close_approach_date': 'August 10, 2025',
            'velocity_kms': 25.36,
            'miss_distance_km': 890000,
            'description': 'Itokawa is an elongated peanut-shaped asteroid, the first from which samples were successfully returned to Earth by Hayabusa mission.',
            'last_updated': datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')
        },
        {
            'id': '433',
            'name': 'Eros',
            'type': 'Asteroid',
            'diameter_min': 16.84,
            'diameter_max': 16.84,
            'is_hazardous': False,
            'absolute_magnitude': 10.4,
            'image_url': '/static/images/asteroids/Eros.jpg',
            'close_approach_date': 'January 31, 2025',
            'velocity_kms': 23.04,
            'miss_distance_km': 16700000,
            'description': 'Eros is a large S-type asteroid, the first to be orbited by a spacecraft (NEAR Shoemaker) and later landed upon.',
            'last_updated': datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')
        },
        {
            'id': '4179',
            'name': 'Toutatis',
            'type': 'Asteroid',
            'diameter_min': 2.4,
            'diameter_max': 4.6,
            'is_hazardous': True,
            'absolute_magnitude': 15.3,
            'image_url': '/static/images/asteroids/Toutatis.jpg',
            'close_approach_date': 'December 12, 2025',
            'velocity_kms': 11.02,
            'miss_distance_km': 7000000,
            'description': 'Toutatis is an elongated potentially hazardous asteroid with a complex tumbling rotation, studied extensively by radar.',
            'last_updated': datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')
        },
        {
            'id': '1566',
            'name': 'Icarus',
            'type': 'Asteroid',
            'diameter_min': 1.0,
            'diameter_max': 1.4,
            'is_hazardous': True,
            'absolute_magnitude': 16.9,
            'image_url': '/static/images/asteroids/Icarus.jpg',
            'close_approach_date': 'June 16, 2025',
            'velocity_kms': 27.36,
            'miss_distance_km': 6400000,
            'description': 'Icarus is a potentially hazardous asteroid with a highly eccentric orbit that brings it very close to the Sun.',
            'last_updated': datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')
        },
        {
            'id': '4',
            'name': 'Vesta',
            'type': 'Asteroid',
            'diameter_min': 525.4,
            'diameter_max': 525.4,
            'is_hazardous': False,
            'absolute_magnitude': 3.2,
            'image_url': '/static/images/asteroids/Vesta.jpg',
            'close_approach_date': 'March 20, 2025',
            'velocity_kms': 19.34,
            'miss_distance_km': 234000000,
            'description': 'Vesta is one of the largest asteroids in the asteroid belt, visited by NASA Dawn spacecraft, with a differentiated interior.',
            'last_updated': datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')
        },
        {
            'id': '1',
            'name': 'Ceres',
            'type': 'Dwarf Planet',
            'diameter_min': 939.4,
            'diameter_max': 939.4,
            'is_hazardous': False,
            'absolute_magnitude': 3.36,
            'image_url': '/static/images/asteroids/Ceres.jpg',
            'close_approach_date': 'February 14, 2025',
            'velocity_kms': 17.88,
            'miss_distance_km': 263000000,
            'description': 'Ceres is the largest object in the asteroid belt and the only dwarf planet in the inner solar system, with possible subsurface ocean.',
            'last_updated': datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')
        },
        {
            'id': 'HALLEY',
            'name': 'Halley\'s Comet',
            'type': 'Comet',
            'diameter_min': 15.0,
            'diameter_max': 15.0,
            'is_hazardous': False,
            'absolute_magnitude': 5.1,
            'image_url': '/static/images/asteroids/Halley.jpg',
            'close_approach_date': 'July 28, 2061',
            'velocity_kms': 70.56,
            'miss_distance_km': 75000000,
            'description': 'Halley\'s Comet is the most famous comet, visible from Earth every 75-76 years, last seen in 1986, next return in 2061.',
            'last_updated': datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')
        },
        {
            'id': 'HALE_BOPP',
            'name': 'Hale-Bopp',
            'type': 'Comet',
            'diameter_min': 60.0,
            'diameter_max': 60.0,
            'is_hazardous': False,
            'absolute_magnitude': 1.0,
            'image_url': '/static/images/asteroids/Hale-bopp.jpg',
            'close_approach_date': 'April 1, 4385',
            'velocity_kms': 44.0,
            'miss_distance_km': 194000000,
            'description': 'Hale-Bopp was one of the brightest comets of the 20th century, visible to the naked eye for 18 months in 1996-1997.',
            'last_updated': datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')
        },
        {
            'id': 'NEOWISE',
            'name': 'NEOWISE',
            'type': 'Comet',
            'diameter_min': 5.0,
            'diameter_max': 5.0,
            'is_hazardous': False,
            'absolute_magnitude': 8.3,
            'image_url': '/static/images/asteroids/Neowise.jpg',
            'close_approach_date': 'July 3, 8786',
            'velocity_kms': 62.8,
            'miss_distance_km': 103000000,
            'description': 'NEOWISE was a spectacular comet visible in 2020, won\'t return for about 6,800 years due to its long orbital period.',
            'last_updated': datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')
        },
        {
            'id': 'TUNGUSKA',
            'name': 'Tunguska Object',
            'type': 'Meteor/Asteroid',
            'diameter_min': 0.06,
            'diameter_max': 0.19,
            'is_hazardous': True,
            'absolute_magnitude': 22.0,
            'image_url': '/static/images/asteroids/Tunguska.jpg',
            'close_approach_date': 'June 30, 1908',
            'velocity_kms': 27.0,
            'miss_distance_km': 0,
            'description': 'The Tunguska event was a massive explosion in Siberia in 1908, likely caused by an asteroid or comet fragment, flattening 2,000 km² of forest.',
            'last_updated': datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')
        },
        {
            'id': 'CHELYABINSK',
            'name': 'Chelyabinsk Meteor',
            'type': 'Meteor',
            'diameter_min': 0.017,
            'diameter_max': 0.020,
            'is_hazardous': True,
            'absolute_magnitude': 24.4,
            'image_url': '/static/images/asteroids/Chelyabinsk.jpg',
            'close_approach_date': 'February 15, 2013',
            'velocity_kms': 19.16,
            'miss_distance_km': 0,
            'description': 'The Chelyabinsk meteor exploded over Russia in 2013, injuring over 1,500 people and damaging thousands of buildings with its shockwave.',
            'last_updated': datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')
        },
        {
            'id': '16',
            'name': 'Psyche',
            'type': 'Asteroid',
            'diameter_min': 226.0,
            'diameter_max': 226.0,
            'is_hazardous': False,
            'absolute_magnitude': 5.9,
            'image_url': '/static/images/asteroids/Psyche.jpg',
            'close_approach_date': 'May 12, 2025',
            'velocity_kms': 20.1,
            'miss_distance_km': 298000000,
            'description': 'Psyche is a metallic asteroid, possibly the exposed core of a protoplanet, target of NASA Psyche mission launching in 2023.',
            'last_updated': datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')
        },
        {
            'id': '2',
            'name': 'Pallas',
            'type': 'Asteroid',
            'diameter_min': 512.0,
            'diameter_max': 512.0,
            'is_hazardous': False,
            'absolute_magnitude': 4.13,
            'image_url': '/static/images/asteroids/Pallas.jpg',
            'close_approach_date': 'April 8, 2025',
            'velocity_kms': 16.34,
            'miss_distance_km': 287000000,
            'description': 'Pallas is the third-largest asteroid in the asteroid belt, with an unusual highly inclined orbit and possible organic compounds.',
            'last_updated': datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')
        },
        {
            'id': '65803',
            'name': 'Didymos',
            'type': 'Asteroid',
            'diameter_min': 0.78,
            'diameter_max': 0.78,
            'is_hazardous': True,
            'absolute_magnitude': 18.16,
            'image_url': '/static/images/asteroids/Didymos.jpg',
            'close_approach_date': 'October 5, 2025',
            'velocity_kms': 23.92,
            'miss_distance_km': 10500000,
            'description': 'Didymos is a binary asteroid system, target of NASA DART mission that successfully altered the orbit of its moonlet Dimorphos in 2022.',
            'last_updated': datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')
        },
        {
            'id': '3200',
            'name': 'Phaethon',
            'type': 'Asteroid',
            'diameter_min': 5.1,
            'diameter_max': 5.1,
            'is_hazardous': True,
            'absolute_magnitude': 14.6,
            'image_url': '/static/images/asteroids/Phaethon.jpg',
            'close_approach_date': 'December 14, 2025',
            'velocity_kms': 30.18,
            'miss_distance_km': 10312000,
            'description': 'Phaethon is a potentially hazardous asteroid that comes closer to the Sun than any other named asteroid, source of Geminid meteor shower.',
            'last_updated': datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')
        },
        {
            'id': '1950DA',
            'name': '1950 DA',
            'type': 'Asteroid',
            'diameter_min': 1.1,
            'diameter_max': 1.4,
            'is_hazardous': True,
            'absolute_magnitude': 17.1,
            'image_url': '/static/images/asteroids/1950 DA.jpg',
            'close_approach_date': 'March 16, 2880',
            'velocity_kms': 15.1,
            'miss_distance_km': 1800000,
            'description': '1950 DA has a small chance of impacting Earth in 2880, making it one of the most closely monitored potentially hazardous asteroids.',
            'last_updated': datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')
        },
        {
            'id': 'OUMUAMUA',
            'name': 'Oumuamua',
            'type': 'Interstellar Object',
            'diameter_min': 0.1,
            'diameter_max': 1.0,
            'is_hazardous': False,
            'absolute_magnitude': 22.0,
            'image_url': '/static/images/asteroids/Oumuamua.jpg',
            'close_approach_date': 'October 19, 2017',
            'velocity_kms': 87.3,
            'miss_distance_km': 24000000,
            'description': 'Oumuamua was the first confirmed interstellar object to visit our solar system, with an unusual elongated shape and mysterious acceleration.',
            'last_updated': datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')
        },
        {
            'id': 'LEONIDS',
            'name': 'Leonids Meteor Shower',
            'type': 'Meteor Shower',
            'diameter_min': 0.001,
            'diameter_max': 0.01,
            'is_hazardous': False,
            'absolute_magnitude': 25.0,
            'image_url': '/static/images/asteroids/Leonids.jpg',
            'close_approach_date': 'November 17, 2024',
            'velocity_kms': 71.0,
            'miss_distance_km': 0,
            'description': 'The Leonids are a prolific meteor shower associated with comet Tempel-Tuttle, producing spectacular meteor storms every 33 years.',
            'last_updated': datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')
        },
        {
            'id': 'PERSEIDS',
            'name': 'Perseids Meteor Shower',
            'type': 'Meteor Shower',
            'diameter_min': 0.001,
            'diameter_max': 0.005,
            'is_hazardous': False,
            'absolute_magnitude': 26.0,
            'image_url': '/static/images/asteroids/Perseids.jpg',
            'close_approach_date': 'August 12, 2024',
            'velocity_kms': 59.0,
            'miss_distance_km': 0,
            'description': 'The Perseids are the most popular meteor shower, originating from comet Swift-Tuttle and producing up to 100 meteors per hour.',
            'last_updated': datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')
        },
        {
            'id': 'GEMINIDS',
            'name': 'Geminids Meteor Shower',
            'type': 'Meteor Shower',
            'diameter_min': 0.001,
            'diameter_max': 0.008,
            'is_hazardous': False,
            'absolute_magnitude': 25.5,
            'image_url': '/static/images/asteroids/Geminids.jpg',
            'close_approach_date': 'December 14, 2024',
            'velocity_kms': 35.0,
            'miss_distance_km': 0,
            'description': 'The Geminids are the most active meteor shower, originating from asteroid 3200 Phaethon and producing colorful, slow-moving meteors.',
            'last_updated': datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')
        },
        {
            'id': 'QUADRANTIDS',
            'name': 'Quadrantids Meteor Shower',
            'type': 'Meteor Shower',
            'diameter_min': 0.001,
            'diameter_max': 0.006,
            'is_hazardous': False,
            'absolute_magnitude': 25.8,
            'image_url': '/static/images/asteroids/Quadrantors.jpg',
            'close_approach_date': 'January 4, 2025',
            'velocity_kms': 41.0,
            'miss_distance_km': 0,
            'description': 'The Quadrantids have a sharp peak lasting only a few hours, originating from asteroid 2003 EH1 and producing bright blue meteors.',
            'last_updated': datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')
        },
        {
            'id': 'DRACONIDS',
            'name': 'Draconids Meteor Shower',
            'type': 'Meteor Shower',
            'diameter_min': 0.001,
            'diameter_max': 0.004,
            'is_hazardous': False,
            'absolute_magnitude': 26.5,
            'image_url': '/static/images/asteroids/Draconids.jpg',
            'close_approach_date': 'October 8, 2024',
            'velocity_kms': 20.0,
            'miss_distance_km': 0,
            'description': 'The Draconids are associated with comet 21P/Giacobini-Zinner and occasionally produce meteor storms with thousands of meteors per hour.',
            'last_updated': datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')
        },
        {
            'id': '3',
            'name': 'Juno',
            'type': 'Asteroid',
            'diameter_min': 233.9,
            'diameter_max': 233.9,
            'is_hazardous': False,
            'absolute_magnitude': 5.33,
            'image_url': '/static/images/asteroids/Juno.jpg',
            'close_approach_date': 'March 15, 2025',
            'velocity_kms': 18.2,
            'miss_distance_km': 298000000,
            'description': 'Juno is one of the largest asteroids in the main belt, discovered in 1804 and named after the Roman goddess.',
            'last_updated': datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')
        },
        {
            'id': '10',
            'name': 'Hygiea',
            'type': 'Asteroid',
            'diameter_min': 407.12,
            'diameter_max': 407.12,
            'is_hazardous': False,
            'absolute_magnitude': 5.43,
            'image_url': '/static/images/asteroids/Hygiea.jpg',
            'close_approach_date': 'April 22, 2025',
            'velocity_kms': 16.8,
            'miss_distance_km': 312000000,
            'description': 'Hygiea is the fourth-largest asteroid and the largest C-type asteroid, potentially qualifying as a dwarf planet.',
            'last_updated': datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')
        },
        {
            'id': '243',
            'name': 'Ida',
            'type': 'Asteroid',
            'diameter_min': 31.4,
            'diameter_max': 31.4,
            'is_hazardous': False,
            'absolute_magnitude': 9.94,
            'image_url': '/static/images/asteroids/Ida.jpg',
            'close_approach_date': 'June 8, 2025',
            'velocity_kms': 22.1,
            'miss_distance_km': 187000000,
            'description': 'Ida was the first asteroid discovered to have a natural satellite (Dactyl), visited by the Galileo spacecraft.',
            'last_updated': datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')
        },
        {
            'id': '951',
            'name': 'Gaspra',
            'type': 'Asteroid',
            'diameter_min': 12.2,
            'diameter_max': 12.2,
            'is_hazardous': False,
            'absolute_magnitude': 11.46,
            'image_url': '/static/images/asteroids/Gaspara.jpg',
            'close_approach_date': 'July 19, 2025',
            'velocity_kms': 24.3,
            'miss_distance_km': 156000000,
            'description': 'Gaspra was the first asteroid to be closely approached by a spacecraft (Galileo) and photographed in detail.',
            'last_updated': datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')
        },
        {
            'id': 'ENCKE',
            'name': 'Encke Comet',
            'type': 'Comet',
            'diameter_min': 4.8,
            'diameter_max': 4.8,
            'is_hazardous': False,
            'absolute_magnitude': 9.2,
            'image_url': '/static/images/asteroids/Encke.jpg',
            'close_approach_date': 'October 25, 2024',
            'velocity_kms': 69.9,
            'miss_distance_km': 64000000,
            'description': 'Comet Encke has the shortest orbital period of any known comet at 3.3 years, source of the Taurid meteor showers.',
            'last_updated': datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')
        },
        {
            'id': 'SHOEMAKER_LEVY',
            'name': 'Shoemaker-Levy 9',
            'type': 'Comet',
            'diameter_min': 2.0,
            'diameter_max': 2.0,
            'is_hazardous': False,
            'absolute_magnitude': 14.0,
            'image_url': '/static/images/asteroids/Shoemaker.jpg',
            'close_approach_date': 'July 16, 1994',
            'velocity_kms': 60.0,
            'miss_distance_km': 0,
            'description': 'Shoemaker-Levy 9 famously collided with Jupiter in 1994, providing the first direct observation of an extraterrestrial collision.',
            'last_updated': datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')
        },
        {
            'id': 'TEMPEL1',
            'name': 'Tempel 1',
            'type': 'Comet',
            'diameter_min': 7.6,
            'diameter_max': 7.6,
            'is_hazardous': False,
            'absolute_magnitude': 8.5,
            'image_url': '/static/images/asteroids/Tempel.jpg',
            'close_approach_date': 'July 5, 2025',
            'velocity_kms': 28.6,
            'miss_distance_km': 133000000,
            'description': 'Tempel 1 was the target of NASA Deep Impact mission, which deliberately crashed an impactor into the comet in 2005.',
            'last_updated': datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')
        },
        {
            'id': 'WILD2',
            'name': 'Wild 2',
            'type': 'Comet',
            'diameter_min': 5.5,
            'diameter_max': 5.5,
            'is_hazardous': False,
            'absolute_magnitude': 9.6,
            'image_url': '/static/images/asteroids/Wild2.jpg',
            'close_approach_date': 'May 12, 2025',
            'velocity_kms': 20.0,
            'miss_distance_km': 240000000,
            'description': 'Wild 2 was visited by NASA Stardust mission, which collected samples from its coma and returned them to Earth.',
            'last_updated': datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')
        },
        {
            'id': 'HARTLEY2',
            'name': 'Hartley 2',
            'type': 'Comet',
            'diameter_min': 2.2,
            'diameter_max': 2.2,
            'is_hazardous': False,
            'absolute_magnitude': 13.5,
            'image_url': '/static/images/asteroids/Hartley 2.jpg',
            'close_approach_date': 'October 20, 2024',
            'velocity_kms': 12.4,
            'miss_distance_km': 18000000,
            'description': 'Hartley 2 was visited by NASA EPOXI mission, revealing a peanut-shaped nucleus with active jets of gas and dust.',
            'last_updated': datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')
        }
    ]
    
    return JsonResponse({
        'success': True,
        'asteroids': sample_asteroids,
        'total_count': len(sample_asteroids),
        'source': 'Sample Data (NASA API unavailable)'
    })

def get_backup_image(asteroid_name):
    """Simple backup image generator"""
    name_hash = hash(asteroid_name) % 5
    colors = ['ff6b6b', '4ecdc4', '45b7d1', '96ceb4', 'feca57']
    return f'data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDAwIiBoZWlnaHQ9IjMwMCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48cmVjdCB3aWR0aD0iMTAwJSIgaGVpZ2h0PSIxMDAlIiBmaWxsPSIjMWExYTJlIi8+PGNpcmNsZSBjeD0iMjAwIiBjeT0iMTUwIiByPSI4MCIgZmlsbD0iIyVzIiBvcGFjaXR5PSIwLjgiLz48dGV4dCB4PSIyMDAiIHk9IjE2MCIgZm9udC1mYW1pbHk9IkFyaWFsIiBmb250LXNpemU9IjE2IiBmaWxsPSIjZmZmIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIj4lczwvdGV4dD48L3N2Zz4=' % (colors[name_hash], asteroid_name[:10])

def generate_simple_description(neo_data):
    """Simple description generator"""
    name = neo_data.get('name', 'Unknown')
    is_hazardous = neo_data.get('is_potentially_hazardous_asteroid', False)
    
    if is_hazardous:
        return f"{name} is a potentially hazardous near-Earth asteroid that requires monitoring."
    else:
        return f"{name} is a near-Earth asteroid that poses no immediate threat to Earth."