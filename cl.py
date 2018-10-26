import json
import requests
import itertools
from requests.auth import HTTPBasicAuth
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
#s = requests.session()	

class ch:
	g = []
	h = []
	k = []
	l = []
	def __init__(self, IP,username,password):
		self.IP = IP
		self.username = username
		self.password = password


	def post(self):
		s = requests.session()
		uri = 'https://' + self.IP + '/dataservice/device'  
		response = s.get(uri, auth=HTTPBasicAuth(self.username, self.password), verify=False)
		d = response.json()
		#print d['data']
		for i in d['data']:
			if i['device-model'] == 'vedge-1000' and i['reachability'] == 'reachable' and i['personality'] =='vedge':
				ch.h.append(i['local-system-ip'])
				ch.g.append(i['uuid'])
			elif i['device-model'] =='vedge-cloud' and i['reachability'] == 'reachable' and i['personality'] == 'vedge':
				ch.k.append(i['local-system-ip'])
				ch.l.append(i['uuid'])
		urv = 'https://' + self.IP  + '/dataservice/device/action/install'
		headers={'Content-Type': 'application/json'}
		payload = {"action":"install","input":{"vEdgeVPN":0,"vSmartVPN":0,"data":[{"family":"vedge-mips","version":"18.3.0"}],"versionType":"vmanage","reboot":True,"sync":True},"devices":[{"deviceIP":" ","deviceId":''}],"deviceType":"vedge"}
		for (i,j) in zip(ch.g,ch.h):
			payload['devices'][0]['deviceId'] = i
			payload['devices'][0]['deviceIP'] = j
			q = json.dumps(payload)
			response_post = s.post(urv, auth=HTTPBasicAuth(self.username, self.password), data = q, headers=headers, verify=False)
			print response_post
		
		
    	
    	
    	#for (o,p) in zip(self.k,self.l):
    	#	payload1['devices'][0]['deviceId'] = p
    	#	payload1['devices'][0]['deviceIP'] = o
    	#	e = json.dumps(payload1)
    	#	response_post_new = s.post(urv, auth=HTTPBasicAuth(self.username, self.password), data = e, headers=headers, verify=False)
    	#	print response_post_new







	#def post(self):

a = ch('10.195.168.110', 'deepesh', 'deepesh4321!')
#a.get()
a.post()
