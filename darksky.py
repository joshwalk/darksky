import requests
import json
from datetime import datetime as dt

base_url = "https://api.darksky.net/forecast/"
api_key = '96a95172439d74821eb774abe9a6759b'
lat_lng = '42.280841,-83.738115'
full_url = base_url+api_key+'/'+lat_lng

response = requests.get(full_url)
data = json.loads(response.text)
hourly = data['hourly']['data']
# print(json.dumps(hourly, indent=4))

for hour in hourly:
    time = hour['time']
    summary = hour['summary']
    temp = hour['temperature']
    print(dt.fromtimestamp(time), "\t",summary, "\t\t\t", temp)
