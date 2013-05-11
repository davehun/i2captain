#!/usr/bin/env python

import sys, time
from daemon import Daemon
from i2captain import SerialThread
import argparse
import socket
import signal
import sys

class ilauncher(Daemon):

 

    def run(self):


        TCP_PORT = 2114
        UDP_PORT = 51423

        BUFFER_SIZE = 20  # Normally 1024, but we want fast response

        udpSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        udpSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        udpSocket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        udpSocket.bind(( '' , UDP_PORT))

        global  serialThread
        print "make file"
        serialThread = SerialThread()
        serialThread.addSocket(udpSocket)
        print "starting thread"
        serialThread.start()
        print "thread started"

        server = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )
        server.bind ( ( '', TCP_PORT ) )
        server.listen ( 1 )
        
        while True:
            conn, addr = server.accept()
            print ("Connection from", addr)
            serialThread.addSocket(conn)
        server.close()



if __name__ == "__main__":
	daemon = ilauncher('/tmp/i2.pid','/dev/null','/tmp/out','/tmp/err')
	if len(sys.argv) == 2:
		if 'start' == sys.argv[1]:
			daemon.start()
		elif 'stop' == sys.argv[1]:
			daemon.stop()
		elif 'restart' == sys.argv[1]:
			daemon.restart()
		else:
			print "Unknown command"
			sys.exit(2)
		sys.exit(0)
	else:
		print "usage: %s start|stop|restart" % sys.argv[0]
		sys.exit(2)
