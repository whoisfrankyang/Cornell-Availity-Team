
import googlemaps
from datetime import datetime
import requests

"""
A function to convert an address into geolocation (altitutde and latitude) using google places API. You need to create YOUR OWN api key from google praces api"

This function is to use for address comparison. For the same address from different data sets, they might have slightly different formats, spaces, names, capitalization, etc. Thus, we use the google API to find the altitude and latitude given an address in String. If two addresses has the same geolocation within a certain thresholds (few decimal places). Then they are the same address.

Note: the result from this contains many other informations. Need further string processing to extract the useful geolocation.
"""

def geocode(api_key, address):
    url = "https://maps.googleapis.com/maps/api/geocode/json"
    params = {
        "address": address,
        "key": api_key,
    }
    
    response = requests.get(url, params=params)
    return response.json()
    
api_key = "//your api key"
location1 = "'5 E 98TH ST, NEW YORK, NY, 10029"
location2 = "5 E 98th St Fl 9, New York, NY, 10029"
location3 = "14 Technology Dr Ste 12, East Setauket, NY, 11733"

geolocation1 = geocode(api_key,location1)
geolocation2 = geocode(api_key,location2)
geolocation3 = geocode(api_key, location3)

print(geolocation1["geometry"])


