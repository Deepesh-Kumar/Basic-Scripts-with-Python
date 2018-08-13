
#Upgrading Devices using vManage API call
#This is a simple script for upgrading devices part of a particular overlay. We start with using a API call (GET Request) 
# to fetch necessary data which includes device types and System IPs (Controllers or vEdge Devices) and use this information 
# in the next API call(POST Request) to upgrade those devices.
#The example shown here is done for all vEdge Devices (software and hardware), the script can be modifed to upgrade 
#Controllers as well.



import json
import requests
import itertools
from requests.auth import HTTPBasicAuth
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
s = requests.session()

g = []
h = []
#print d['data']
k = []
l = []

def main():
	IP1 = raw_input('Enter the IP: ')
	username1 = raw_input('Enter the username: ')
	password1 = raw_input('Enter the password: ')
	get_req(IP1,username1,password1)
	post_req(IP1,username1,password1,p,p1)

def get_req(IP,username,password):
	uri = 'https://' + IP + '/dataservice/device'  
	response = s.get(uri, auth=HTTPBasicAuth(username, password), verify=False)
	d = response.json()
	for i in d['data']:
		if i['device-model'] == 'vedge-1000' and i['reachability'] == 'reachable' and i['personality'] =='vedge':
			h.append(i['local-system-ip'])
			g.append(i['uuid'])
		elif i['device-model'] =='vedge-cloud' and i['reachability'] == 'reachable' and i['personality'] == 'vedge':
			k.append(i['local-system-ip'])
			l.append(i['uuid'])

p = {"action":"install","input":{"vEdgeVPN":0,"vSmartVPN":0,
            "data":[{"family":"vedge-mips","version":"18.3.0"}],"versionType":"vmanage","reboot":True,"sync":True},
            "devices":[{"deviceIP":" ","deviceId":''}],"deviceType":"vedge"}

p1 = {"action":"install","input":{"vEdgeVPN":0,"vSmartVPN":0,
            "data":[{"family":"vedge-x86","version":"18.3.0"}],"versionType":"vmanage","reboot":True,"sync":True},
            "devices":[{"deviceIP":" ","deviceId":''}],"deviceType":"vedge"}


#print  g
#print h

def post_req(IP,username,password,payload,payload1):
	urv = 'https://' + IP  + '/dataservice/device/action/install'
	headers={'Content-Type': 'application/json'}
	for (i,j) in zip(g,h):
		payload['devices'][0]['deviceId'] = i
		payload['devices'][0]['deviceIP'] = j
		q = json.dumps(payload)
		response_post = s.post(urv, auth=HTTPBasicAuth(username, password), data = q, headers=headers, verify=False)
		print response_post
	for (o,p) in zip(k,l):
		payload1['devices'][0]['deviceId'] = p
		payload1['devices'][0]['deviceIP'] = o
		e = json.dumps(payload1)
		response_post_new = s.post(urv, auth=HTTPBasicAuth(username, password), data = e, headers=headers, verify=False)
		print response_post_new


if __name__ == "__main__":
	main()
