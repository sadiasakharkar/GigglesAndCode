import numpy as np
import matplotlib.pyplot as plt
from astropy.time import Time
from astropy.coordinates import get_body, solar_system_ephemeris
import astropy.units as u
from matplotlib.animation import FuncAnimation
from sky_map import plot_sky_map  # Importing the sky map function

# Function to get and plot orbits of the planets
def plot_orbits():
    times = Time('2025-01-28') + np.linspace(0, 365, 365) * u.day  # One year of data
    planets = ['mercury', 'venus', 'earth', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune']
    plt.figure(figsize=(8, 6))

    for planet in planets:
        pos = get_body(planet, times)
        plt.plot(pos.x, pos.y, label=planet.capitalize())

    plt.xlabel("X (AU)")
    plt.ylabel("Y (AU)")
    plt.title("Planetary Orbits")
    plt.grid(True)
    plt.legend()
    plt.show()

# Interactive Orbit Visualization
def plot_interactive_orbits():
    from ipywidgets import interact
    from astropy.coordinates import get_body
    from astropy.time import Time

    def plot_orbit(planet_name='earth', time_step=365):
        times = Time('2025-01-28') + np.linspace(0, time_step, time_step) * u.day
        pos = get_body(planet_name, times)

        plt.figure(figsize=(8, 6))
        plt.plot(pos.x, pos.y, label=planet_name.capitalize())
        plt.xlabel("X (AU)")
        plt.ylabel("Y (AU)")
        plt.title(f"{planet_name.capitalize()} Orbit")
        plt.grid(True)
        plt.legend()
        plt.show()

    interact(plot_orbit, planet_name=['earth', 'mars', 'jupiter'], time_step=(365, 730, 1))

# Space Missions Visualization (Mars Rover Example)
from astropy.coordinates import CartesianRepresentation

def plot_space_missions():
    # Define the timespan for the simulation (one year of data)
    times = Time('2025-01-28') + np.linspace(0, 365, 365) * u.day
    
    # Get the position of Mars at these times
    mars_pos = get_body('mars', times)

    # Convert the position of Mars to Cartesian coordinates
    mars_pos_cart = mars_pos.cartesian
    
    # Add an offset to the Mars rover's position (0.1 AU offset)
    rover_offset = 0.1 * u.AU
    
    # Manually add the offset to the x and y coordinates
    mars_rover_pos_cart = CartesianRepresentation(
        x=mars_pos_cart.x + rover_offset, 
        y=mars_pos_cart.y + rover_offset, 
        z=mars_pos_cart.z
    )
    
    # Plotting the results
    plt.figure(figsize=(8, 6))
    plt.plot(mars_rover_pos_cart.x, mars_rover_pos_cart.y, label="Mars Rover", color='purple')
    plt.xlabel("X (AU)")
    plt.ylabel("Y (AU)")
    plt.title("Mars Rover Position Relative to Mars")
    plt.grid(True)
    plt.legend()
    plt.show()

# Customizable Time Range for Orbit Visualization
def plot_orbits_with_time_range():
    start_date = input("Enter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")

    times = Time([start_date, end_date])
    planets = ['mercury', 'venus', 'earth', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune']
    
    plt.figure(figsize=(8, 6))

    for planet in planets:
        pos = get_body(planet, times)
        plt.plot(pos.x, pos.y, label=planet.capitalize())

    plt.xlabel("X (AU)")
    plt.ylabel("Y (AU)")
    plt.title("Planetary Orbits with Custom Time Range")
    plt.grid(True)
    plt.legend()
    plt.show()

# Animate Orbits
def animate_orbits():
    times = Time('2025-01-28') + np.linspace(0, 365, 365) * u.day  # One year of data
    planets = ['mercury', 'venus', 'earth', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune']

    fig, ax = plt.subplots(figsize=(8, 6))
    lines = {}
    for planet in planets:
        lines[planet], = ax.plot([], [], label=planet.capitalize())

    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_xlabel("X (AU)")
    ax.set_ylabel("Y (AU)")
    ax.set_title("Orbit Animation")
    ax.grid(True)
    ax.legend()

    def init():
        for line in lines.values():
            line.set_data([], [])
        return list(lines.values())

    def update(frame):
        for planet, line in lines.items():
            pos = get_body(planet, times[frame])
            line.set_data(pos.x, pos.y)
        return list(lines.values())

    ani = FuncAnimation(fig, update, frames=range(len(times)), init_func=init, blit=True)
    plt.show()

# Sky Map Visualization Function
def plot_sky_map_option():
    # Ask user for location (latitude and longitude)
    lat = float(input("Enter observer's latitude: "))
    lon = float(input("Enter observer's longitude: "))
    
    # Call the sky map plotting function
    plot_sky_map(lat, lon)
