# from Kw import Kw


def search_matches():
    
    matches = []
    places = dict()

    local_places = [["res1", "ad", "http"], ["res2", "ad1", "http1"]]
    places[1] = list()
    for place in local_places:
        places[1].append(place[0])
    
    return places


print(search_matches())