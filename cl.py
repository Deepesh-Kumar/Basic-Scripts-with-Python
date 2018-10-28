import json
import requests
import itertools
from requests.auth import HTTPBasicAuth
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
s = requests.session()	

class ch:

	def __init__(self, IP,username,password,g,h,k,l):
		self.IP = IP
		self.username = username
		self.password = password
		self.g = g
		self.h = h
		self.k = k
		self.l = l


	def get(self):
		try:
			uri = 'https://' + self.IP + '/dataservice/device'  
			response = s.get(uri, auth=HTTPBasicAuth(self.username, self.password), verify=False)
			d = response.json()
			for i in d['data']:
				if i['device-model'] == 'vedge-1000' or i['device-model'] == 'vedge-cloud' and i['reachability'] == 'reachable' and i['personality'] =='vedge':
					self.h.append(i['local-system-ip'])
					self.g.append(i['uuid'])
				#elif i['device-model'] =='vedge-cloud' and i['reachability'] == 'reachable' and i['personality'] == 'vedge':
					#self.k.append(i['local-system-ip'])
					#self.l.append(i['uuid'])
		except:
			print 'Cannot Connect'
	def get_bgp(self):
		#s = requests.session()
		urv = 'https://' + self.IP + '/dataservice/device/interface/stats?deviceId='
		for i in self.h:
			urv1 = urv + i + '&&&'
			#print urv1
			response1 = s.get(urv1, auth=HTTPBasicAuth(self.username, self.password), verify=False)
			e = response1.json()
			for i in e['data']:
				print i['vpn-id']

	def get_arp(self):
		urv2 = 'https://' + self.IP + '/dataservice/device/arp?deviceId='
		for i in self.h:
			urv3 = urv2 + i + '&&&'
			response12 = s.get(urv3, auth=HTTPBasicAuth(self.username, self.password), verify=False)
			f = response12.json()
			for i in f['data']:
				print i['if-name'], i['vpn-id'], i['vdevice-host-name'], i['mac'], i['ip']

	def get_software_version(self):
		urv4 = 'https://' + self.IP + '/dataservice/device/software?deviceId='
		count = 0
		for i in (self.h):
			urv5 = urv4 + i + '&&&'
			response12 = s.get(urv5, auth=HTTPBasicAuth(self.username, self.password), verify=False)
			g = response12.json()
			for i in g['data']:
				if i['version'] == '18.3.0' and i['active'] == 'true':
					count = count + 1

    #def deactivate_policy(self):
    #	urv4 = 'https://' + self.IP + '/dataservice/template/policy/vsmart/deactivate/da1a9dea-aac7-4171-805a-39c58c51dfdb?confirm=true'
    #	headers={'Content-Type': 'application/json'}
    #	#p = 'da1a9dea-aac7-4171-805a-39c58c51dfdb'
		#q = json.dumps(p)
	#	response1 = s.post(urv4, auth=HTTPBasicAuth(self.username, self.password), headers=headers, verify=False)
	#	print

	def get_appserver_logs(self):
		url = 'https://' + self.IP + '/dataservice/util/logfile/appserver/lastnlines?lines=100'
		response12 = s.get(url, auth=HTTPBasicAuth(self.username, self.password), verify=False)
		print response12.content

		

t = []
u = []
v = []
l = []
a = ch('10.195.168.110', 'deepesh', 'deepesh4321!',t,u,v,l)
a.get()
#a.get()
#a.get_software_version()
#a.deactivate_policy()
#a.get_software_version()
a.get_appserver_logs()
