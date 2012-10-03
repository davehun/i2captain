# i2captain #

NMEA network multiplexor. There are 2 programs i2captain and i2armchair.
They allow NMEA data to be sent to multiple ios, andriod and PCs for
logging / display. They can be used either live (i2captain) or after the
event (i2armchair).

## Installation ##

We need to make this a proper installable python package using setuptools
and/or distribute. This is what the setup.py is for.

See: http://guide.python-distribute.org/

## i2captain ##
Copies data from a serial port and broadcasts as UDP (port 51243) and a muti
threaded TCP server (port 2114).

### Usage ###
> python i2captain.py > log
This will run the application and capture the log into a file called
log suitable for use by i2armchair.

### Todo ###
* Merge in i2armchair as a subcommand.
* Ditch the threads!
* Exit cleanly from control-c
* Log into file with timestamps using python logging module.
* Compress log files.
* Log rotation (could be delegated to logrotate).

## i2armchair ##
Takes a rate and logfile as argument. Replays the log file NMEA over the
same TCP and UDP ports as i2captain.

### Usage ###
> python i2armchair.py examples/holheadrace
this will start the simulator using some example data collected during
a race from HolyHead.

### Todo ###
* Log file with timestamps and then reply using accurate times
* Support compressed log files

## Development Prerequisites ##

The following python modules are required to develop this software:
* pyserial
* pynmea

These can be installed into your python site-packages using pip:

$ pip install -r requirements.txt

Note that you can avoid contaminating your OS python installation by
installing these as user packages as follows:

$ pip install --user -r requirements.txt

This will typically be ~/.local/lib/python2.x/site-packages for Unix-likes.

## NMEA Applications Tested ##
A list of applications that have been used to view the data.
So far no apps have been tested to set waypoints.

* inavX [iOS](http://www.inavx.com/)
* iregatta [iOS](http://itunes.apple.com/gb/app/iregatta/id334632033?mt=8) [android](https://play.google.com/store/apps/details?id=dk.letscreate.aRegatta&hl=en)
### Untested ###
* iNMEA [iOS](http://itunes.apple.com/gb/app/inmea/id382867581?mt=8)

