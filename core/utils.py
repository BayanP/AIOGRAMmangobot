from geopy.geocoders import Nominatim

def get_adress(latitude,longitude):
    geolocator = Nominatim(user_agent="myGeocoder")
    location=geolocator.reverse((latitude,longitude))
    return location.adress