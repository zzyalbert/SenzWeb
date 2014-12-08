# -*- encoding=utf-8 -*-
#__author__ = 'Zhong.zy'

import sys
#sys.path.append('../utils')

import json
from avos_manager import *
from util_opt import *
from geo_coding import GeoCoder

class PoiGet(object):
        def __init__(self):
                self.avos = AvosManager()

        def get(self,lat,lng):
                geo = GeoCoder()
                return geo.getPOI(lat,lng)

        
     
                        

if __name__ == '__main__':
        print PoiGet().get(39.983424,116.322987)
