#!/usr/bin/env   python3.7


players={'Shewag': {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12},
         'Sachin': {'rope': 2, 'torch': 2, 'gold coin': 32, 'dagger': 4, 'arrow': 1},
         'Pandaya': {'rope': 4, 'torch': 3, 'gold coin': 22, 'dagger': 2, 'arrow': 2},
         'Dhoni': {'rope': 6, 'torch': 1, 'gold coin': 12, 'dagger': 0, 'arrow': 9}
         }

def totalM(player):
    for (i,j) in player.items():
        print()
        print('')
        print( "Player " + i + " has below medals: ")
        c=0
        for a,b in j.items():
            print(str(a) +"::" + str(b))
            c+=int(b)
        print(i + " has total no of Medal is :" + str(c))


totalM(players)
