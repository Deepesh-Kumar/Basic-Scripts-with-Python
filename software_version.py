
#Simple Python Script using GET request to get Software Versions of Devices(vEdges) using an API Call, we use json module to get data in a 
#list format, and filter the required data


import json
import requests
from requests.auth import HTTPBasicAuth
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
s = requests.session()
IP = raw_input('Enter the IP: ')
username = raw_input('Enter the username:  ')
password = raw_input('Enter the password:  ')
uri = 'https://' + IP + ':8443/dataservice/device'
response = s.get(uri, auth=HTTPBasicAuth(username, password), verify=False)
response_data = response.json()
for i in response_data['data']:
	if i['personality'] == 'vedge':
		print i['version'],i['local-system-ip'],i['host-name']


		
#Python Script for POST request , this example is for rediscovering devices, the rsponse will just print the status code for the 
#request
		
import json
import requests
from requests.auth import HTTPBasicAuth
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
s = requests.session()
uri = 'https://34.203.116.253:8443/dataservice/device/action/rediscover'
payload = {'devices':[{'deviceId': "8e897e63-7b79-4622-8040-6aab57fab89e", 'deviceIP': "1.1.1.222"}]}
payload = json.dumps(payload)
response = s.post(uri, auth=HTTPBasicAuth('admin', 'Green88!!'), data=payload, verify=False)
print response




























