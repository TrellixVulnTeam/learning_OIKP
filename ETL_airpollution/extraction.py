import pandas as pd
import requests
import json
from collections import defaultdict
import datetime



def weather_extract() -> pd.DataFrame():
    key = json.loads(open("C:\data\key.json","r").read())
    KEY = key['weather']
    LAT = 37.44
    LON = 126.766

    #handling timedelta, unixtime(timestamp)
    today = datetime.datetime.now()
    yesterday = today - datetime.timedelta(days=365)
    unix_time_yesterday = int(yesterday.timestamp())
    unix_time_today = int(today.timestamp())

    #request
    url = f"http://api.openweathermap.org/data/2.5/air_pollution/history?lat={LAT}&lon={LON}&start={unix_time_yesterday}&end={unix_time_today}&appid={KEY}"
    response = requests.get(url)

    a = response.json()

    #to convert them to pandas.DataFrame later, I used defaultdict(list)
    hash = defaultdict(list)

    #Extraction!
    for i in a['list']:
        hash["observation_location"].append([a['coord']['lat'], a['coord']['lon']])
        hash["time"].append(datetime.datetime.fromtimestamp(i['dt']).strftime('%Y-%m-%d %H:%M:%S'))
        hash["pm2_5"].append(i['components']['pm2_5'])
        hash["pm10"].append(i['components']['pm10'])
        hash["ozone"].append(i['components']['o3'])
    df = pd.DataFrame(hash)
    return df



if __name__ == '__main__':
   print(weather_extract())