import socket
from smbus import SMBus

HOST = '192.168.1.13'  
PORT = 8080

addrs = 0x8 # bus address
bus = SMBus(1) # indicates /dev/ic2-1
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(2)

while True:
    client, addr = s.accept()
    
    try:
        print('Connected by', addr)

        numb = 1
        while numb == 1:
            data = client.recv(1024)
            str_data = data.decode("utf8")

            if str_data == "5":
                print("5")
            #    bus.write_byte(addrs, 0x0)
            #elif str_data != "5" or str_data == null:
            #    bus.write_byte(addrs, 0x1)
            elif str_data == "0":
                print("0")
            elif str_data == "1":
            	print("1")
            elif str_data == "2":
            	print("2")
            elif str_data == "3":
            	print("3")
            elif str_data == "4":
            	print("4")
            #elif str_data == "5":
            #	print("5")
            else:
                numb = 0
    finally:
        client.close()

s.close()
