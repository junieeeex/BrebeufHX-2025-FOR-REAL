import requests
import json
import time
class GooglePlaces(object):
    def __init__(self, apiKey):
        super(GooglePlaces, self).__init__()
        self.apiKey = apiKey
 
    def search_places_by_coordinate(self, location, radius, keyword):
        endpoint_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
        places = []
        params = {
            'location': location,
            'radius': radius,
            'keyword': keyword,
            'key': self.apiKey
        }
        res = requests.get(endpoint_url, params = params)
        results =  json.loads(res.content)
        places.extend(results['results'])
        time.sleep(2)
        while "next_page_token" in results:
            params['pagetoken'] = results['next_page_token'],
            res = requests.get(endpoint_url, params = params)
            results = json.loads(res.content)
            places.extend(results['results'])
            time.sleep(2)
        return places
 
    def get_place_details(self, place_id, fields):
        endpoint_url = "https://maps.googleapis.com/maps/api/place/details/json"
        params = {
            'placeid': place_id,
            'fields': ",".join(fields),
            'key': self.apiKey
        }
        res = requests.get(endpoint_url, params = params)
        place_details =  json.loads(res.content)
        return place_details
    
    def get_local_places(self, coordinates, radius, keyword):
        places = self.search_places_by_coordinate(coordinates, radius, keyword)

        fields=['name','formatted_address', 'url']

        international_chains = [
            "McDonald's",
            "Burger King",
            "KFC",
            "Subway",
            "Starbucks",
            "Domino's Pizza",
            "Pizza Hut",
            "Taco Bell",
            "Dunkin' Donuts",
            "Popeyes",
            "Wendy's",
            "Tim Hortons",
            "Five Guys",
            "Chipotle Mexican Grill",
            "A&W",
            "Hard Rock Cafe",
            "Denny's",
            "Pret A Manger",
            "HOOTERS"
        ]
        local_places = []
        for place in places:
            details=api.get_place_details(place['place_id'],fields)
            try:
                name = details['result']['name']
                if(name in international_chains):
                    continue
            except KeyError:
                name = ""

            try:
                address = details['result']['formatted_address']
            except KeyError:
                address = ""

            try:
                url = details['result']['url']
            except KeyError:
                url = ""

            local_places.append([name, address, url])


        return local_places






api=GooglePlaces('AIzaSyB8N3cgIEi8Ww2igo5I_uY9ikn9YocvNKk')
coordinates = "45.5016286, -73.6235556"
radius = "500"
keyword = "cafe"

    
local_places = api.get_local_places(coordinates, radius, keyword)

for place in local_places:

    print("Name:", place[0])
    print("Address:", place[1])
    print("Url:", place[2])