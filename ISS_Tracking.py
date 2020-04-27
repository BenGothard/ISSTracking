import requests
from geopy.geocoders import Nominatim

iss_loc = requests.get("http://api.open-notify.org/iss-now.json")
iss_coordinates = iss_loc.json()['iss_position']
iss_lat = float(iss_coordinates['latitude'])
iss_lon = float(iss_coordinates['longitude'])
geolocator = Nominatim(user_agent="ISS_Tracking.py")
location = geolocator.reverse(f"{iss_lat}, {iss_lon}")
print(f"The ISS is currently at {location.address} - {iss_coordinates} to be precise - but won't be there for long!")


