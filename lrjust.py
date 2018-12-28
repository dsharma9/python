#!/usr/bin/enf python3.7


players= {'cricket':11, 'hocky':11, 'TT': 2, 'tanice':4, 'foosball':4, 'ludo':4}

def playerlist(game, lj , rj):
    print("Printing Player's list")
    for i,j in game.items():
        print(i.ljust(rj, '.'), end=' : ')
        print(str(j).rjust(lj, '.'))




playerlist(players, 3, 10)
print()
print()
playerlist(players, 4, 12)
print()
print()
playerlist(players, 7, 14)
print()
print()
playerlist(players, 9, 18)
