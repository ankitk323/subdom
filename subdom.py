#!/usr/bin/python2

import os
from termcolor import colored
Name = '''
   _____       _     _____                  
  / ____|     | |   |  __ \                 
 | (___  _   _| |__ | |  | | ___  _ __ ___  
  \___ \| | | | '_ \| |  | |/ _ \| '_ ` _ \ 
  ____) | |_| | |_) | |__| | (_) | | | | | |
 |_____/ \__,_|_.__/|_____/ \___/|_| |_| |_|
                                            
by @ankitk323
'''                                            

try:
	print colored(Name , "white")
	file = raw_input("Enter the file name: ")
	print("\n")
	with open(file) as file:
		dump = file.read()
		dump = dump.splitlines()
		for url in dump:
			command = "dig -t A " + url
			process = os.popen(command)
			results = str(process.read())
			if (results.find('azure')!=-1):
				print ("[*] \"AZURE\" find in " + url)
			elif (results.find('amazon')!=-1):
				print ("[*] \"AWS\" find in " + url)
			elif (results.find('bitbucket')!=-1):
				print ("[*] \"BITBUSKET\" find in " + url)
			elif (results.find('cargocollective')!=-1):
				print ("[*] \"CARGOCOLLECTIVE\" find in " + url)
			elif (results.find('feedpress')!=-1):
				print ("[*] \"FEEDPRESS\" find in " + url)
			elif (results.find('github')!=-1):
				print ("[*] \"GITHUB\" find in " + url)
			elif (results.find('helpjuice')!=-1):
				print ("[*] \"HELPJUICE\" find in " + url)
			elif (results.find('heroku')!=-1):
				print ("[*] \"HEROKU\" find in " + url)
			elif (results.find('intercom')!=-1):
				print ("[*] \"INTERCOM\" find in " + url)	
			elif (results.find('readme')!=-1):
				print ("[*] \"README\" find in " + url)
			elif (results.find('shopify')!=-1):
				print ("[*] \"SHOPIFY\" find in " + url)
			elif (results.find('strikingly')!=-1):
				print ("[*] \"STRIKINGLY\" find in " + url)
			elif (results.find('surge')!=-1):
				print ("[*] \"SURGE\" find in " + url)
			elif (results.find('uptimerobot')!=-1):
				print ("[*] \"UPTIMEROBOT\" find in " + url)
			else:
				print colored("[*] " + url + " Not Vulnerable " , "white")
	print colored("\nCompleted\n" , "white")			
except:
	print colored("\nTry Again\n" , "red")