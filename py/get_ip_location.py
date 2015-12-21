#!/usr/bin/env python 
# -*- coding: utf-8 -*-


import json
import urllib2
import re
import sys	

class location_taobao():
    '''
build the mapping of the ip address and its location
the geo info is from Taobao
e.g. http://ip.taobao.com/service/getIpInfo.php?ip=112.111.184.63
The getIpInfo API from Taobao returns a JSON object.
    '''

    def __init__(self,ip):
        self.ip = ip
        self.api_url = 'http://ip.taobao.com/service/getIpInfo.php?ip=%s' % self.ip
   
    def get_geoinfo(self):
        urlobj = urllib2.urlopen(self.api_url)
        data = urlobj.read()
        datadict = json.loads(data,encoding='utf-8')
#        return datadict[u'data']
        print self.ip,datadict[u'data'][u'country'],datadict[u'data']['region'],datadict[u'data']['city'],datadict[u'data']['isp']

'''    def get_country(self):
        key = u'country'
        datadict = self.get_geoinfo()
        return datadict[key]
 
    def get_region(self):
        key = 'region'
        datadict = self.get_geoinfo()
        return datadict[key]
 
    def get_city(self):
        key = 'city'
        datadict = self.get_geoinfo()
        return datadict[key]
 
    def get_isp(self):
        key = 'isp'
        datadict = self.get_geoinfo()
        return datadict[key]
'''

if __name__ == '__main__':
    if len(sys.argv) == 2:
        ip = sys.argv[1]
        iploc = location_taobao(ip)
        iploc.get_geoinfo()
    else:
        print '''
Usage: %s : ipaddress
'''%sys.argv[0]
