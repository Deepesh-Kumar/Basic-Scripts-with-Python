
#Simple Python Script to get Software Versions of Devices(vEdges) using an API Call, we use json module to get data in a 
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
r = s.get(uri, auth=HTTPBasicAuth(username, password), verify=False)
a = r.json()
for i in a['data']:
	if i['personality'] == 'vedge':
		print i['version'],i['local-system-ip'],i['host-name']





















#class x():
#	def __init__(self,l):
#		self.l = l
#	def check(self):
#		d = []
#		if self.l >16:
#			d.append(self.l)
#			return d

#c = x(20)
#print c.check()



















#class Triangle():
#	def __init__(self,angle1,angle2,angle3):
#		self.angle1 = angle1
#		self.angle2	= angle2
#		self.angle3	= angle3
#	number_of_sides = 3
#	def check_angles(self):
#		if self.angle1 + self.angle2 + self.angle3 == 180:
#			return True
#		else:
#			return False

#my_triangle = Triangle(90,30,60)
#print my_triangle.check_angles()
#print my_triangle.number_of_sides








#class bank:
#	def __init__(self,name,balance):
#		self.name = name
#		self.balance = balance
#	def withdraw(self,amount):
#		if amount > self.balance:
#			print "fail"
#		else:
#			self.balance = self.balance - amount
#			self.balance = balance
#			return self.balance
#	def deposit(self,amount):
#		if amount > 0:
#			self.balance = self.balance + amount
#			return self.balance

	

#d = bank('Deepesh',100)
#print d.withdraw(50)

