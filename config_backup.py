
import pexpect
import sys
from datetime import date

IP = raw_input("Enter the IP of the vmanage: ")
username = raw_input("Enter the username: ")
password = raw_input("Enter the password: ")


backup_server_IP = raw_input("Enter the IP of the backup server: ")
backup_server_username = raw_input("Enter the username for the backup server: ")
backup_server_Password = raw_input("Enter the password for the backup server: ")

today_date = date.today()



#try:
c = pexpect.spawn('ssh admin@%s' %IP)
c.timeout = 4
c.expect("password: ")
c.logfile = sys.stdout
#except pexpect.TIMEOUT:
#	raise Exception("Fail")


c.sendline(password)
c.expect('#')
c.sendline('request nms configuration-db backup path /home/admin/%s' %today_date )
c.timeout = 1000
c.expect('#')
c.sendline('request execute vpn 512 scp %s.tar.gz me@%s:/home/%s' (%today_date, %backup_server_IP) )
i = c.expect(['yes/no ', 'password:'])
if i == 0:
	c.sendline('yes')
	c.timeout  = 100
	c.expect('password: ')
	c.sendline(backup_server_Password)
	c.timeout  = 1000
	c.expect('#')
elif i == 1:
	c.sendline(backup_server_Password)
	c.timeout  = 1000
	c.expect('#')
c.sendline('vshell')
c.expect('$')
c.sendline('rm - rf %s.tar.gz' %today_date)
c.timeout = 100
c.expect('$')
c.close()

