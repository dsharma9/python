#!/usr/bin/env python3.7

import time
#from time import localtime, strftime, sleep, mktime

print("This is the program to check the time interval between the execution of time")


start_time=time.localtime()
print(f"Time start time is {time.strftime('%X',start_time)}")

time.sleep(10)

stop_time=time.localtime()
print(f"Time stop time is {time.strftime('%X',stop_time)}")

difference=time.mktime(stop_time) - time.mktime(start_time)

print(f"The time interval between the execution of the command is {difference}")
