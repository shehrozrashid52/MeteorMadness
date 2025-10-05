import os
from django.core.management.base import BaseCommand
from django.conf import settings

class Command(BaseCommand):
    help = 'Generate high-quality SVG images for asteroids'

    def handle(self, *args, **options):
        # Asteroid image data with unique characteristics
        asteroid_data = {
            '99942': {'name': 'Apophis', 'color': '#ff4444', 'shape': 'elongated', 'craters': 3},
            '101955': {'name': 'Bennu', 'color': '#2d2d2d', 'shape': 'diamond', 'craters': 5},
            '162173': {'name': 'Ryugu', 'color': '#4a4a4a', 'shape': 'diamond', 'craters': 4},
            '25143': {'name': 'Itokawa', 'color': '#8b7355', 'shape': 'peanut', 'craters': 2},
            '433': {'name': 'Eros', 'color': '#a0a0a0', 'shape': 'elongated', 'craters': 6},
            '4179': {'name': 'Toutatis', 'color': '#666666', 'shape': 'irregular', 'craters': 4},
            '1566': {'name': 'Icarus', 'color': '#ff6b35', 'shape': 'round', 'craters': 3},
            '4': {'name': 'Vesta', 'color': '#c4a484', 'shape': 'round', 'craters': 8},
            '1': {'name': 'Ceres', 'color': '#8c7853', 'shape': 'round', 'craters': 10},
            'HALLEY': {'name': 'Halley', 'color': '#4a90e2', 'shape': 'comet', 'craters': 0},
            'HALE_BOPP': {'name': 'Hale-Bopp', 'color': '#5bc0de', 'shape': 'comet', 'craters': 0},
            'NEOWISE': {'name': 'NEOWISE', 'color': '#f0ad4e', 'shape': 'comet', 'craters': 0},
            'TUNGUSKA': {'name': 'Tunguska', 'color': '#d9534f', 'shape': 'fragment', 'craters': 0},
            'CHELYABINSK': {'name': 'Chelyabinsk', 'color': '#ff8c00', 'shape': 'fragment', 'craters': 0},
            '16': {'name': 'Psyche', 'color': '#c0c0c0', 'shape': 'metallic', 'craters': 5},
            '2': {'name': 'Pallas', 'color': '#9d9d9d', 'shape': 'round', 'craters': 7},
            '65803': {'name': 'Didymos', 'color': '#7a7a7a', 'shape': 'binary', 'craters': 3},
            '3200': {'name': 'Phaethon', 'color': '#ff4500', 'shape': 'round', 'craters': 4},
            '1950DA': {'name': '1950 DA', 'color': '#696969', 'shape': 'round', 'craters': 5},
            'OUMUAMUA': {'name': 'Oumuamua', 'color': '#8b4513', 'shape': 'cigar', 'craters': 0}
        }

        # Create images directory
        images_dir = os.path.join(settings.BASE_DIR, 'static', 'images', 'asteroids')
        os.makedirs(images_dir, exist_ok=True)

        self.stdout.write(self.style.SUCCESS(f'Generating {len(asteroid_data)} asteroid images...'))

        for asteroid_id, data in asteroid_data.items():
            filename = f'{asteroid_id}.svg'
            filepath = os.path.join(images_dir, filename)

            svg_content = self.generate_asteroid_svg(data)
            
            with open(filepath, 'w') as f:
                f.write(svg_content)

            self.stdout.write(self.style.SUCCESS(f'Generated {filename}'))

        self.stdout.write(self.style.SUCCESS('Image generation complete!'))

    def generate_asteroid_svg(self, data):
        """Generate unique SVG for each asteroid"""
        name = data['name']
        color = data['color']
        shape = data['shape']
        craters = data['craters']

        # Base SVG template
        svg = f'''<svg width="400" height="300" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <radialGradient id="spaceGrad" cx="50%" cy="50%" r="50%">
            <stop offset="0%" style="stop-color:#1a1a2e;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#0a0a0a;stop-opacity:1" />
        </radialGradient>
        <radialGradient id="asteroidGrad" cx="30%" cy="30%" r="70%">
            <stop offset="0%" style="stop-color:{self.lighten_color(color)};stop-opacity:1" />
            <stop offset="100%" style="stop-color:{color};stop-opacity:1" />
        </radialGradient>
        <filter id="glow">
            <feGaussianBlur stdDeviation="3" result="coloredBlur"/>
            <feMerge> 
                <feMergeNode in="coloredBlur"/>
                <feMergeNode in="SourceGraphic"/>
            </feMerge>
        </filter>
    </defs>
    
    <!-- Space background -->
    <rect width="100%" height="100%" fill="url(#spaceGrad)"/>
    
    <!-- Stars -->
    {self.generate_stars()}
    
    <!-- Asteroid shape -->
    {self.generate_shape(shape, color)}
    
    <!-- Craters -->
    {self.generate_craters(craters, shape)}
    
    <!-- Name label -->
    <text x="200" y="280" text-anchor="middle" fill="#00ffff" font-family="Orbitron, monospace" font-size="16" font-weight="bold" filter="url(#glow)">{name}</text>
</svg>'''
        return svg

    def generate_stars(self):
        """Generate random stars in background"""
        stars = []
        import random
        for i in range(20):
            x = random.randint(10, 390)
            y = random.randint(10, 250)
            size = random.choice([1, 1.5, 2])
            opacity = random.uniform(0.3, 1.0)
            stars.append(f'<circle cx="{x}" cy="{y}" r="{size}" fill="#ffffff" opacity="{opacity}"/>')
        return '\n    '.join(stars)

    def generate_shape(self, shape, color):
        """Generate asteroid shape based on type"""
        if shape == 'round':
            return f'<circle cx="200" cy="150" r="80" fill="url(#asteroidGrad)" stroke="{color}" stroke-width="2"/>'
        elif shape == 'elongated':
            return f'<ellipse cx="200" cy="150" rx="100" ry="60" fill="url(#asteroidGrad)" stroke="{color}" stroke-width="2"/>'
        elif shape == 'diamond':
            return f'<polygon points="200,70 280,150 200,230 120,150" fill="url(#asteroidGrad)" stroke="{color}" stroke-width="2"/>'
        elif shape == 'peanut':
            return f'''<ellipse cx="170" cy="130" rx="40" ry="60" fill="url(#asteroidGrad)" stroke="{color}" stroke-width="2"/>
                      <ellipse cx="230" cy="170" rx="40" ry="60" fill="url(#asteroidGrad)" stroke="{color}" stroke-width="2"/>'''
        elif shape == 'irregular':
            return f'<polygon points="150,100 250,90 280,140 260,200 180,220 120,180 130,120" fill="url(#asteroidGrad)" stroke="{color}" stroke-width="2"/>'
        elif shape == 'comet':
            return f'''<ellipse cx="180" cy="150" rx="30" ry="40" fill="url(#asteroidGrad)" stroke="{color}" stroke-width="2"/>
                      <path d="M 210 150 Q 300 120 350 100" stroke="{color}" stroke-width="8" fill="none" opacity="0.6"/>
                      <path d="M 210 150 Q 320 140 380 130" stroke="{self.lighten_color(color)}" stroke-width="4" fill="none" opacity="0.4"/>'''
        elif shape == 'fragment':
            return f'''<polygon points="180,120 220,110 240,140 230,170 190,180 160,160" fill="url(#asteroidGrad)" stroke="{color}" stroke-width="2"/>
                      <polygon points="240,130 270,125 280,150 260,170 240,165" fill="{color}" opacity="0.8"/>'''
        elif shape == 'metallic':
            return f'<circle cx="200" cy="150" r="75" fill="url(#asteroidGrad)" stroke="{color}" stroke-width="3" opacity="0.9"/>'
        elif shape == 'binary':
            return f'''<circle cx="170" cy="150" r="50" fill="url(#asteroidGrad)" stroke="{color}" stroke-width="2"/>
                      <circle cx="240" cy="150" r="25" fill="{color}" opacity="0.8"/>'''
        elif shape == 'cigar':
            return f'<ellipse cx="200" cy="150" rx="120" ry="25" fill="url(#asteroidGrad)" stroke="{color}" stroke-width="2"/>'
        else:
            return f'<circle cx="200" cy="150" r="70" fill="url(#asteroidGrad)" stroke="{color}" stroke-width="2"/>'

    def generate_craters(self, count, shape):
        """Generate craters on asteroid surface"""
        if count == 0:
            return ''
        
        craters = []
        import random
        for i in range(count):
            if shape == 'round':
                x = random.randint(140, 260)
                y = random.randint(90, 210)
            elif shape == 'elongated':
                x = random.randint(120, 280)
                y = random.randint(110, 190)
            else:
                x = random.randint(150, 250)
                y = random.randint(100, 200)
            
            size = random.randint(5, 15)
            craters.append(f'<circle cx="{x}" cy="{y}" r="{size}" fill="#000000" opacity="0.4"/>')
        
        return '\n    '.join(craters)

    def lighten_color(self, hex_color):
        """Lighten a hex color for gradient effect"""
        hex_color = hex_color.lstrip('#')
        rgb = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
        lighter_rgb = tuple(min(255, int(c * 1.3)) for c in rgb)
        return f"#{lighter_rgb[0]:02x}{lighter_rgb[1]:02x}{lighter_rgb[2]:02x}"