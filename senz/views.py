from django.http.response import HttpResponse
from poiGenerator import PoiGenerator

# Create your views here.
def index(request):
	res = ''
	for param,value in request.GET.items():
		res += "%s = %s, " % (param,value)
	return HttpResponse("senz Index View: <br>"+res[:-2])

def get_poi(request):
	poi = PoiGenerator()
	username,lat,lng = request.GET['username'], request.GET['lat'],request.GET['lng']
	pois = poi.getPoiGroupByGps(username,int(lat),int(lng))
	res = ''
	for poi in pois:
		res += poi+' '
	return HttpResponse(res)

