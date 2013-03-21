import sys

filename = 'exploit.py'
f = ""

if len(sys.argv) == 2:

	filename = sys.argv[1]
	last_chars = filename[-3:]
	if last_chars != ".py":
		filename += ".py"

else:
	print "Default filename is 'exploit.py'"

try:
	exists = open(filename)
	
	if exists:
		ans = raw_input("exploit.py already exists, do you want to overwrite it? [y/n] ")
		if 'y' in ans:
			f = open(filename, "w")

		else:
			print "Run this again with this syntax: python " + sys.argv[0] + " [filename]"
			exit(0)

except:
	f = open(filename, "w")

text = """import socket

class Exploit():

	def execute(self, ip, port, flag_id):

		# Put your nasty code here ;)
		# Exploit must follow 4 rules!
		#	- each script must be self contained (i.e., located in this file).
		#	- the script must be pure python (no os.system() call).
		#	- one script, one thread. No multithreading.
		# 	- ZDI wants the exploit to be as stealthy as possible. It must ONLY
		#		steal the flag. It can't overwrite the flag and must not
		#		destroy the service.

		# Example:
		socket = socket.socket()
		socket.connect((ip, port))
		data = socket.recv(1024)
		socket.send("hello!")
		socket.close()

		# This example sets up a socket connection to the port and ip
		#	specified in the execute() params and sends the string
		# 	"hello!"
	
	def result(self):
	
		return { 'FLAG' : self.flag }
"""

f.write(text)
f.close()
