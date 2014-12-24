# -*- encoding=utf-8 -*-
#__author__ = 'Zhong.zy'

import sys
#sys.path.append('../utils')

import json
from utils.avos_manager import *
from utils.util_opt import *

class Motion(object):
	def __init__(self):
		self.avos = AvosManager()

	def save(self,device_id,developer_id,motion):
		user = dict(__type='Pointer',className='_User',objectId=developer_id)
		dataDict={'device_id':device_id,'developer':user,'type':motion['type'],'time':motion['time']}
		res = self.avos.saveData('Motion',dataDict)
		return res

