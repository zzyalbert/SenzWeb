# -*- encoding=utf-8 -*-
#__author__ = 'Zhong.zy'

import sys
#sys.path.append('../utils')
from datetime import *
import json
from utils.avos_manager import *
from utils.util_opt import *

class ToiGet(object):
	def __init__(self):
		self.avos = AvosManager()

	def get(self,timestamp):
		time = datetime.datetime.fromtimestamp(int(timestamp))
		hour = time.timetuple().tm_hour
		mon = time.timetuple().tm_mon
		day = time.timetuple().tm_mday
		return {'when':self.getWhen(hour),'while':self.getWhile(mon,day)}

	def getWhen(self,hour):
		if hour>=6 and hour<8:
			return 'breakfest'
		elif hour>=8 and hour<11:
			return 'morning activity'
		elif hour>=11 and hour<13:
			return 'lunch'
		elif hour>=13 and hour<18:
			return 'afternoon activity'
		elif hour>=18 and hour<20:
			return 'supper'
		elif hour>=20 and hour<22:
			return 'evening activity'
		elif hour>=22 or hour<6:
			return 'sleep'

	def getWhile(self,month,day):
		return 'nothing'






if __name__ == '__main__':
	print PoiGet().get(39.983424,116.322987)
