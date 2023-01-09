import requests
import pandas as pd

def getData(ll,query):
    url = "https://api.foursquare.com/v3/places/search?"
    if ll != '':
        url += 'query='+query+'&ll='+ll+'&fields=fsq_id%2Cname%2Ccategories%2Clocation%2Cgeocodes&limit=20'
    else:
        url += 'query='+query+'&fields=fsq_id%2Cname%2Ccategories%2Clocation%2Cgeocodes&limit=20'

    headers = {
        "accept": "application/json",
        "Authorization": "fsq3FwL8o3am2Zw//dg/GKQuZqXk/CDiPaHhjbB0VP/TCcw="
    }

    response = requests.get(url, headers=headers)
    data = response.json()
    if len(data['results']) == 0:
        print('No data found for ',query)
        return None
    geolocation_data2 = []
    for i in range(len(data['results'])):
        cur = data['results'][i]
        changed_cur = {}
        for m,n in cur.items():
            if m == 'location':
                for x,y in n.items():
                    if x == 'address'or x=='country'or x=='cross_street'or x=='locality':
                        changed_cur[x]=y
                    else:
                        continue
            elif m == 'geocodes':
                for a,b in n.items():
                    if a == 'main':
                        coordinates = n['main']
                        lat = coordinates['latitude']
                        long = coordinates['longitude']
                        changed_cur['latitude'] = lat
                        changed_cur['longitude'] = long
                    else:
                        continue
            else:
                changed_cur[m] = n
        geolocation_data2.append(changed_cur)
    df = pd.DataFrame(geolocation_data2)
    df = cleancategories(df)
    return df
    
def cleancategories(df):
    id = []
    category = []
    for i in df.categories:
        if i != []:
            id.append((str(i).split(',',1))[0])
            category.append((str(i).split(',',2))[1])
            
    id1 = []
    category1 = []
    for j in id:
        num = ''
        for k in j:
            if k.isdigit():
                num += k
        id1.append(num)
    for l in category:
        category1.append((l.split(':'))[1].strip())
    df.insert(2, "ID", pd.Series(id1), True)
    df.insert(3, "Category", pd.Series(category1), True)
    df.drop(['categories'], axis=1, inplace=True)
    return df