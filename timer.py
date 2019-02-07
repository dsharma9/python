#!/usr/bin/env python3.7

from time import localtime, strftime, sleep, mktime

print("This is the program to check the time interval between the execution of time")


start_time=localtime()
print(f"Time start time is {strftime('%X',start_time)}")

sleep(10)

stop_time=localtime()
print(f"Time stop time is {strftime('%X',stop_time)}")

difference=mktime(stop_time) - mktime(start_time)

print(f"The time interval between the execution of the command is {difference}")
