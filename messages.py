#!/usr/bin/env python3.7

print("printing the no of character using dict data structure")

def msgDict(msg):
    count={}
    for i in msg:
        count.setdefault( i, 0)
        count[i] = count.get(i) + 1
    for k,v in count.items():
        print(k, ": ", v)

message="The pprint.pprint() function is especially helpful when the dictionary itself contains nested lists or dictionaries.If you want to obtain the prettified text as a string value instead of displaying it on the screen, call pprint.pformat() itead. These two lines are equivalent to each other:pprint.pprint(someDictionaryValue)print(pprint.pformat(someDictionaryValue))Using Data Structures to Model Real-World ThingsEven before the Internet, it was possible to play a game of chess with someone on the other side of the world. Each player would set up a chessboard at their home and then take turns mailing a postcard to each other describing each move. To do this, the players needed a way to unambiguously describe the state of the board and their moves.In algebraic chess notation, the spaceon the chessboard are identified by a number and letter coordinate, as in Figure 5-1.The coordinates of a chessboard in algebraic chess notationFigure 5-1. The coordinates of a chessboard in algebraic chess notationThe chess pieces are identified by letters: K for king, Q for queen, R for rook, B for bishop, and N for knight. Describing a move uses the letter of the piece and the coordinates of its destination. A pair of these moves describes what happens in a single turn (with white going first); for instance, the notation 2. Nf3 Nc6 indicates that white moved a knight to f3 and black moved a knight to c6 on the second turn of the game.Computers have good memories. A program on a modern computer can easily store billions of strings like '2. Nf3 Nc6'. This is how computers can play chess without having a physical chessboard. They model data to represent a chessboard, and you can write code to work with this model.This is where lists and dictionaries can come in. You can use them to model real-world things, like chessboards. For the first example, you’ll use a game that’s a little simpler than chess: tic-tac-toe.A tic-tac-toe board looks like a large hash symbol (#) with nine slots that can each contain an X, an O, or a blank. To represent the board with a dictionary, you can assign each slot a string-value key, as shown in Figure 5-2.You can use string values to represent what’s in each slot on the board: 'X', 'O', or ' ' (a space character). Thus, you’ll need to store nine strings. You can use a dictionary of values for this. The string value with the key 'top-R' can represent the top-right corner, the string value with the key 'low-L' can represent the bottom-left corner, the string value with the key 'mid-M' can represent the middle, and so on.Thanks it's working..I meant resultset of query. Do you know which are the concerns using python..i don't know am new of this technology before i have worked in dotnet."
print(message)
msgDict(message)

