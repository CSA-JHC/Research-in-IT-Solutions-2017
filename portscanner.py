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

#Jessica Chiu

import socket
import sys

def checkports():
    try:
        remoteServer = input("Enter a remote host to scan: ")
        if remoteServer == '':
            print('You must enter a host ')
            checkports()
        remoteServerIP = socket.gethostbyname(remoteServer)
    except KeyboardInterrupt:
        print('You pressed Ctrl+C')
        checkports()

    ##host="172.17.2.87"
    port = [21, 22, 23, 25, 53, 80, 110, 143]
    print("This program will check ports 21,22,23,25,53,80,110,143")

    askport = input("Do you want to check any ports (YES OR NO)? ").upper()

    if askport == 'YES':
        numberports = int(input("How many ports do you want to check? "))
        for i in range(numberports):
         newport=input('What is your '+str(i+1)+' port? ')
         port.append(newport)
    elif askport == 'NO':
        pass

    try:
        for i in port:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((remoteServerIP, int(i)))
            if result == 0:
                print("Port "+str(i)+": Open".format(i))
                sock.close()
            else:
                print("Port "+str(i)+": Closed".format(i))
                sock.close()

    except KeyboardInterrupt:
        print('You pressed Ctrl+C')

    except socket.error:
        print("Couldn't connect to server")
        sys.exit()
        checkports()

    sys.exit()

checkports()
