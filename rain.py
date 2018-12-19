#  Program for Rain

#/usr/bin/env  python3.7


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
           while True:
              print('Don\'t have umbrella so Wait until rain stops')
              print('Still raining: yes/no?')
              rain = input()
              if  rain == 'yes':
                  print('Wait a while untill rain stops')
              else:
                  print('Go outside')
                  break
           break
    else:
        print('It\'s not rainig , we can go out')
        break


