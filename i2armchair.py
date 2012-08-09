#!/usr/bin/env python

from time import sleep
import argparse
import socket
import signal
import sys
import thread
import threading


def processSentance(sentance,sleepLength):
    print "Sentance is : ", sentance
    sleep(sleepLength/100.0)


class FileThread (threading.Thread):
    """This just reads the file."""

    def __init__( self,theLogFile ,theSleepLength ):
        threading.Thread.__init__(self)
        global infile
        self.infile = theLogFile
        self.sleepLength = theSleepLength
        self.mySockets = []
        self.leaving = False
        #print "init"
        
    def run ( self ):
        global infile
        global sleepLength
        global mySockets
        sentance = ""
        #print(len(self.mySockets))

        for line in self.infile:
            
            if ((line == "") or (self.leaving)):
                print "leaving now"
                break
            line = line[0:1]
            sentance += line
            if line == "\n":
                if len(sentance) > 4:
                    processSentance(sentance,self.sleepLength)
                    for data in sentance:
                        for theSocket in self.mySockets:
                            try:
                                theSocket.send(data)
                            except socket.error, msg:
                                theSocket.close()
                                self.mySockets.remove(theSocket)
                                theSocket = None
                                break
                            continue
                sentance = ""
                
    def addSocket(self, socket):

        self.mySockets.append(socket)
        #print(len(self.mySockets))

    def delSocket(self, socket):
        mySockets.remove(socket)
       
    def exit(self):
         for theSocket in self.mySockets:
             try:
                 theSocket.close()
             except socket.error, msg:
                 self.mySockets.remove(theSocket)
                 theSocket = None
                 break
             continue
         print "All closed lets exit"
         global leaving
         self.leaving = True


def signal_handler(signal, frame):
        fileThread.exit()
        sys.exit(0)
        
if __name__ == "__main__":

    signal.signal(signal.SIGINT, signal_handler)

    parser = argparse.ArgumentParser(description="Navigation simulator. Plays back log files over the network")
    parser.add_argument('--rate', type=int,  default=1    ,  nargs='?', help='how long to sleep for between sending each NMEA sentance')
    parser.add_argument( 'infile', nargs='?', type=argparse.FileType('r'), help='File with log in')

    args = parser.parse_args()
    print args

    #logFile = open(,'r')
    sentance = ""
    TCP_PORT = 2114
    UDP_PORT = 51423

    BUFFER_SIZE = 20  # Normally 1024, but we want fast response

    udpSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udpSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    udpSocket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    udpSocket.bind(( '' , UDP_PORT))

    global fileThread
    fileThread = FileThread(args.infile,args.rate)
    fileThread.addSocket(udpSocket)
    fileThread.start()

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
            fileThread.addSocket(conn)
    server.close()


