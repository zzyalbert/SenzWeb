# -*- encoding=utf-8 -*-
#__author__ = 'Zhong.zy'

import sys
#sys.path.append('../utils')

import json
from utils.avos_manager import *
from utils.util_opt import *
from utils.geo_coding import GeoCoder

class PoiGet(object):
	def __init__(self):
		self.avos = AvosManager()

	def getPoi(self,lat,lng):
		geo = GeoCoder()
		return geo.getPOI(lat,lng)
	
	def get(self,device_id,developer_id,location,beacon):
		user = dict(__type='Pointer',className='_User',objectId=developer_id)
		lat,lng = float(location['latitude']),float(location['longitude'])
		if beacon:
			lat,lng = self.getLocation(beacon)
		gps = dict(__type='GeoPoint',latitude=lat,longitude=lng)
		dataDict={"device_id":device_id,"developer":user,"accuracy":location['accuracy'],"time":location['time'],"gps":gps,"speed":location['speed']}
		self.avos.saveData('Location',dataDict)
		poi = self.getPoi(lat,lng)
		return dict(at=poi)

	def getLocation(self,beacon):
		return 0,0			
				
				

if __name__ == '__main__':
	print PoiGet().getPoi(40.056885091681,116.30814954222)
