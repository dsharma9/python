#!/usr/bin/env python3.7

def telNo(text1):
    if len(text1) != 12:
        return False
    for i in range(0,3):
        if not  text1[i].isdecimal():
            return False
    if text1[3] != '-':
          return False
    for i in range(4,7):
        if not text1[i].isdecimal():
            return False
    if text1[7] != '-' :
        return False
    for i in range(8,12):
        if not text1[i].isdecimal():
            return False
    return True


message = input("Kindly enter string having phone no: ")
#message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
for i in range(len(message)):
    chunk = message[i:i+12]
    telNo(chunk)
    if telNo(chunk) == True:
        print("Found tel no: " + message[i:i+12])
