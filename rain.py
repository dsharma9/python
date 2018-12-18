#  Program for Rain

#/usr/bin/env  python3.7

print("Is it raining outside??")

while True:
    print('')
    print('')
    print("Still  raining outside??")
    print('Yes and no only for the rain')
    rain = input()
    if rain == 'yes':
         print('yes/no for umbrella')
         umbrella = input()
         if umbrella == 'yes':
              print('Take umbrella and go out')
              break
         else:
              print('Don\'t have umbrella so Wait until rain stops')
              continue
    else:
        print('It\'s not rainig , we can go out')
        break


