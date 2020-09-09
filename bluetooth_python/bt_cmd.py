from bluetooth import *
import time
import bluetooth
import binascii
import os

print ("search ...")


device_num = 0
nearby_devices = discover_devices(lookup_names = True)

print ("found %d devices" % len(nearby_devices))
print (nearby_devices[0][0])
print ("next step")
for name, addr in nearby_devices:
	
	print (" %d %s - %s" % (device_num, addr, name))
	device_num+= 1

#print nearby_devices

print ("select bt device num")
set_device_num = input()

#print ("the set device %s" % nearby_devices[int(set_device_num)][0])

bd_addr = "80:7D:3A:B5:8F:FA"
# Create the client socket

client_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
#client_socket.connect((serverMACAddress, port))

#client_socket = bluetooth.BluetoothSocket( RFCOMM )
print (nearby_devices[int(set_device_num)][0])


#client_socket.connect((bd_addr, 1))
client_socket.connect((nearby_devices[int(set_device_num)][0], 3))

#client_socket.send("Hello")

print ("connect finished! you can set your cmd")


while True:
	#cmd = raw_input()
	#client_socket.send(cmd)
	client_socket.send('get rtk message')
	sleep(0.01)
client_socket.close()


