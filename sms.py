#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess
import time
import platform

adb = r'c:\adb\adb.exe'
sqlite_exe = 'su -c \'sqlite3 /data/data/com.android.providers.telephony/databases/mmssms.db \"%s\"\''
	
def count_device():
	return subprocess.check_output([adb,'devices']).count('device')

def output_device():
	for i in subprocess.check_output([adb,'devices']).split('\n')[1:]:
		print i 

def check_device():
	if count_device() < 2:
		print 'Device error, no device pluged in.'
		print count_device()
		exit(1)
	elif count_device() > 3:
		print 'Device error, more than one device pluged in.'
		output_device()
		exit(1)


def main():
	current_time = int(subprocess.check_output([adb,'shell','date +%s']))*1000
	last_updated = str(current_time)

	counter = 0

	while True:
		foo = '[' + str(counter) + ']'
		print str(foo) + 'local_time:' + time.asctime()
		print str(foo) + 'last_updated:' + time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(int(last_updated)/1000))
	
		sql = sqlite_exe % ('SELECT address, date, body, type FROM sms WHERE date > ' + last_updated + ' order by date desc')
		sms_dump = subprocess.check_output([adb,'shell',sql])

		for i,line in enumerate(sms_dump.split('\n')):
			part = line.split('|')
			if len(part) > 3 and part[3].strip() == '1':
				#SMS
				#print str(i) + 'th: ' + 'Sender:' + part[0] + ',time:' + time.strftime("%Y-%m-%dT %H:%M:%S",time.localtime(int(part[1])/1000)) + ',Body:' + part[2] + ',type:' + part[3]
				if platform.system() == 'Windows':
					print str(foo) + str(i) + 'th: ' + 'Sender:' + part[0] + ',time:' + time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(int(part[1])/1000)) + ',Body:' + part[2].decode('utf8').encode('gbk') + ',type:' + part[3]
					#bar = 'python /sdcard/smssend.py ' + part[0] + ' \"' + part[0]  + 'sended at ' + time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(int(part[1])/1000)) + ':' + part[2] + '\"'
					execute_command = 'python /sdcard/smssend.py ' + part[0]  + ' \"'  +  part[2] +'\"'
					print execute_command
					bar = subprocess.check_call([adb,'shell',execute_command])
					print bar
				else:
					print str(foo) + str(i) + 'th: ' + 'Sender:' + part[0] + ',time:' + time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(int(part[1])/1000)) + ',Body:' + part[2] + ',type:' + part[3]
				if i == 0:
					last_updated = part[1]
		counter = counter + 1
		time.sleep(2)

if __name__ == '__main__':
	check_device()
	main()