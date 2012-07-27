import socket
import serial
import socket
from SerialThread import *

TCP_PORT = 2114
UDP_PORT = 51423

BUFFER_SIZE = 20  # Normally 1024, but we want fast response

udpSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udpSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
udpSocket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
udpSocket.bind(( '' , UDP_PORT))



serial = SerialThread()
serial.addSocket(udpSocket)
serial.start()

#ser = serial.Serial('/dev/ttyUSB0', 4800, timeout=1)
    #x = ser.read()          # read one byte
    #s = ser.read(10)        # read up to ten bytes (timeout)
    #line = ser.readline()   # read a '\n' terminated line
server = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )
server.bind ( ( '', TCP_PORT ) )
server.listen ( 1 )

while True:
	conn, addr = server.accept()
	print ("Connection from", addr)
	serial.addSocket(conn)
server.close()
