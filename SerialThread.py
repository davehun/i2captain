import thread
import threading
import serial
import socket
class SerialThread (threading.Thread):
    # This just watches the serial port.
    #when it reads a byte it is spat to all the connected socket

    def __init__( self ):
        threading.Thread.__init__(self)

        self.mySockets = []
        #print "init"
        self.ser = serial.Serial('/dev/ttyUSB0', 4800, timeout=1)
    def run ( self ):
        
        global mySockets
        #print(len(self.mySockets))
        while 1:
            data = self.ser.read()
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
       
