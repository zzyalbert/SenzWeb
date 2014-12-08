# -*- encoding=utf-8 -*-

from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from poiGenerator import PoiGenerator
from motion import Motion
from poi import PoiGet

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

@csrf_exempt
def get_senz(request):
	param = json.loads(request.POST['param'])
	device_id = param['device_id']
	developer_id = param['developer_id']
	location = param['location']
	beacon = ''
	if 'beacon' in param.keys():
		beacon = param['beacon']
	poi = PoiGet().get(device_id,developer_id,location,beacon)
	result = json.dumps(dict(POI=poi,TOI=''),ensure_ascii=False)
	return HttpResponse(result)

@csrf_exempt
def motion(request):
	param = json.loads(request.POST['param'])
	device_id = param['device_id']
	developer_id = param['developer_id']
	motion = param['motion']
	res = Motion().save(device_id, developer_id, motion)
	return HttpResponse(res)

@csrf_exempt
def static_info(request):
	param = json.loads(request.POST['param'])
	device_id = param['device_id']
	developer_id = param['developer_id']
	device_info = param['device_info']
	app_list = param['app_list']
	return HttpResponse('')



