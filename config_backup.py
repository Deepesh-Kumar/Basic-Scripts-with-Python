
import pexpect
import sys
from datetime import date

z = 'Green88!!'


t = date.today()



#try:
c = pexpect.spawn('ssh admin@34.203.116.253')
c.timeout = 4
c.expect("password: ")
c.logfile = sys.stdout
#except pexpect.TIMEOUT:
#	raise Exception("Fail")


c.sendline(z)
c.expect('#')
c.sendline('request nms configuration-db backup path /home/admin/%s' %t )
c.timeout = 1000
c.expect('#')
c.sendline('request execute vpn 512 scp %s.tar.gz me@54.201.156.238:/home/me' %t)
i = c.expect(['yes/no ', 'password:'])
if i == 0:
	c.sendline('yes')
	c.timeout  = 100
	c.expect('password: ')
	c.sendline('vtac123')
	c.timeout  = 1000
	c.expect('#')
elif i == 1:
	c.sendline('vtac123')
	c.timeout  = 1000
	c.expect('#')
c.sendline('vshell')
c.expect('$')
c.sendline('rm - rf %s.tar.gz' %t)
c.timeout = 100
c.expect('$')
c.close()






















