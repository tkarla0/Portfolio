import urllib.request
import json

#Get the weather  temperature below the ISS and convert the  temp to celsius 
def weather_iis(long,lat):
  latt = str(lat)
  longg = str(long)
  url = "https://api.openweathermap.org/data/2.5/weather?lat="+latt+"&lon="+ longg + "&appid=20b1306b8a5b83d500b719a956ba00c0"
  response = urllib.request.urlopen(url)
  result = json.loads(response.read())
  current_weather = result["main"]["temp"]
  cel_temp = current_weather - 273.15 
  return round(cel_temp,1)

