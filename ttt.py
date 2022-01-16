one = 1
two = 2
thr = 3
four = 4
five = 5
six = 6
svn = 7
egt = 8
nine = 9
game = 1
box = 0
turns = 9
player = "x"

def game_board():
    print (one, "|", two, "|", thr)
    print ("- + - + - ")
    print (four, "|", five, "|", six)
    print ("- + - + - ")
    print (svn, "|", egt, "|", nine)
    box = input("Player", player, "please choose your square!(1-9)")

def game_():
    if box == 1:
        one = player
    elif box == 2:
        two = player
    elif box == 3:
        thr = player
    elif box == 4:
        four = player
    elif box == 5:
        five = player
    elif box == 6:
        six = player
    elif box == 7:
        svn = player
    elif box == 8:
        egt = player
    elif box == 9:
        nine = player

def win_test():
    if one == two == thr:
        print("Game Over!", one, "Wins!")
        game == 0
    elif one == five == nine:
        print("Game Over!", one, "Wins!")
        game == 0
    elif four == five == six:
        print("Game Over!", four, "Wins!")
        game == 0
    elif svn == egt == nine:
        print("Game Over!", svn, "Wins!")
        game == 0
    elif svn == five == thr:
        print("Game Over!", svn, "Wins!")
        game == 0
    elif one == four== svn:
        print("Game Over!", one, "Wins!")
        game == 0
    elif two == five == egt:
        print("Game Over!", two, "Wins!")
        game == 0
    elif thr == six== nine:
        print("Game Over!", thr, "Wins!")
        game == 0
    
while game == 1:
    game_board
    game_
    win_test
    if game == 1:
        player = "o"
# %%
