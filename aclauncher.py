#!/usr/bin/env python

import sys, time
from daemon import Daemon
def processSentance(sentance,sleepLength):
    print "Sentance is : ", sentance
    sleep(sleepLength/100.0)



class aclauncher(Daemon):
	def run(self):
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



if __name__ == "__main__":
	daemon = aclauncher('/tmp/i2armchair.pid','/dev/null','/tmp/out','/tmp/err')
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
