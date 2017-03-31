import json
import requests
import datetime
import time
name = "KSU"
user_apiid = ''
zipcode = '30360'
#user_apiid = 'ddbfcc8c94446f1c49335ca393a33509'

url = 'http://api.openweathermap.org/data/2.5/forecast?zip='+zipcode+'&units=imperial&appid='+user_apiid
url.replace(' ', '')
r = requests.get(url)
r = json.loads(r.text)
print(r)
print ("Name: " + name)
print ("Current Temperature: ",r['list'][1]['main']['temp'])
print ("Atmospheric Pressure: ", r['list'][1]['main']['pressure'])
print ("Wind Speed: ", r['list'][1]['wind']['speed'], "mph")
print ("Wind Direction: ", r['list'][1]['wind']['deg'])
ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
print("Time of Report: "+ st)
input("\n\n\nPress enter to quit")


