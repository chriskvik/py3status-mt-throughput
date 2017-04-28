# -*- coding: utf-8 -*-
from pysnmp.entity.rfc3413.oneliner import cmdgen 
import time

class Py3status:
	snmp_host = '192.168.1.1'
	snmp_port = 161
	snmp_community = 'public'
	wan_in =  '.1.3.6.1.2.1.31.1.1.1.6.4'
	wan_out = '.1.3.6.1.2.1.31.1.1.1.10.4'
	rate = 'bit' #bit
	acc = 2
	refresh = 2
	threshold = 50

	def __init__(self):
		self.drate = 'Mbps'
		
	def mt_wan(self):
		b = self._get_bytes()
		d1_out= b[0]
		d1_in = b[1]
		
		time.sleep(self.acc)

		b = self._get_bytes()
		d2_out = b[0]
		d2_in =  b[1]
		
		d_out = d2_out - d1_out
		d_in = d2_in - d1_in

		d_in = round(d_in/1024/1024/self.acc)
		d_out = round(d_out/1024/2014/self.acc)

		color = self.py3.COLOR_LOW

		if self.rate == 'bit':

			self.drate = 'Mbps'
			d_out = d_out * 8
			d_in  =	d_in  * 8
		else:
			self.drate = 'MB/s'

		if self.threshold < d_in or d_out:
			color = self.py3.COLOR_HIGH

		return {'full_text':'DOWN {0}{2} UP {1}{2}'.format(d_in,d_out,self.drate), 'cached_until':self.py3.time_in(self.refresh),'color': color}


	def _get_bytes(self):
		cmdGen = cmdgen.CommandGenerator()
		errorIndication, errorStatus, errorIndex, varBinds = cmdGen.getCmd(
		cmdgen.CommunityData(self.snmp_community),
		cmdgen.UdpTransportTarget((self.snmp_host, self.snmp_port)),
		self.wan_in, #out
		self.wan_out #in
		)
		
		return [int(x.prettyPrint().split('=')[1].strip()) for x in varBinds]
