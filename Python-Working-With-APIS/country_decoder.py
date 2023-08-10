import urllib.request
import json

#Get the country code of the country the ISS is above
def country_location(long,lat):
  latt = str(lat)
  longg = str(long)
  url = "https://www.mapquestapi.com/geocoding/v1/reverse?key=hNKX3cZKEJu8OEbTi12zDgvnknQiKE7x&location="+ latt + ","+ longg + "&outFormat=json&thumbMaps=false"
  response = urllib.request.urlopen(url)
  result = json.loads(response.read())
  c_name=result["results"][0]["locations"][0]["adminArea1"]
  print (c_name)
  if not c_name:
    country= "Over Water"
  else:
    country = c_name
  return country


#Get information about the country below the ISS
def country_info(c_code):
  url = "https://restcountries.com/v3.1/alpha/"+ c_code
  response = urllib.request.urlopen(url)
  result = json.loads(response.read())
  print (result[0]["flags"]["png"])
  img_scr = result[0]["flags"]["png"]
  country_name = result[0]["name"]["common"]
  capital = result[0]["capital"][0]
  locale = result[0]["subregion"] + "," + result[0]["region"]
  lang_dict =  result[0]["languages"]
  curr_dict = result[0]["currencies"]
  languages = ""
  currencies = ""
  for value in lang_dict.values():
    languages = languages +  value + ", "

  for value in curr_dict.values():
    currencies = currencies + value["name"] + ", "
  
  country_intel = {
    "name" : country_name,
    "capital" : capital,
    "regionAndSub" : locale,
    "languages" : languages[:-2],
    "image_scr": img_scr,
    "currency" : currencies[:-2]
  }
  return country_intel