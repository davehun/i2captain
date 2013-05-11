#!/usr/bin/env python

import socket
import serial
import thread
import threading
import sys
import signal
import os
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
        inputs = [ self.tactick, self.gps ]
        while 1:
            readable, writable, exceptional  = select.select(inputs,[],[])
            for sp in readable:
                data=sp.read()
                print  data
                if sp != self.tactick:
                    self.tactick.write(data)
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
        print os.getpid()
        os.kill(os.getpid(), 9)

