import requests

def get_amenities_Data(ll, query):
    url = "https://api.foursquare.com/v3/places/search?"
    amenities_count = {}

    url += 'query='+query+'&ll='+ll+'&fields=fsq_id%2Cname%2Ccategories%2Clocation%2Cgeocodes&limit=20'

    headers = {
            "accept": "application/json",
            "Authorization": "fsq3FwL8o3am2Zw//dg/GKQuZqXk/CDiPaHhjbB0VP/TCcw="
        }

    response = requests.get(url, headers=headers)
    data = response.json()

    if len(data['results']) == 0:
            print('No ',query,' near:',ll)
            amenities_count[query]=None
            return amenities_count
        
    if query == 'Juice':
            jcount = len(data['results'])
            amenities_count[query]=jcount
            
    if query == 'coffee':
            ccount = len(data['results'])
            amenities_count[query]=ccount
            
    if query == 'gym':
            gcount = len(data['results'])
            amenities_count[query]=gcount
            
    if query == 'cafe':
            cfcount = len(data['results'])
            amenities_count[query]=cfcount
            
    return amenities_count


def get_residence_data(residence,query):
    amenities = []
    for j,k in residence.iterrows():
        lat = k['latitude']
        long = k['longitude']
        ll = str(lat)+','+str(long)
        record = []
        for i in query:
            amenities_data = get_amenities_Data(ll, i)
            record.append(amenities_data)
        amenities.append(record)
    return amenities