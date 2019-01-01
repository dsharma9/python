#!/usr/bin/env python3.7


def telNo(text1):
    if len(text1) !=12:
        return False
    for i in range(0,3):
        if not  text1[i].isdecimal():
            return False
    if text1[3] != '-':
          return False
    for i in range(4,7):
        if not text1[i].isdecimal():
            return False
    if text1[7] != '-':
        return False
    for i in range(8,12):
        if not text1[i].isdecimal():
            return False
    return True

while True:
    text=input("Kindly enter the phone number, Press enter to quit: ")
    if text == '':
        break
    print("Entered value is : " + text)
    print("Is entered no is correct: " + str(telNo(text)))
