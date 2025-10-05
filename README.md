# MeteorMatix - Asteroid Impact Visualization

A Django-based web application for visualizing asteroid data and simulating impact effects.

## Features

- **Dashboard**: Overview of asteroid data with statistics
- **Asteroid Database**: Browse and search asteroid information
- **Impact Simulation**: Calculate impact effects based on asteroid parameters
- **3D Visualization**: Interactive asteroid orbit visualization (coming soon)
- **Educational Content**: Learn about asteroid science and impact effects

## Quick Start

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run Migrations**:
   ```bash
   python manage.py migrate
   ```

3. **Populate Sample Data**:
   ```bash
   python manage.py populate_sample_data
   ```

4. **Start Server**:
   ```bash
   python manage.py runserver
   ```

5. **Access Application**:
   Open http://127.0.0.1:8000 in your browser

## Optional: Fetch Real NASA Data

To fetch real asteroid data from NASA's API:

```bash
python manage.py fetch_nasa_data
```

Note: This requires an internet connection and may take some time.

## Navigation

- **🌍 Dashboard**: Main overview with statistics
- **☄️ Asteroids**: Browse asteroid database
- **💥 Simulation**: Impact effect calculator
- **🎯 Visualizer**: 3D visualization (placeholder)
- **📚 Education**: Learning resources

## Technology Stack

- **Backend**: Django 4.2.7
- **Frontend**: HTML5, CSS3, JavaScript, Tailwind CSS
- **Database**: SQLite
- **APIs**: NASA Near-Earth Object API
- **Visualization**: Chart.js (Three.js planned)

## Sample Data

The application comes with sample asteroid data including:
- Apophis
- Bennu
- Ryugu
- Itokawa
- Eros

Each asteroid includes close approach data and orbital information.

## Future Enhancements

- Real-time 3D Earth visualization with Three.js
- Interactive orbital mechanics simulation
- Advanced impact modeling
- Real-time NASA API integration
- Mobile responsive design improvements
- User accounts and saved simulations

## API Endpoints

- `/api/neo-data/` - Get asteroid data (JSON)
- `/simulation/calculate/` - Calculate impact effects

## Development

The application is designed for educational and demonstration purposes. The impact calculations use simplified physics models for illustration.

For production use, consider:
- Adding proper error handling
- Implementing caching for API calls
- Adding user authentication
- Optimizing database queries
- Adding comprehensive testing