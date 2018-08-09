
#Upgrading Devices using vManage API call
#This is a simple script for upgrading devices part of a particular overlay. We start with using a API call (GET Request) 
# to fetch necessary data which includes device types and System IPs (Controllers or vEdge Devices) and use this information 
# in the next API call(POST Request) to upgrade those devices.
#The example shown here is done for hardware vEdge Devices, the script can be modifed to upgrade Controllers or software vEdge 
#devices.


import json
import requests
import itertools
from requests.auth import HTTPBasicAuth
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
s = requests.session()


IP = raw_input("Enter the IP: ") .              # Enter the IP and credentials
username = raw_input("Enter the username: ")
password = raw_input("Enter the password:  ")


uri = 'https://' + IP + '/dataservice/device'        # API Call for Fetching Data

response = s.get(uri, auth=HTTPBasicAuth(username, password), verify=False)
d = response.json()   # Storing the response 

system_ip = []
device_id = []
for i in d['data']:
	if i['personality'] == 'vedge' and i['reachability'] == 'reachable':
		system_ip.append(i['local-system-ip'])      #Filtering System IP and Device ID from the data fetched 
		device_id.append(i['uuid'])             # and appending it to the list 
							#this can be further modifed to filter based on existing software version
	
payload = {"action":"install","input":{"vEdgeVPN":0,"vSmartVPN":0,
            "data":[{"family":"vedge-mips","version":"18.3.0"}],"versionType":"vmanage","reboot":True,"sync":True},
            "devices":[{"deviceIP":" ","deviceId":''}],"deviceType":"vedge"} . # Payload to be used for the post call family has to be changed for different device types

urv = 'https://'+ IP + '/dataservice/device/action/install' .   # API Call for Software Upgrade

headers={'Content-Type': 'application/json'}

for (i,j) in zip(g,h):
	payload['devices'][0]['deviceId'] = i   # . Updating values for device Id and 
	payload['devices'][0]['deviceIP'] = j	# .    device IP
	json_payload = json.dumps(payload)    
	response_post = s.post(urv, auth=HTTPBasicAuth(username, password), data = json_payload, headers=headers, verify=False)
	print response_post .   #Prints the response code for calls made for all iterations
