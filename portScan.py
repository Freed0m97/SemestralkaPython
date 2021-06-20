#!/usr/bin/env python
import socket
import subprocess
import sys
import threading
import time
import concurrent.futures
from queue import Queue

print_lock = threading.Lock()

def tcp_scanner(port, server):    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)# 
    remote_server = server
    remote_server_IP = socket.gethostbyname(remote_server)
    #remote_server_IP = '192.168.0.100'
    try:
        result = sock.connect_ex((remote_server_IP, port))   
        strViceInfo = ""
        if result == 0:
            if(port == 25):
                strViceInfo = "SMTP"
            elif (port == 21) or (port == 20):
                strViceInfo = "FTP"
            elif (port == 22):
                strViceInfo = "SSH"
            elif (port == 23):
                strViceInfo = "Telnet"
            elif (port == 53):
                strViceInfo = "DNS"
            elif (port == 69):
                strViceInfo = "TFTP"
            elif (port == 80):
                strViceInfo = "HTTP"
            elif (port == 443):
                strViceInfo = "HTTPS"
            elif (port == 110):
                strViceInfo = "POP3"
            elif (port == 111):
                strViceInfo = "NFS"
            elif (port == 119):
                strViceInfo = "NNTP"
            elif (port == 123):
                strViceInfo = "NTP"
            elif (port == 135):
                strViceInfo = "Windows RPC"
            elif (port == 137) or (port == 138) or (port == 139):
                strViceInfo = "Windows NetBIOS"
            elif (port == 143):
                strViceInfo = "IMAP"
            elif (port == 156):
                strViceInfo = "SQL"
            elif (port == 445):
                strViceInfo = "SMB directly over IP"
            elif (port == 465):
                strViceInfo = "Authenticated SMTP"                
            elif (port == 543):
                strViceInfo = "Kerberos login"
            elif (port == 544):
                strViceInfo = "Kerberos remote shell"
            elif (port == 548):
                strViceInfo = "AFP"
            elif (port == 993):
                strViceInfo = "IMAPS"
            elif (port == 995):
                strViceInfo = "POP3S"   
            elif (port == 1433) or (port == 1434):
                strViceInfo = "Microsoft SQL Server"
            print("Port:{0:25}{1}".format(strViceInfo, port)+" open")
            sock.close()
    except socket.gaierror:
        print('hostname couldnt be resolved')
        sys.exit()

def checkRange(rangeLow, rangeHigh, server):
    #oklika jak získat jednotlivé porty když je to v multithreadu, protože prostě nemůžu rozchodit žádný postup co je na netu a už u toho sedím několik hodin, určitě by to šlo lépe
    for x in range(rangeLow,rangeHigh): 
        t = threading.Thread(target=tcp_scanner,kwargs={'port':x,'server':server}) 
        t.start()
    
#def checkRange(rangeLow, rangeHigh, server):
    #oklika jak získat jednotlivé porty když je to v multithreadu, protože prostě nemůžu rozchodit žádný postup co je na netu a už u toho sedím několik hodin, určitě by to šlo lépe
 #   original_stdout = sys.stdout
  #  with open('VypisPortu.txt', 'w') as f:
   #     sys.stdout = f
    #    for x in range(rangeLow,rangeHigh): 
     #       t = threading.Thread(target=tcp_scanner,kwargs={'port':x,'server':server}) 
      #      t.start()
    #sys.stdout = original_stdout

def checkSpecificPort(specificPort, server):
    checkRange(specificPort,specificPort+1, server)



#checkSpecificIP(80, '192.168.0.100')
#checkRange(20,22)