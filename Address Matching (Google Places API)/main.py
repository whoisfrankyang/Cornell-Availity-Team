import googlemaps
from datetime import datetime
import requests

"""
A function to convert an address into geolocation (longtitude and latitude) using google places API. You need to create YOUR OWN api key from google praces api"

This function is to use for address comparison. For the same address from different data sets, they might have slightly different formats, spaces, names, capitalization, etc. Thus, we use the google API to find the altitude and latitude given an address in String. If two addresses has the same geolocation within a certain thresholds (few decimal places). Then they are the same address.

"""


def geocode(api_key, address):
    url = "https://maps.googleapis.com/maps/api/geocode/json"
    params = {
        "address": address,
        "key": api_key,
    }

    response = requests.get(url, params=params)
    return response.json()


api_key = "YOUR OWN API KEYS"
location1 = "'5 E 98TH ST, NEW YORK, NY, 10029"
location2 = "5 E 98th St Fl 9, New York, NY, 10029"
location3 = "14 Technology Dr Ste 12, East Setauket, NY, 11733"

geolocation1 = geocode(api_key, location1)
geolocation2 = geocode(api_key, location2)
geolocation3 = geocode(api_key, location3)

latitude1 = round(geolocation1['results'][0]['geometry']['location']['lat'], 3)
longtitude1 = round(geolocation1['results'][0]
                    ['geometry']['location']['lng'], 3)

latitude2 = round(geolocation2['results'][0]['geometry']['location']['lat'], 3)
longtitude2 = round(geolocation2['results'][0]
                    ['geometry']['location']['lng'], 3)

latitude3 = round(geolocation3['results'][0]['geometry']['location']['lat'], 3)
longtitude3 = round(geolocation3['results'][0]
                    ['geometry']['location']['lng'], 3)

print("Location 1 and location 2 are the same address: " +
      str((longtitude1 == longtitude2 and latitude1 == latitude2)))
print("Location 1 and location 3 are the same address: " +
      str((longtitude1 == longtitude3 and latitude1 == latitude3)))



