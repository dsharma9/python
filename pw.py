#! python3.7

print("This is weak password managing program")

import sys,pyperclip

password = {'Deepak':'65b50b04a6af50bb2f174db30a8c6dad',
            'GhaatWala':'a281620372706d8da9085ba8b1123ae0',
            'Kalua':'f9949a935133924912ab250ea2920d49',
            'Govia':'1221f611c0d9def6b2a8229464fa1f3c'
           }

print("The encripted password for user is : " + str(sys.argv[1]))
if len(sys.argv) < 2:
   printf("No user name passed as argument. Existing()")
   sys.exit()
else:
   print("User " + str(sys.argv[1]) + " found in out database and password is copied to clipboard")

   pyperclip.copy('hia')
   print(pyperclip.paste())

   pyperclip.copy(str(password[sys.argv[1]]))
   print("Printing the password of the user " + str(sys.argv[1]) + " is ", end=':')
   print(pyperclip.paste())
