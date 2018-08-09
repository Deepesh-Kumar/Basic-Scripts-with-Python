
import json
import requests
import itertools
from requests.auth import HTTPBasicAuth
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
s = requests.session()

#payload = {"action":"install","input":{"vEdgeVPN":0,"vSmartVPN":0,"data":[{"family":"vedge-x86","version":"18.3.0"}],"versionType":"vmanage","reboot":'true',"sync":'true'},
#			"devices":[{"deviceIP":"1.1.1.15","deviceId":"5cbad91d-9805-441b-a27d-8d9f262cc788"}],"deviceType":"vedge"}
#payload = json.dumps(payload)
uri = 'https://10.195.168.110:8443/dataservice/device'
response = s.get(uri, auth=HTTPBasicAuth('deepesh', 'deepesh4321!'), verify=False)
d = response.json()
#e = {}
g = []
h = []
#print d['data']
for i in d['data']:
	if i['personality'] == 'vedge' and i['reachability'] == 'reachable':
		h.append(i['local-system-ip'])
		g.append(i['uuid'])

#print  g
#print h
p = {"action":"install","input":{"vEdgeVPN":0,"vSmartVPN":0,
            "data":[{"family":"vedge-mips","version":"18.3.0"}],"versionType":"vmanage","reboot":True,"sync":True},
            "devices":[{"deviceIP":" ","deviceId":''}],"deviceType":"vedge"}

urv = 'https://10.195.168.110:443/dataservice/device/action/install'
headers={'Content-Type': 'application/json'}
#response_post = s.post(uri, auth=HTTPBasicAuth('deepesh', 'deepesh4321!'), data = payload, verify=False)
for (i,j) in zip(g,h):
	p['devices'][0]['deviceId'] = i
	p['devices'][0]['deviceIP'] = j
	q = json.dumps(p)
	response_post = s.post(urv, auth=HTTPBasicAuth('deepesh', 'deepesh4321!'), data = q, headers=headers, verify=False)
	print response_post


#print e
#urv = 'https://10.195.168.110:443/dataservice/device/action/install'

#payload = {"action":"install","input":{"vEdgeVPN":0,"vSmartVPN":0,
	#		"data":[{"family":"vedge-mips","version":"18.3.0"}],"versionType":"vmanage","reboot":true,"sync":true},
	#		"devices":[{"deviceIP":"1.1.1.4","deviceId":"11OD152130127"}],"deviceType":"vedge"}

#response_post = s.get(uri, auth=HTTPBasicAuth('deepesh', 'deepesh4321!'), data = payload, verify=False)
#for j,k in e.items():
#	print j
#	print k







    







#{"action":"install","input":{"vEdgeVPN":0,"vSmartVPN":0,"data":[{"family":"vedge-x86","version":"18.3.0"}],"versionType":"vmanage","reboot":true,"sync":true},
#"devices":[{"deviceIP":"1.1.1.215","deviceId":"210a74a7-9a0f-462c-8098-ba60369733ac"}],"deviceType":"vedge"}
































#def a(str):
#	for i in range(0,len(str)):
#		if str[i].isalpha():
#			if str[i-1] != '+' or str[i+1] != '+':
#				return 'false'
#	return 'True'
#
#print a("+a+b+c+")