#!/usr/bin/env python

import socket
import serial
import thread
import threading
import sys
import signal
from time import sleep

TCP_PORT = 2114
UDP_PORT = 51423

BUFFER_SIZE = 20  # Normally 1024, but we want fast response

class SerialThread (threading.Thread):
    """This just watches the serial port.
    when it reads a byte it is spat to all the connected socket."""

    def __init__( self ):
        threading.Thread.__init__(self)

        self.mySockets = []
        #print "init"
        self.tactick = serial.Serial('/dev/ttyUSB0', 4800, timeout=1)
        self.gps = serial.Serial('/dev/ttyACM0', 4800, timeout=1)
    def run ( self ):
        
        global mySockets
        #print(len(self.mySockets))
        while 1:
            data = self.tactick.read()
            print  data
            for theSocket in self.mySockets:
                try:
                    theSocket.send(data)
                except socket.error, msg:
                    theSocket.close()
                    self.mySockets.remove(theSocket)
                    theSocket = None
                    break
                continue
                
    def addSocket(self, socket):

        self.mySockets.append(socket)
        #print(len(self.mySockets))

    def delSocket(self, socket):
        mySockets.remove(socket)



def signal_handler(signal, frame):
        print 'exit'
        for theSocket in self.mySockets:
            theSocket.close()

        sys.exit(0)
# Main entry point.
if __name__ == "__main__":

    udpSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udpSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    udpSocket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    udpSocket.bind(( '' , UDP_PORT))
    
    print 'Press Ctrl+C to exit'
    

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
    signal.signal(signal.SIGINT, signal_handler)
    while True:
            conn, addr = server.accept()
            print ("Connection from", addr)
            serial.addSocket(conn)
    server.close()

