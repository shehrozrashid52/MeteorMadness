import os
import requests
from django.core.management.base import BaseCommand
from django.conf import settings

class Command(BaseCommand):
    help = 'Download asteroid images and store them locally'

    def handle(self, *args, **options):
        # Asteroid image URLs mapping
        asteroid_images = {
            '99942': 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/32/Apophis_2004_MN4.jpg/400px-Apophis_2004_MN4.jpg',
            '101955': 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Bennu_mosaic_OSIRIS-REx.jpg/400px-Bennu_mosaic_OSIRIS-REx.jpg',
            '162173': 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/8a/Ryugu.jpg/400px-Ryugu.jpg',
            '25143': 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/6c/Itokawa8_hayabusa_1210.jpg/400px-Itokawa8_hayabusa_1210.jpg',
            '433': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/433eros.jpg/400px-433eros.jpg',
            '4179': 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/96/4179_Toutatis_%28Goldstone_radar%29.jpg/400px-4179_Toutatis_%28Goldstone_radar%29.jpg',
            '4': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cc/Vesta_in_natural_color.jpg/400px-Vesta_in_natural_color.jpg',
            '1': 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/76/Ceres_-_RC3_-_Haulani_Crater_%2822381131691%29_%28cropped%29.jpg/400px-Ceres_-_RC3_-_Haulani_Crater_%2822381131691%29_%28cropped%29.jpg',
            'HALLEY': 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/2a/Lspn_comet_halley.jpg/400px-Lspn_comet_halley.jpg',
            'HALE_BOPP': 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Comet-Hale-Bopp-29-03-1997_hires_adj.jpg/400px-Comet-Hale-Bopp-29-03-1997_hires_adj.jpg',
            'NEOWISE': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/Comet_NEOWISE_%28C-2020_F3%29.jpg/400px-Comet_NEOWISE_%28C-2020_F3%29.jpg',
            'TUNGUSKA': 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Tunguska_event_fallen_trees.jpg/400px-Tunguska_event_fallen_trees.jpg',
            'CHELYABINSK': 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/Chelyabinsk_meteor_trace_15-02-2013.jpg/400px-Chelyabinsk_meteor_trace_15-02-2013.jpg',
            '16': 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f9/16_Psyche_VLT_%282021%29.png/400px-16_Psyche_VLT_%282021%29.png',
            '2': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c8/Pallas_Hubble.jpg/400px-Pallas_Hubble.jpg',
            '65803': 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/6c/Didymos_and_Dimorphos.jpg/400px-Didymos_and_Dimorphos.jpg',
            'OUMUAMUA': 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/1c/Artist%27s_impression_of_%CA%BBOumuamua.jpg/400px-Artist%27s_impression_of_%CA%BBOumuamua.jpg',
            '1566': 'https://images.unsplash.com/photo-1446776653964-20c1d3a81b06?w=400&h=300&fit=crop&q=80',
            '3200': 'https://images.unsplash.com/photo-1502134249126-9f3755a50d78?w=400&h=300&fit=crop&q=80',
            '1950DA': 'https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=400&h=300&fit=crop&q=80'
        }

        # Create images directory if it doesn't exist
        images_dir = os.path.join(settings.BASE_DIR, 'static', 'images', 'asteroids')
        os.makedirs(images_dir, exist_ok=True)

        self.stdout.write(self.style.SUCCESS(f'Downloading {len(asteroid_images)} asteroid images...'))

        for asteroid_id, url in asteroid_images.items():
            try:
                # Get file extension from URL
                if 'jpg' in url or 'jpeg' in url:
                    ext = '.jpg'
                elif 'png' in url:
                    ext = '.png'
                else:
                    ext = '.jpg'

                filename = f'{asteroid_id}{ext}'
                filepath = os.path.join(images_dir, filename)

                # Skip if file already exists
                if os.path.exists(filepath):
                    self.stdout.write(f'Skipping {filename} (already exists)')
                    continue

                # Download image
                response = requests.get(url, timeout=10)
                response.raise_for_status()

                # Save image
                with open(filepath, 'wb') as f:
                    f.write(response.content)

                self.stdout.write(self.style.SUCCESS(f'Downloaded {filename}'))

            except Exception as e:
                self.stdout.write(self.style.ERROR(f'Failed to download {asteroid_id}: {str(e)}'))

        self.stdout.write(self.style.SUCCESS('Image download complete!'))