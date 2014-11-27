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
	poiGroupName,username = request.GET['poiGroupName'], request.GET['username']
	pois = poi.getPoiGroupMembersByName(poiGroupName,username)
	return HttpResponse(str(pois))

