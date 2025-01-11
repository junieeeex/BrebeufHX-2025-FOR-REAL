kws = set() # TODO hard code all types
matching_kws = set()

class Kw:
    def __init__(self, name):
        self.name = name
        self.count = 0
        

    def __str__(self):
        return f"{self.name} : {self.count}"
    
    def add_count(self):
        self.count += 1
        return self.count

    def remove_count(self):
        self.count -= 1

    def get_count(self):
        return self.count
    
    @staticmethod
    def add_count_by_name(kw_name):
        for kw in kws:
            if(kw == kw_name):
                if kw.add_count() >= 3:
                    matching_kws.add(kw)
                    return
            
        kws.add(Kw(kw_name))

    @staticmethod
    def get_matches():
        return matching_kws
    
    
    def __eq__(self, other):
        if self.name == other:
            return True
        
        if not isinstance(other, Kw):
            return False
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)
    
matching_kws.add(Kw("cafe"))
matching_kws.add(Kw("restaurant"))
from GooglePlaces import GooglePlaces

api=GooglePlaces('AIzaSyB8N3cgIEi8Ww2igo5I_uY9ikn9YocvNKk')
coordinates = "45.5016286, -73.6235556"
radius = "400"
def search_matches():
    
    matches = Kw.get_matches()
    places = dict()
    for kw in matches:
        local_places = api.get_local_places(coordinates, radius, kw)
        places[kw] = list()
        for place in local_places:
            places[kw].append(place[0])
    
    return places

places = search_matches()
for key in places:
    print(str(key) + ": " + places[key])
