from geo_location import *
from locations import *
import matplotlib.pyplot as plt
from plotgraph import *
import time

DataFrames = []
ll = input('Enter the coordinates:\t')
start = time.time()
org_coordinates = ll

ll = ll.replace(" ", "")
query = ['Hostel','PG','Dorm']
for i in query:
    data = getData(ll, i)
    DataFrames.append(data)

residential_data = DataFrames[0]
residence = residential_data.append(DataFrames[1:-1],ignore_index = True)
print(residence)

try:
    query = ['Juice' , 'coffee' , 'gym' , 'cafe']
    amenities = get_residence_data(residence,query)
except Exception as e:
    print(e)
    print('Stopped midway')

amenities_refined = [[[b for a,b in x.items()] for x in i] for i in amenities]

df1 = pd.DataFrame(amenities_refined, columns = ['JUICE_SHOPS', 'COFFEE_SHOPS', 'GYMS', 'CAFE'])

df1.insert(0, "Latitude", residence.latitude, True)
df1.insert(0, "Longtude", residence.longitude, True)

df1.JUICE_SHOPS = [x[0] for x in df1.JUICE_SHOPS]

df1.COFFEE_SHOPS = [x[0] for x in df1.COFFEE_SHOPS]

df1.GYMS = [x[0] for x in df1.GYMS]

df1.CAFE = [x[0] for x in df1.CAFE]

df1 = df1.fillna(0)

print(df1)

from sklearn.cluster import KMeans
locations = df1
Classifier = KMeans(n_clusters=6).fit(locations)
y_pred = Classifier.fit_predict(locations)

plt.scatter(locations['Latitude'], locations['Longtude'], c=y_pred, cmap='rainbow')
plt.title('K-Means Clustering over general population')
plt.ylabel('Longitude')
plt.xlabel('Latitude')
plt.show()


clusters = pd.DataFrame(y_pred)
locations['clusters'] = clusters
locations.insert(0, "Name", pd.Series(residence.name), True)
locations.to_csv('locations.csv',index=False)


map = get_graph(org_coordinates)
end = time.time()
print('Completed in {}'.format(end-start))
