from GooglePlaces import GooglePlaces
api=GooglePlaces('AIzaSyB8N3cgIEi8Ww2igo5I_uY9ikn9YocvNKk')


matching_kws = set()

class Kw:
    def __init__(self, name):
        self.name = name
        self.count = 0
        

    def __str__(self):
        return self.name
    
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
                    print("EFUHWEIGFOWNIEYFGNI")
                    matching_kws.add(kw)
                    return True
                
                return False
            
                
        kws.add(Kw(kw_name))
        return False
        

    @staticmethod
    def get_matches():
        return matching_kws
    
    @staticmethod
    def search_matches(coordinates, radius):
        matches = Kw.get_matches()
        restaurants = []
        for kw in matches:
            print("awefa:"+ str(kw))
            local_places = api.get_local_places(coordinates, radius, str(kw))

            restaurants.append(local_places)
        
        return restaurants

    
    
    def __eq__(self, other):
        if self.name == other:
            return True
        
        if not isinstance(other, Kw):
            return False
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)
    

kws_str = set(('american food', 'fried chicken', 'fast food', 'korean food', 'cafe', 'bakery', 'thai food', 'indian food', 'mexican food', 'chinese food', 'japanese food', 'pizza', 'italian food', 'noodles', 'ice cream', 'baked goods'))
kws = set()
for name in kws_str:
    kws.add(Kw(name))

    


coordinates = "45.49426171303169, -73.5794899059468"
radius = "400"


