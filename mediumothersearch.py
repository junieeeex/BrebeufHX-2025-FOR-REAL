#copied from that same medium article but this is search which is like slightly different
#search returnss the address
#couldnt find this on the pricing sheet so idk that seem sketch

import googlemaps

# client object
client = googlemaps.Client(key = "AIzaSyB8N3cgIEi8Ww2igo5I_uY9ikn9YocvNKk")

# area within 500 m of The White House
lat =  38.897957, 
lon = -77.036560, # lat lon of The White House
radius = 500 # radius in meters
token = None # page token for going to next page of search

# method 1
desirable_places = client.places(query = 'coffee')

# or use way # method 2
place_type = 'cafe'
desirable_places = client.places(type = place_type)

# token for searching next page; to be used in a loop
token = desirable_places['next_page_token'] 

print(len(desirable_places))

#once again output was 20 originally but again who knows