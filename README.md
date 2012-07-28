# i2captain #


NMEA network multiplexor.
There are 2 programs i2Captain and i2armChairCaptain.
They allow NMEA data to be sent to multiple ios, andriod and PCs for
logging / display.
They can be used either live (i2Captain) or after the event
(i2armChairCaptain).


## i2Captain ##

Copies data from a serial port and broadcasts as UDP (port 51243) and a muti
threaded TCP server (port 2114).

### Usage ###
> python i2Captain.py > log
This will run the application and capture the log into a file called
log suitable for use by i2armChairCaptain
### Todo ###
* Exit cleanly from control-c
* Log into file with timestamps
* Compress log files.
* Log rotation

## i2armChairCaptain ##
Takes a rate and logfile as argument.
Replays the log file NMEA over the same TCP and UDP ports as
i2Captain.
### Usage ###
> python i2armChairCaptain.py examples/holheadrace
this will start the simulator using some example data collected during
a race from HolyHead.

### Todo ###
* Log file with timestamps and then reply using accurate times
* Support compressed log files
## Apps that work ##
A list of applications that have been used to view the data.
So far no apps have been tested to set waypoints.
### Tested ###
* inavX [iOS](http://www.inavx.com/)
* iregatta [iOS](http://itunes.apple.com/gb/app/iregatta/id334632033?mt=8) [android](https://play.google.com/store/apps/details?id=dk.letscreate.aRegatta&hl=en)
### Untested ###
* iNMEA [iOS](http://itunes.apple.com/gb/app/inmea/id382867581?mt=8)
