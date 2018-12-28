#!/usr/bin/env python3.7

allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
        'Bob': {'ham': 3, 'apples': 2},
        'Carol': {'cups': 3, 'pies': 1}
        }

def picnic(material, item):
    no = 0
    for i,j in material.items():
        no += j.get(item, 0)
    return no





print("The no of Apples is : " + str(picnic(allGuests, 'apples')))
print("The no of pretzels is : " + str(picnic(allGuests, 'pretzels')))
print("The no of ham is : " + str(picnic(allGuests, 'ham')))
print("The no of cups is : " + str(picnic(allGuests, 'cups')))
print("The no of pies is : " + str(picnic(allGuests, 'pies')))
