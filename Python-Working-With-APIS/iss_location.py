import urllib.request
import json
import haversine as hs   
from haversine import Unit

#Get ISS Current Location
def iss_coordinates():
    url = "http://api.open-notify.org/iss-now.json"
    request = urllib.request.urlopen(url)
    result = json.loads(request.read())
    lat = result['iss_position']['latitude']
    long = result['iss_position']['longitude']
    return lat, long

#Determine the location between ISS And St.Catharines ON
def distance(long,lat):
  #location 525 Welland Ave St.Catharines Ontario
  loc1 = (float(lat),float(long))
  loc2 = (float(43.17723387761392), float(-79.21224540269105))
  result=hs.haversine(loc1,loc2,unit=Unit.KILOMETERS)
  return round(result,2)