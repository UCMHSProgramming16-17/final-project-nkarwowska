import requests
import pandas as pd


latlist = []
templist = []

endpoint = 'https://api.darksky.net/forecast/'
key = '6da8db3cdfa7641b1c696c20fe2c82bf'

for x in range(-90,90,10):
    lat = str(x)
    lon = '-122.4233'
    url = endpoint + key + '/' + lat + ',' + lon 
    payload = {'lang': 'x-pig-latin'}
    r = requests.get(url, params=payload)
    weather = r.json()

    temperature = weather['currently']['temperature']

    latlist.append(int(lat))
    templist.append(temperature)
    
df = pd.DataFrame({
    'Latitude' : latlist,
    'Temperature' : templist
})

from bokeh.charts import Bar, output_file, save

p = Bar(df, 'Latitude', 'Temperature', title= 'Temperature for Latitude', legend=False)
output_file('Bar.html')
save(p)