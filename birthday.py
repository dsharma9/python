#!/usr/bin/env python3.7

print("This program is for getting friend's birthday detail")

birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

while True:
    print("Kindly enter the friends name, enter to terminalte the program")
    name = input()
    if name == '':
        break
    if name in birthdays:
        print("The "+ name + " has birthday on " +  birthdays[name] , end='\n')

    if name not in birthdays:
        print(f"Kindly enter the {name}'s B\'day")
        birthdays[name] = input()


print(birthdays)
