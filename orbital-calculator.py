# Calculator used to find basic metrics of an equatorial circular orbit with the input of an orbital height

import math

# Constants
earth_radius = 6378000 # Mean radius at equator in meters
earth_mass = 5.972e24 # kg
G = 6.67e-11 # Gravitational constant


# Get altitude from user
try:
    altitude = float(input("Orbital Altitude (m): "))
    if altitude < 0:
        print("Altitude must be positive")
        exit()
except ValueError:
    print("Please enter a valid number")
    exit()


# Calculate orbital radius
radius = earth_radius + altitude 

# Calculate orbital velocity using vis-viva equation
velocity = ((G * earth_mass) / radius) ** 0.5 # m/s

# Calculate orbital period
period = ((2 * math.pi * radius) / velocity) / 3600 # Hours


# Print metrics
print(f"""
      --- Orbital Metrics at {altitude/1000:.0f}km ---
      
      Orbital Velocity: {velocity:.2f} m/s ({velocity*3.6:.2f} km/h)

      Orbital Period: {period:.1f} hours ({period*60:.1f} minutes)

""")
