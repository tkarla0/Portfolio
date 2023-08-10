from flask import Flask, render_template
from iss_location import iss_coordinates, distance
from open_weather import weather_iis
from country_decoder import country_location,country_info
app = Flask('app')


@app.route('/')
def home():
  cords = iss_coordinates() #Get ISS Location 
  long = cords[1]
  lat = cords[0]
  distance_total = distance(long,lat) #Get Distance Between ISS and current location
  temp = weather_iis(long,lat) #Get weather temp below ISS
  c_code = country_location(long,lat) #Get country below ISS
  #Get country info If the ISS isn't above water
  if c_code != "Over Water":
    country_intel = country_info(c_code)
    country = country_intel["name"]
    image = country_intel["image_scr"]
    currency=country_intel["currency"]
    region_sub = country_intel["regionAndSub"]
    capital = country_intel["capital"]
    language = country_intel["languages"]
  else:
    image = 'static/images/ocean.jpg'
    country="Not applicable, Over the ocean"
    currency=""
    region_sub = ""
    capital = ""
    language = ""
  print (image)
  return render_template("index.html", title = "Space Location",long = long , lat = lat , country = country,c_code=c_code ,spaceWeather=temp,distance_total=distance_total,image=image , region_sub = region_sub , capital = capital, language = language , currency = currency )


app.run(host='0.0.0.0', port=8080)
