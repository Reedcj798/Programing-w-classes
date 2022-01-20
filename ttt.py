# %%
def game_board(one,two,thr,four,five,six,svn,egt,nine):
    print (one, "|", two, "|", thr)
    print ("- + - + - ")
    print (four, "|", five, "|", six)
    print ("- + - + - ")
    print (svn, "|", egt, "|", nine)

def main():
    one = "1"
    two = "2"
    thr = "3"
    four = "4"
    five = "5"
    six = "6"
    svn = "7"
    egt = "8"
    nine = "9"
    go = 1
    box = "0"
    turns = 9
    player = "x"
    while go == 1 and turns > 0:
        print("Player ", player, " please choose your square!(1-9)")
        game_board(one,two,thr,four,five,six,svn,egt,nine)
        box = input("Player "+ player +" please choose your square!(1-9)") 
        if box == "1":
            one = player
        elif box == "2":
            two = player
        elif box == "3":
            thr = player
        elif box == "4":
            four = player
        elif box == "5":
            five = player
        elif box == "6":
            six = player
        elif box == "7":
            svn = player
        elif box == "8":
            egt = player
        elif box == "9":
            nine = player
        else:
            print("Please input a valid number(1-9)")
            if player == "o":
                player = "x"
            elif player == "x":
                player = "o"
        go = win_test(one,two,thr,four,five,six,svn,egt,nine,go,player)
        turns = turns - 1
        if player == "o":
            player = "x"
        elif player == "x":
            player = "o"
        if turns == 0:
            print("Tie! No winner!")
            game_board(one,two,thr,four,five,six,svn,egt,nine)
        print("")

def win_test(one,two,thr,four,five,six,svn,egt,nine,go,player):
    if one == two == thr:
        win(player,go)
    elif one == five == nine:
        win(player,go)
    elif four == five == six:
        win(player,go)
    elif svn == egt == nine:
       win(player,go)
    elif svn == five == thr:
        win(player,go)
    elif one == four == svn:
        win(player,go)
    elif two == five == egt:
        win(player,go)
    elif thr == six== nine:
        win(player,go)
    else:
        return go

def win(player,go):
    print("")
    print("Game Over!", player, "Wins!")
    go = 0
    return go

main()
# %%
