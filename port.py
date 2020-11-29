from socket import *

hostname = input('Enter the host to be scanned: ')
ip_add = gethostbyname(hostname)
connections = [ ]   
for i in range(133, 136):
    s = socket(AF_INET, SOCK_STREAM)
      
    conn = s.connect_ex((ip_add, i))
    print(conn)
    connections.append(conn)
if 0 in connections:
    print ('Host is online')
    s.close()
else:
    print ('system is unreachable')