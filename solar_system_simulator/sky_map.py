from astropy.coordinates import AltAz, get_sun, get_body, solar_system_ephemeris
from astropy import units as u
from datetime import datetime
import matplotlib.pyplot as plt
from astropy.coordinates import EarthLocation
from astropy.time import Time


# Function to plot the sky map for the given observer's latitude and longitude
def plot_sky_map(lat, lon):
    observer_location = EarthLocation.of_site('greenwich')  # Placeholder, you can update for specific location

    # Current time (this can be adjusted as needed)
    current_time = Time(datetime.utcnow())

    # Using get_body to get the moon's position instead of get_moon
    moon = get_body('moon', current_time)
    sun = get_sun(current_time)

    # Coordinates for the sky map
    altaz_frame = AltAz(obstime=current_time, location=observer_location)
    moon_altaz = moon.transform_to(altaz_frame)
    sun_altaz = sun.transform_to(altaz_frame)

    # Plotting the sky map
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    ax.plot(moon_altaz.az, moon_altaz.alt, 'bo', label="Moon")
    ax.plot(sun_altaz.az, sun_altaz.alt, 'yo', label="Sun")

    ax.set_title('Sky Map')
    ax.set_xlabel('Azimuth (degrees)')
    ax.set_ylabel('Altitude (degrees)')
    ax.legend()
    plt.show()
