#!/usr/bin/env  python3.7

users = [  { 'admin': True, 'active': True, 'name': 'Kevin' },
           { 'admin': True, 'active': False, 'name': 'Elisabeth' },
           { 'admin': False, 'active': True, 'name': 'Josh' },
           { 'admin': False, 'active': False, 'name': 'Kim' },
        ]
a=1
for i in users:
    print(str(a) + ". The user's name is: " + str(i['name']) + " and his admin status is: "  + str(i['admin']) + " and Active status is: " + str(i['active']))
    a += 1


print('')
print('')


for i in users:
    if i['admin'] == True and i['active'] == False:
        print("(ADMIN) : " + str(i['name']))
    elif i['active'] == True and i['admin'] == False:
        print("ACTIVE : " + str(i['name']))
    elif i['active'] == True and i['admin'] == True:
        print("ACTIVE - (ADMIN)" + str(i['name']))
    else:
        print(i['name'])





