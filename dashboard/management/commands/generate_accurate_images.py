import os
from django.core.management.base import BaseCommand
from django.conf import settings

class Command(BaseCommand):
    help = 'Generate accurate asteroid images based on real characteristics'

    def handle(self, *args, **options):
        # Accurate asteroid data with real characteristics
        asteroid_data = {
            '99942': {'name': 'Apophis', 'color': '#8B4513', 'shape': 'elongated', 'size': 'medium', 'texture': 'rocky', 'craters': 2},
            '101955': {'name': 'Bennu', 'color': '#2F2F2F', 'shape': 'diamond', 'size': 'small', 'texture': 'carbon', 'craters': 4},
            '162173': {'name': 'Ryugu', 'color': '#4A4A4A', 'shape': 'diamond', 'size': 'small', 'texture': 'rubble', 'craters': 3},
            '25143': {'name': 'Itokawa', 'color': '#D2B48C', 'shape': 'peanut', 'size': 'tiny', 'texture': 'regolith', 'craters': 1},
            '433': {'name': 'Eros', 'color': '#CD853F', 'shape': 'elongated', 'size': 'large', 'texture': 'rocky', 'craters': 8},
            '4179': {'name': 'Toutatis', 'color': '#696969', 'shape': 'irregular', 'size': 'medium', 'texture': 'rocky', 'craters': 5},
            '1566': {'name': 'Icarus', 'color': '#FF6347', 'shape': 'round', 'size': 'small', 'texture': 'metallic', 'craters': 3},
            '4': {'name': 'Vesta', 'color': '#DEB887', 'shape': 'round', 'size': 'huge', 'texture': 'basaltic', 'craters': 12},
            '1': {'name': 'Ceres', 'color': '#A0522D', 'shape': 'round', 'size': 'massive', 'texture': 'icy', 'craters': 15},
            'HALLEY': {'name': 'Halley', 'color': '#4682B4', 'shape': 'comet', 'size': 'medium', 'texture': 'icy', 'craters': 0},
            'HALE_BOPP': {'name': 'Hale-Bopp', 'color': '#87CEEB', 'shape': 'comet', 'size': 'large', 'texture': 'icy', 'craters': 0},
            'NEOWISE': {'name': 'NEOWISE', 'color': '#FFD700', 'shape': 'comet', 'size': 'small', 'texture': 'icy', 'craters': 0},
            'TUNGUSKA': {'name': 'Tunguska', 'color': '#8B0000', 'shape': 'fragment', 'size': 'tiny', 'texture': 'stony', 'craters': 0},
            'CHELYABINSK': {'name': 'Chelyabinsk', 'color': '#FF4500', 'shape': 'fragment', 'size': 'tiny', 'texture': 'stony', 'craters': 0},
            '16': {'name': 'Psyche', 'color': '#C0C0C0', 'shape': 'irregular', 'size': 'large', 'texture': 'metallic', 'craters': 6},
            '2': {'name': 'Pallas', 'color': '#778899', 'shape': 'round', 'size': 'huge', 'texture': 'rocky', 'craters': 10},
            '65803': {'name': 'Didymos', 'color': '#696969', 'shape': 'binary', 'size': 'small', 'texture': 'rocky', 'craters': 2},
            '3200': {'name': 'Phaethon', 'color': '#FF6B35', 'shape': 'round', 'size': 'medium', 'texture': 'rocky', 'craters': 4},
            '1950DA': {'name': '1950 DA', 'color': '#708090', 'shape': 'round', 'size': 'small', 'texture': 'rocky', 'craters': 3},
            'OUMUAMUA': {'name': 'Oumuamua', 'color': '#8B4513', 'shape': 'cigar', 'size': 'small', 'texture': 'rocky', 'craters': 0},
            # Additional meteors and asteroids
            'LEONIDS': {'name': 'Leonids', 'color': '#FFD700', 'shape': 'fragment', 'size': 'tiny', 'texture': 'stony', 'craters': 0},
            'PERSEIDS': {'name': 'Perseids', 'color': '#87CEEB', 'shape': 'fragment', 'size': 'tiny', 'texture': 'icy', 'craters': 0},
            'GEMINIDS': {'name': 'Geminids', 'color': '#FF69B4', 'shape': 'fragment', 'size': 'tiny', 'texture': 'rocky', 'craters': 0},
            'QUADRANTIDS': {'name': 'Quadrantids', 'color': '#32CD32', 'shape': 'fragment', 'size': 'tiny', 'texture': 'stony', 'craters': 0},
            'DRACONIDS': {'name': 'Draconids', 'color': '#9370DB', 'shape': 'fragment', 'size': 'tiny', 'texture': 'icy', 'craters': 0},
            # Additional major asteroids
            '3': {'name': 'Juno', 'color': '#B8860B', 'shape': 'irregular', 'size': 'huge', 'texture': 'rocky', 'craters': 9},
            '10': {'name': 'Hygiea', 'color': '#2F4F4F', 'shape': 'round', 'size': 'massive', 'texture': 'carbon', 'craters': 11},
            '243': {'name': 'Ida', 'color': '#CD853F', 'shape': 'elongated', 'size': 'medium', 'texture': 'rocky', 'craters': 6},
            '951': {'name': 'Gaspra', 'color': '#DAA520', 'shape': 'irregular', 'size': 'small', 'texture': 'rocky', 'craters': 4},
            # Additional famous comets
            'ENCKE': {'name': 'Encke', 'color': '#4169E1', 'shape': 'comet', 'size': 'small', 'texture': 'icy', 'craters': 0},
            'SHOEMAKER_LEVY': {'name': 'Shoemaker-Levy 9', 'color': '#DC143C', 'shape': 'fragment', 'size': 'small', 'texture': 'icy', 'craters': 0},
            'TEMPEL1': {'name': 'Tempel 1', 'color': '#6495ED', 'shape': 'comet', 'size': 'small', 'texture': 'icy', 'craters': 0},
            'WILD2': {'name': 'Wild 2', 'color': '#20B2AA', 'shape': 'comet', 'size': 'small', 'texture': 'icy', 'craters': 0},
            'HARTLEY2': {'name': 'Hartley 2', 'color': '#48D1CC', 'shape': 'peanut', 'size': 'tiny', 'texture': 'icy', 'craters': 0}
        }

        images_dir = os.path.join(settings.BASE_DIR, 'static', 'images', 'asteroids')
        os.makedirs(images_dir, exist_ok=True)

        self.stdout.write(self.style.SUCCESS(f'Generating {len(asteroid_data)} accurate space object images...'))

        for asteroid_id, data in asteroid_data.items():
            filename = f'{asteroid_id}.svg'
            filepath = os.path.join(images_dir, filename)

            svg_content = self.generate_accurate_svg(data)
            
            with open(filepath, 'w') as f:
                f.write(svg_content)

            self.stdout.write(self.style.SUCCESS(f'Generated {filename}'))

        self.stdout.write(self.style.SUCCESS('Complete space object image generation finished!'))
        
        # Print the list of all generated objects
        self.stdout.write(self.style.SUCCESS('\n=== COMPLETE LIST OF 30 SPACE OBJECTS ==='))
        for i, (asteroid_id, data) in enumerate(asteroid_data.items(), 1):
            self.stdout.write(f'{i:2d}. {data["name"]} ({asteroid_id}) - {data["shape"]} {data["size"]} {data["texture"]} object')

    def generate_accurate_svg(self, data):
        """Generate accurate SVG based on real asteroid characteristics"""
        name = data['name']
        color = data['color']
        shape = data['shape']
        size = data['size']
        texture = data['texture']
        craters = data['craters']

        # Size mapping
        size_map = {
            'tiny': 40, 'small': 60, 'medium': 80, 'large': 100, 'huge': 120, 'massive': 140
        }
        base_size = size_map.get(size, 80)

        # Base SVG template with realistic space background
        svg = f'''<svg width="400" height="300" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <radialGradient id="spaceGrad" cx="50%" cy="50%" r="50%">
            <stop offset="0%" style="stop-color:#0a0a1a;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#000000;stop-opacity:1" />
        </radialGradient>
        <radialGradient id="asteroidGrad" cx="30%" cy="30%" r="70%">
            <stop offset="0%" style="stop-color:{self.lighten_color(color)};stop-opacity:1" />
            <stop offset="70%" style="stop-color:{color};stop-opacity:1" />
            <stop offset="100%" style="stop-color:{self.darken_color(color)};stop-opacity:1" />
        </radialGradient>
        <filter id="glow">
            <feGaussianBlur stdDeviation="2" result="coloredBlur"/>
            <feMerge> 
                <feMergeNode in="coloredBlur"/>
                <feMergeNode in="SourceGraphic"/>
            </feMerge>
        </filter>
        <filter id="roughness">
            <feTurbulence baseFrequency="0.9" numOctaves="4" result="noise"/>
            <feDisplacementMap in="SourceGraphic" in2="noise" scale="3"/>
        </filter>
    </defs>
    
    <!-- Deep space background -->
    <rect width="100%" height="100%" fill="url(#spaceGrad)"/>
    
    <!-- Realistic stars -->
    {self.generate_realistic_stars()}
    
    <!-- Main asteroid shape -->
    {self.generate_accurate_shape(shape, color, base_size, texture)}
    
    <!-- Surface features -->
    {self.generate_surface_features(craters, shape, base_size, texture)}
    
    <!-- Name label with glow -->
    <text x="200" y="280" text-anchor="middle" fill="#ffffff" font-family="Arial, sans-serif" 
          font-size="14" font-weight="bold" filter="url(#glow)">{name}</text>
    
    <!-- Size indicator -->
    <text x="200" y="295" text-anchor="middle" fill="#cccccc" font-family="Arial, sans-serif" 
          font-size="10">{size.title()} • {texture.title()}</text>
</svg>'''
        return svg

    def generate_realistic_stars(self):
        """Generate realistic star field"""
        import random
        stars = []
        for i in range(30):
            x = random.randint(10, 390)
            y = random.randint(10, 250)
            size = random.choice([0.5, 1, 1.5, 2])
            brightness = random.uniform(0.3, 1.0)
            color = random.choice(['#ffffff', '#ffffcc', '#ccccff', '#ffcccc'])
            stars.append(f'<circle cx="{x}" cy="{y}" r="{size}" fill="{color}" opacity="{brightness}"/>')
        return '\n    '.join(stars)

    def generate_accurate_shape(self, shape, color, base_size, texture):
        """Generate accurate asteroid shape based on real characteristics"""
        center_x, center_y = 200, 150
        
        if shape == 'round':
            return f'<circle cx="{center_x}" cy="{center_y}" r="{base_size}" fill="url(#asteroidGrad)" stroke="{self.darken_color(color)}" stroke-width="2" filter="url(#roughness)"/>'
        
        elif shape == 'elongated':
            return f'<ellipse cx="{center_x}" cy="{center_y}" rx="{base_size * 1.4}" ry="{base_size * 0.7}" fill="url(#asteroidGrad)" stroke="{self.darken_color(color)}" stroke-width="2" filter="url(#roughness)"/>'
        
        elif shape == 'diamond':
            points = f"{center_x},{center_y - base_size} {center_x + base_size * 0.8},{center_y} {center_x},{center_y + base_size} {center_x - base_size * 0.8},{center_y}"
            return f'<polygon points="{points}" fill="url(#asteroidGrad)" stroke="{self.darken_color(color)}" stroke-width="2" filter="url(#roughness)"/>'
        
        elif shape == 'peanut':
            return f'''<ellipse cx="{center_x - 25}" cy="{center_y - 20}" rx="{base_size * 0.6}" ry="{base_size * 0.8}" fill="url(#asteroidGrad)" stroke="{self.darken_color(color)}" stroke-width="2" filter="url(#roughness)"/>
                      <ellipse cx="{center_x + 25}" cy="{center_y + 20}" rx="{base_size * 0.6}" ry="{base_size * 0.8}" fill="url(#asteroidGrad)" stroke="{self.darken_color(color)}" stroke-width="2" filter="url(#roughness)"/>'''
        
        elif shape == 'irregular':
            points = f"{center_x - base_size},{center_y - 40} {center_x + base_size * 1.2},{center_y - 20} {center_x + base_size * 0.8},{center_y + 60} {center_x - 20},{center_y + base_size} {center_x - base_size * 1.1},{center_y + 20}"
            return f'<polygon points="{points}" fill="url(#asteroidGrad)" stroke="{self.darken_color(color)}" stroke-width="2" filter="url(#roughness)"/>'
        
        elif shape == 'comet':
            nucleus = f'<ellipse cx="{center_x - 50}" cy="{center_y}" rx="{base_size * 0.4}" ry="{base_size * 0.5}" fill="url(#asteroidGrad)" stroke="{self.darken_color(color)}" stroke-width="2"/>'
            tail = f'<path d="M {center_x - 10} {center_y} Q {center_x + 80} {center_y - 30} {center_x + 150} {center_y - 10}" stroke="{color}" stroke-width="12" fill="none" opacity="0.6"/>'
            tail2 = f'<path d="M {center_x - 10} {center_y} Q {center_x + 100} {center_y + 20} {center_x + 180} {center_y + 30}" stroke="{self.lighten_color(color)}" stroke-width="8" fill="none" opacity="0.4"/>'
            return nucleus + tail + tail2
        
        elif shape == 'fragment':
            fragments = []
            for i in range(3):
                x = center_x + (i - 1) * 30
                y = center_y + (i - 1) * 20
                size = base_size * (0.3 + i * 0.2)
                fragments.append(f'<polygon points="{x - size},{y - size * 0.5} {x + size},{y - size * 0.3} {x + size * 0.7},{y + size} {x - size * 0.8},{y + size * 0.6}" fill="url(#asteroidGrad)" stroke="{self.darken_color(color)}" stroke-width="1"/>')
            return '\n                      '.join(fragments)
        
        elif shape == 'binary':
            primary = f'<circle cx="{center_x - 30}" cy="{center_y}" r="{base_size * 0.8}" fill="url(#asteroidGrad)" stroke="{self.darken_color(color)}" stroke-width="2" filter="url(#roughness)"/>'
            secondary = f'<circle cx="{center_x + 40}" cy="{center_y}" r="{base_size * 0.4}" fill="{color}" opacity="0.8" stroke="{self.darken_color(color)}" stroke-width="1"/>'
            return primary + secondary
        
        elif shape == 'cigar':
            return f'<ellipse cx="{center_x}" cy="{center_y}" rx="{base_size * 2}" ry="{base_size * 0.3}" fill="url(#asteroidGrad)" stroke="{self.darken_color(color)}" stroke-width="2" filter="url(#roughness)"/>'
        
        else:
            return f'<circle cx="{center_x}" cy="{center_y}" r="{base_size}" fill="url(#asteroidGrad)" stroke="{self.darken_color(color)}" stroke-width="2" filter="url(#roughness)"/>'

    def generate_surface_features(self, crater_count, shape, base_size, texture):
        """Generate realistic surface features"""
        if crater_count == 0:
            return ''
        
        features = []
        import random
        
        for i in range(crater_count):
            if shape == 'round':
                x = random.randint(160, 240)
                y = random.randint(110, 190)
            elif shape == 'elongated':
                x = random.randint(120, 280)
                y = random.randint(120, 180)
            else:
                x = random.randint(150, 250)
                y = random.randint(120, 180)
            
            crater_size = random.randint(3, min(15, base_size // 6))
            
            # Crater with rim and shadow
            features.append(f'<circle cx="{x}" cy="{y}" r="{crater_size}" fill="#000000" opacity="0.6"/>')
            features.append(f'<circle cx="{x}" cy="{y}" r="{crater_size + 1}" fill="none" stroke="#666666" stroke-width="0.5" opacity="0.8"/>')
        
        # Add texture based on material
        if texture == 'metallic':
            # Add metallic shine
            features.append(f'<ellipse cx="180" cy="130" rx="20" ry="8" fill="#ffffff" opacity="0.3"/>')
        elif texture == 'icy':
            # Add ice crystals
            for i in range(5):
                x = random.randint(170, 230)
                y = random.randint(130, 170)
                features.append(f'<circle cx="{x}" cy="{y}" r="2" fill="#ffffff" opacity="0.7"/>')
        
        return '\n    '.join(features)

    def lighten_color(self, hex_color):
        """Lighten a hex color"""
        hex_color = hex_color.lstrip('#')
        rgb = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
        lighter_rgb = tuple(min(255, int(c * 1.4)) for c in rgb)
        return f"#{lighter_rgb[0]:02x}{lighter_rgb[1]:02x}{lighter_rgb[2]:02x}"

    def darken_color(self, hex_color):
        """Darken a hex color"""
        hex_color = hex_color.lstrip('#')
        rgb = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
        darker_rgb = tuple(max(0, int(c * 0.6)) for c in rgb)
        return f"#{darker_rgb[0]:02x}{darker_rgb[1]:02x}{darker_rgb[2]:02x}"