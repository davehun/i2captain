from time import sleep
import thread
import threading
import socket
import sys

def processSentance(sentance,sleepLength):
    print "Sentance is : ", sentance
    sleep(sleepLength/100.0)
class FileThread (threading.Thread):
    # This just reads the file


    def __init__( self,theLogFile ,theSleepLength ):
        threading.Thread.__init__(self)
        global infile
        self.infile = theLogFile
        self.sleepLength =theSleepLength
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
