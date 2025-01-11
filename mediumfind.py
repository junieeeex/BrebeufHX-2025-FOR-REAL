#this is all like directtly copy pasted from medium
import requests
def get_place_info(address, api_key):
# Base URL
  base_url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json"
# Parameters in a dictionary
  params = {
   "input": address,
   "inputtype": "textquery",
   "fields": "formatted_address,name,business_status,place_id",
   "key": api_key,
  }
# Send request and capture response
  response = requests.get(base_url, params=params)
# Check if the request was successful
  if response.status_code == 200:
    return response.json()
  else:
    return None
  

api_key = "AIzaSyB8N3cgIEi8Ww2igo5I_uY9ikn9YocvNKk"
address = "500 Bd Dollard, Outremont, QC H2V 3G2"
place_info = get_place_info(address, api_key)
if place_info is not None:
  print(place_info)
else:
  print("Failed to get a response from Google Places API")