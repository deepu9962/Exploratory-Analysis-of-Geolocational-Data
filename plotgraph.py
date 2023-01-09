
import folium
import pandas as pd

def get_graph(org):
# importing the dataset as a csv file,
# and storing it as a dataframe in 'df'
    df=pd.read_csv('locations.csv')
    co_ordinates = org.split(',')
    lati = co_ordinates[0]
    long = co_ordinates[1].strip()
    # Creating a map object using Map() function.
    # Location parameter takes latitudes and
    # longitudes as starting location.
    # (Map will be centered at those co-ordinates)
    map5 = folium.Map(location=[lati,long],zoom_start=11)

    # Function to change the marker color
    # according to the clusters
    def color(elev):
        if elev == 0:
            col = 'green'
        elif elev ==1:
            col = 'blue'
        elif elev ==2:
            col = 'orange'
        elif elev ==3:
            col = 'purple'
        elif elev ==4:
            col = 'pink'
        else:
            col='red'
        return col

    # Iterating over the LAT,LON,NAME and
    # ELEV columns simultaneously using zip()
    for lat,lan,name,elev in zip(df['Latitude'],df['Longtude'],df['Name'],df['clusters']):
        # Marker() takes location coordinates
        # as a list as an argument
        folium.Marker(location=[lat,lan],popup=name,icon= folium.Icon(color=color(elev),icon_color='yellow',icon = 'cloud')).add_to(map5)

    # Save the file created above
    folium.Marker(location=[lati, long],popup=[lati, long],icon= folium.Icon(color='lightgray',icon_color='yellow',icon = 'cloud')).add_to(map5)
    map5.save('test7.html')
    return map5