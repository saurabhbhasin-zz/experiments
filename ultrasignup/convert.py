# convert.py
import googlemaps
api_key = 'YOUR GOOGLE MAPS API KEY'


def getLat(zipcode):
    gmaps = googlemaps.Client(key=api_key)
    geocode_result = gmaps.geocode(zipcode)
    ll = geocode_result[0]["geometry"]["location"]
    lat = (ll["lat"])
    return lat


def getLng(zipcode):
    gmaps = googlemaps.Client(key=api_key)
    geocode_result = gmaps.geocode(zipcode)
    ll = geocode_result[0]["geometry"]["location"]
    lng = (ll["lng"])
    return lng


def getAddress(zipcode):
    gmaps = googlemaps.Client(key=api_key)
    geocode_result = gmaps.geocode(zipcode)
    address = geocode_result[0]["formatted_address"]
    return address
