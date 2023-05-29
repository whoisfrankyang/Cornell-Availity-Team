import requests
from bs4 import BeautifulSoup
import numpy 
import pandas

def get_locations(first, last):
    """
    Returns a list of addresses for a given provider with first and last name as parameters
    Limits search for providers in New York with a speciality in Pediatric Orthopedic Surgery
    """

    search = first+ "+" +last + "+Pediatric+Orthopedic+Surgery+New+York+Healthgrades&oq=Friedrich+Boettner+Pediatric+Orthopedic+Surgery+New+York+Healthgrades"
    url = 'https://www.google.com/search'

    headers = {
        'Accept' : '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82',
    }
    parameters = {'q': search}

    content = requests.get(url, headers = headers, params = parameters).text
    soup = BeautifulSoup(content, 'html.parser')

    search = soup.find(id = 'search')
    first_link = search.find('a')

    #print(first_link['href'])

    #get text content from a specific div
    response = requests.get(first_link['href'])
    soup = BeautifulSoup(response.content, 'html.parser')
    divs = soup.find_all('div', class_='office-title')

    addresses = []
    for i in divs:
        #find all span tags in the div
        span = i.find_all('span')
        address = [''.join(i.text) for i in span]
        addresses.append(address)

    return addresses


print(get_locations("Friedrich", "Boettner"))