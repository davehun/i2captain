from time import sleep
import argparse

def processSentance(sentance,sleepLength):
    print "Sentance is : ", sentance
    sleep(sleepLength)

parser = argparse.ArgumentParser(description="Navigation simulator. Plays back log files over the network")
parser.add_argument('--rate', type=int,  default=1    ,  nargs='?', help='how long to sleep for between sending each NMEA sentance')
parser.add_argument( 'infile', nargs='?', type=argparse.FileType('r'), help='File with log in')


args = parser.parse_args()
print args
#logFile = open(,'r')
sentance = ""
for line in args.infile:
    if line == "":
        exit
    line = line[0:1]
    sentance += line
    if line == "\n":
        if len(sentance) > 4:
            processSentance(sentance,args.rate)
        sentance = ""

        
