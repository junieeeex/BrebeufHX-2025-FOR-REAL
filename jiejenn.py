#code copied from jie jenn on youtube, could be useful to troubleshoot

import googlemaps
import pandas as pd
import time

def milesToMeter(miles):
    try:
        return miles*1609.344
    except:
        return 0
    
APIKey='AIzaSyB8N3cgIEi8Ww2igo5I_uY9ikn9YocvNKk'
mapClient=googlemaps.Client(APIKey)

location=(45.520120, -73.584320)
searchString='bagel'
distance=milesToMeter(15),
business_list=[]

response=mapClient.places_nearby(
    Location=location,
    keyword=searchString,
    radius=distance,
)
business_list.extend(response.get('results'))
#might not be necessary to do the next page token if we want to limit calls
next_page_token=response.get('next_page_token')

#while its non null meaning while theres stuff on the next page
while next_page_token:
    #apparenty calling the next page too fast causes duplicate results
    time.sleep(2)
    response=mapClient.places_nearby(
        Location=location,
        keyword=searchString,
        radius=distance,
        page_token=next_page_token
    )
    business_list.extend(response.get('results'))
    next_page_token=response.get('next_page_token')

df=pd.DataFrame(business_list)
df['url']='https://www.google.com/maps/place/?q=place_id:' +df['place_id']
df.to_excel('bagel shop list.xlsx',index=False)

#if this doesnt work once i have all the other shit sorted out im gonna cry
#actally this whole thing mught be obsolete now LOLLLLLL