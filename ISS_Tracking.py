import requests
from geopy.geocoders import Nominatim

iss_loc = requests.get("http://api.open-notify.org/iss-now.json")
iss_coordinates = iss_loc.json()['iss_position']
iss_lat = float(iss_coordinates['latitude'])
iss_lon = float(iss_coordinates['longitude'])
geolocator = Nominatim(user_agent="ISS_Tracking.py")
location = geolocator.reverse(f"{iss_lat}, {iss_lon}")
tell_me_good_news = f"🚀 The ISS is currently at {location.address},\n🗺 {iss_coordinates} to be precise,\n⏳ but won't be there for long!"
tell_me_bad_news = f"🚀 The ISS is currently at a location that has no set address, \n🗺 {iss_coordinates} to be precise,\n⏳ but won't be there for long!"


if location.address is None:
    print(tell_me_bad_news)
else:
    print(tell_me_good_news)

print("\n😊 Thanks for using the ISS Tracker!\n👍 Come back to track the International Space Station again soon!")

print("\n📚 To read more about what the ISS does, I'd encourage you to visit https://www.nasa.gov/mission_pages/station/main/index.html")