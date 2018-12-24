#!/usr/bin/env python3.7

user = {'admin':False, 'active':False, 'name':'Deepak'}

if user['admin']==True:
    print('User ' + str(user['name']) + ' is admin')
elif user['active'] == True:
    print('User ' + str(user['name']) + ' is active')
else:
    print('User ' + str(user['name']) + ' is nor \'Admin\' neither \'Active\'')


print( 'My name is ' + user['name'])
