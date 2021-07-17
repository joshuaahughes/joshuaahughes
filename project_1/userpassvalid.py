import paramiko
import os.path
import time
import sys
import re

#checking username/password file
#Prompting user for input - USERNAME/PASSWORD FILE
user_file = input("\n# Enter user file path and name (e.g. D:\MyApps\myfile.txt): ")

#Verifying the validity of the USERNAME/PASSWORD file
if os.path.isfile(user_file):
	print("\n* Username/passowrd file is valid :)\n")
	
else:
	print("\n* file {} does not exist :( Please check and try again.\n".format(user_file))
	
#Checking commands file
#Prompting user for input - COMMANDS FILE
cmd_file = input("\n# Enter commands file path and name (e.g. D:\MyApps\myfile.txt): ")

#verifying the validity of the COMMANDS FILE
if os.path.isfile(cmd_file) == True:
	print("\n* Command file is valid :)\n")
else:
	print("\n* File {} does not exist :( Please check and try again.\n".format(cmd_file))
	sys.exit()
	