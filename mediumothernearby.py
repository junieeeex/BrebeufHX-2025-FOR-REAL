#got this code from a medium article,looks pretty simple to try
#apparently this is more expensive but interesting to note it apparently doesnt return address?
#might return a link to google maps tho which could be useful
#this is 32 per 1000 calls which is pricey but at the level wereusing it it might not matter
#upon reflexion im not convinced this code would run

import googlemaps

# client object
client = googlemaps.Client(key = "AIzaSyB8N3cgIEi8Ww2igo5I_uY9ikn9YocvNKk")

# area within 500 m of The White House
lat =  38.897957, 
lon = -77.036560, # lat lon of The White House
radius = 500 # radius in meters
token = None # page token for going to next page of search

# method 1
desirable_places = client.places_nearby(keyword = 'coffee')

# the code beneath is to search by keyword
#place_type = 'cafe'
#desirable_places = client.places_nearby(type = place_type)

# token for searching next page; to be used in a loop
token = desirable_places['next_page_token'] 

print(len(desirable_places))

# at the time the article was written there was 20 places but like who knows