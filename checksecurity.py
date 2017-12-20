# This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
#
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
#
#     You should have received a copy of the GNU General Public License
#     along with this program.  If not, see <http://www.gnu.org/licenses/>.

import socket
import sys

def checkports():
    #getting the IP's
    for i in range(0,155):
        x=100+i #gets IP's after 100 to get ports from 172.17.2.100-154
        remoteServer="172.17.2."+str(x)
        print(remoteServer)
        remoteServerIP = socket.gethostbyname(remoteServer)
        socket.setdefaulttimeout(0.5) #go faster

        ##host="172.17.2.87"
        port = [80,20,22]
        #print("This program will check ports 80,20,22")

        checkedports=[]
        try:
            for i in port:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                result = sock.connect_ex((remoteServerIP, int(i)))
                if result == 0:
                    #if port is open add to checkedports list
                    openport=("Port "+str(i)+": Open".format(i))
                    print(openport)
                    sock.close()
                    checkedports.append('Port '+str(i))
                else:
                    #if it is closed do nothing
                    closeport="Port "+str(i)+": Closed".format(i)
                    print(closeport)
                    sock.close()

        except KeyboardInterrupt:
            #if something goes wrong
            print('Something went wrong')
            pass

        except socket.error:
            #if something goes wrong
            print("Couldn't connect to server")
            sys.exit()
            checkports()

        #clean up the list
        checkedports=str(checkedports)
        checkedports=checkedports.replace('[','')
        checkedports=checkedports.replace(']','')
        checkedports=checkedports.replace("'",'')

        #write IP's and open ports to a server
        file=open('portcheck.txt','a')
        file.write(str(remoteServer)+' - '+str(checkedports)+'\n')
        file.close()

    sys.exit()

checkports()
