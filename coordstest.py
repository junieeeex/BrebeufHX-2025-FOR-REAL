import googlemaps
import requests

apiKey="AIzaSyB8N3cgIEi8Ww2igo5I_uY9ikn9YocvNKk"

#if i get an error in this section it could be because i enabled the geocoding api after i had already created the key
#also i removed the accents from that address cuase theyve caused problems before but that could make it invalid idk
userLocation='3200 Chem. de la Côte-Sainte-Catherine, Montréal, QC H3T 1C1'

def extract_coords(address,key):
    lat, lng = None, None
    api_key = key
    base_url = "https://maps.googleapis.com/maps/api/geocode/json"
    endpoint = base_url + "?address=" + address + "&key=" + api_key
<<<<<<< HEAD
=======

>>>>>>> fb95b09c98ac3bf7f9b3a246d7f42f029ab78dc8
    # see how our endpoint includes our API key? Yes this is yet another reason to restrict the key
    r = requests.get(endpoint)
    if r.status_code not in range(200, 299):
        return None, None
    try:
        '''
        This try block incase any of our inputs are invalid. This is done instead
        of actually writing out handlers for all kinds of responses.
        '''
        #lowkey i dont know what this is doing
        results = r.json()['results'][0]
        lat = results['geometry']['location']['lat']
        lng = results['geometry']['location']['lng']
    except:
        pass
    return (lat,lng)

print(extract_coords(userLocation, apiKey))