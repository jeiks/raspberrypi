#!/usr/bin/env python2

from __future__ import print_function
from sys import exit, stderr
import ctypes, ctypes.util
from requests import get
from time import gmtime, mktime, altzone
from datetime import datetime

def get_localtime(tz):
    ttime   = gmtime()
    tm_year = ttime.tm_year
    tm_mon  = ttime.tm_mon
    tm_mday = ttime.tm_mday
    tm_hour = ttime.tm_hour+tz
    tm_min  = ttime.tm_min
    tm_sec  = ttime.tm_sec

    localtime = datetime(tm_year, tm_mon, tm_mday, tm_hour, tm_min, tm_sec)
    return mktime(localtime.timetuple())

def get_googletime(tz):
    try:
        #Date example: 'Sat, 27 Nov 2021 11:13:47 GMT'
        req = get('http://google.com').headers['Date'].split()[1:-1]
        #req = ['27', 'Nov', '2021', '11:13:47']
    except:
        print("ERROR: could not get Google's headers time.", file=stderr)
        exit(1)
    aux = ['Jan', 'Fev', 'Mar', 'Apr', 'May', 'Jun',
           'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    tm_year = int(req[2])
    tm_mon  = aux.index(req[1])+1
    tm_mday = int(req[0])
    tm_hour = int(req[3].split(':')[0])+tz
    tm_min  = int(req[3].split(':')[1])
    tm_sec  = int(req[3].split(':')[2])

    googletime = datetime(tm_year, tm_mon, tm_mday, tm_hour, tm_min, tm_sec)
    return mktime(googletime.timetuple())

#adapted from:
# stackoverflow, 12081310/python-module-to-change-system-date-and-time
def set_time(tz):
    librt = ctypes.CDLL(ctypes.util.find_library("rt"))
    class timespec(ctypes.Structure): # /usr/include/time.h
        _fields_ = [("tv_sec", ctypes.c_long), ("tv_nsec", ctypes.c_long)]

    ts = timespec()
    ts.tv_sec = int(get_googletime(tz)) #getting updated time
    ts.tv_nsec = 50000000 #~difference to process the header's requests
    
    librt.clock_settime(0, ctypes.byref(ts))

if __name__ == '__main__':
    desired_diff = 30.0 #seconds
    tz = altzone / 60 / 60 * -1
    googletime = get_googletime(tz)
    localtime  = get_localtime(tz)
    diff       = abs(localtime-googletime)

    if diff >= desired_diff: set_time(tz)
