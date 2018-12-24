#!/usr/bin/env python3.7

def listPrint(l1):
    count = int(len(l1))
    index = 0
    for i in l1:
        if index == count -1:
            print(" and " + i )
            break
        print(i + ', ', end='')
        index +=1


spam = ['apples', 'bananas', 'tofu', 'cats']
listPrint(spam)
print('')
print('')

listPrint(spam)
