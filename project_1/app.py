import sys
import paramiko

from checkingipfilevalidity import ip_file_valid
from ipaddrval import ip_addr_valid
from checkreachability import ip_reach
from ssh_connection import ssh_connection
from creating_threads import create_threads

#Saving the list of IP addresses in ip.txt to a variable
ip_list = ip_file_valid()

#Verifying the validity of each IP address in the list
try:
    ip_addr_valid(ip_list)
    
except KeyboardInterrupt:
    print("\n\n* Program aborted by user. Exiting...\n")
    sys.exit()
    
try:
    ip_reach(ip_list)
    
except KeyboardInterrupt:
    print("\n\n* Program aborted by user. Exiting...\n")
    sys.exit()
    
#Calling threads creation function for one of multiple SSH connect
create_threads(ip_list, ssh_connection)

#End of program
