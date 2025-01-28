from astropy.time import Time
from astropy.coordinates import EarthLocation
import astropy.units as u

def get_current_time():
    """Returns the current time in UTC."""
    return Time.now()

def get_observer_location(lat, lon, height=0):
    """Returns the EarthLocation for a given latitude, longitude, and height (in meters)."""
    return EarthLocation.of_site('greenwich')  # Change to specific location if needed
    # Example: EarthLocation.from_geodetic(lon, lat, height)
