import threading
import socket
from queue import Queue
import sys

#inputs
checkhost = str(input("Would you like to scan locally? Reply yes or no: ")).lower()
if checkhost == "yes":
    port_addr = my_socket.gethostname()
else:
    port_addr = str(input("Enter customised address to scan: "))

port_low = int(input("Lower bound of port number: "))
port_high = int(input("Higher bound of port number: "))

open_ports = []
close_ports = []

def checksocket(port_addr,q):
    while True:
        my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # AF_INET: address format is host and port number --> IPv4
        curr_port = q.get()
        try:
            value = my_socket.connect((port_addr,curr_port))
            data = my_socket.recv(1024)
            open_ports.append(curr_port)
            #print("Socket successfully binded to empty port {0}. It looks open".format(curr_port))
            value.close()

        except:
            close_ports.append(curr_port)
            #print("The port {0} appears to be busy".format(curr_port))
        q.task_done()

# Create the queue array
q = Queue()

total_processes = port_high-port_low
for k in range(total_processes):
    q.put(k+port_low)

#Creation of Threads
for x in range(8):
     t = threading.Thread(target=checksocket,args=(port_addr,q))
     # daemon will die by itself
     t.daemon = True
     t.start()

#stop once done
q.join()

print("\nThese are the closed ports: ",close_ports)

if len(open_ports) == 0:
    print("There are no open ports")
else:
    print("\nThese are the open ports",open_ports)

sys.exit()

'''
def port_test(ports,port_addr,my_socket):
    try:
        #ports = int(ports)
        value = my_socket.connect((port_addr,ports))
        data = my_socket.recv(1024)
        print("Socket successfully binded to empty port {0}. It looks open".format(ports))
        value.close()
    except:
        print("The port {0} appears to be busy".format(ports))
port_test(12344,'127.0.0.1',my_socket)
'''
