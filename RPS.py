#Rock Paper scissors
#date: 1/3/2024
#for clearing screen
import os
#for easy mode (inputs are random)
import random
#the nine tiles
screen=["","","","","","","","",""]
#the dificukty level for the bot
level=""
#a count of how many o and x fill up any of the possible win combinations (if the count reaches 3 then=win)
bot_count=[0,0,0,0,0,0,0,0]
user_count=[0,0,0,0,0,0,0,0]
# all win combinations
dictionary = {
    # horisontal win
    0: [0, 1, 2],
    1: [3, 4, 5],
    2: [6, 7, 8],
    # verticle win
    3: [0, 3, 6],
    4: [1, 4, 7],
    5: [2, 5, 8],
    # diagonal win
    6: [0, 4, 8],
    7: [2, 4, 6]
}
#history of all previouse values inputed
delete=[]
botDelete=[]
#all the locations of the user and the bots input (o,x)
x = []
o = []
#update screen
def update(screen,user_count,bot_count,dictionary,o,x,botDelete,delete,level):
    #print the table
    print(screen[0],"|",screen[1],"|",screen[2],"\n--------\n",
          screen[3],"|",screen[4],"|",screen[5],"\n--------\n"
    ,screen[6],"|",screen[7],"|",screen[8],"\n")
    get_input(screen,user_count,bot_count,dictionary,o,x,botDelete,delete,level)

def get_input(screen,user_count,bot_count,dictionary,o,x,botDelete,delete,level):
    while True:#runs until user plays valid move
        try:
            location=input("which block do you want to input? (blocks=1-9)\n")
            if screen[int(location)-1] == "":
                screen[int(location)-1] = "X"
                os.system('cls')
                #bot move
                if level == "easy":
                    easy(screen,user_count,bot_count,dictionary,o,x,botDelete,delete,level)
                elif level == "medium":
                    medium(screen,user_count,bot_count,dictionary,o,x,botDelete,delete,level)
                elif level == "hard":
                    hard(screen,user_count,bot_count,dictionary,o,x,botDelete,delete,level)
            else:
                print("please enter a Valid move (1-9)")
        except ValueError:
            print("please enter a Valid move (1-9)")

def select(screen,user_count,bot_count,dictionary,o,x,botDelete,delete,level):
    # resets board
    screen = ["", "", "", "", "", "", "", "", ""]
    while True:
        dif=input("Select your oponent dificulty:\nEasy[1]\nMedium[2]\nHard[3]\n")
        if dif in ["easy","EASY","Easy","1"]:
            level="easy"
            os.system("cls")
            easy(screen,user_count,bot_count,dictionary,o,x,botDelete,delete,level)
        elif dif in ["medium","MEDIUM","Medium","2"]:
            level="medium"
            os.system("cls")
            medium(screen,user_count,bot_count,dictionary,o,x,botDelete,delete,level)
        elif dif in ["hard","Hard","HARD","3"]:
            level="hard"
            os.system("cls")
            hard(screen,user_count,bot_count,dictionary,o,x,botDelete,delete,level)
        else:
            print("please enter a valid input")

def win(screen,user_count,bot_count,dictionary,o,x,botDelete,delete,level):
    #resets the user count (tally of how close the user is to finishing the board)
    user_count=[0,0,0,0,0,0,0,0]
    bot_count=[0,0,0,0,0,0,0,0]
    #resets number of x and O counted
    x=[]
    o=[]
#except occurs when everything has been sorted
    #find all o and x locations
    for l in range(9):
        if screen[l] == "O":
            o.append(l)
        elif screen[l] == "X":
             x.append(l)
    #check and add for every time a number is part of a combination
    for i in range(8):
        #check each character to see if its in the dictionary
        for j in range(len(o)):
            try:#index out of bounds error would occur in the first iteration since o > s
                if x[j] in dictionary[i]:
                    user_count[i]+=1
                    delete.append(x[j])
            except:
                pass
            if o[j] in dictionary[i]:
                bot_count[i]+=1
                delete.append(o[j])
    #end game conditions
    if 3 in user_count:
        print(screen[0],"|",screen[1],"|",screen[2],"\n--------\n",
              screen[3],"|",screen[4],"|",screen[5],"\n--------\n"
        ,screen[6],"|",screen[7],"|",screen[8],"\n")
        print("You won, Congrats!!")
        again = input("would you like to play again?\n")
        if again.lower() in ["yes", "y"]:
            select(screen,user_count,bot_count,dictionary,o,x,botDelete,delete,level)
        else:
            print("thank you for having played my game")
            exit()
    if 3 in bot_count:
        print(screen[0],"|",screen[1],"|",screen[2],"\n--------\n",
              screen[3],"|",screen[4],"|",screen[5],"\n--------\n"
        ,screen[6],"|",screen[7],"|",screen[8],"\n")
        print("Robot won")
        again = input("would you like to play again?\n")
        if again.lower() in ["yes", "y"]:
            select(screen,user_count,bot_count,dictionary,o,x,botDelete,delete,level)
        else:
            print("thank you for having played my game")
            exit()
    if len(x) + len(o) == 9:
        print(screen[0],"|",screen[1],"|",screen[2],"\n--------\n",
              screen[3],"|",screen[4],"|",screen[5],"\n--------\n"
        ,screen[6],"|",screen[7],"|",screen[8],"\n")
        print("DRAW!!")
        again = input("would you like to play again?\n")
        if again.lower() in ["yes", "y"]:
            select(screen,user_count,bot_count,dictionary,o,x,botDelete,delete,level)
        else:
            print("thank you for having played my game")
            exit()
    update(screen,user_count,bot_count,dictionary,o,x,botDelete,delete,level)

#easy bot will always play random answers
def easy(screen,user_count,bot_count,dictionary,o,x,botDelete,delete,level):
    while True:
        bot=random.randint(0,8)
        if screen[bot] == "":
            screen[bot] = "O"
            win(screen,user_count,bot_count,dictionary,o,x,botDelete,delete,level)

#medium bot will always play random answers, but if it can fill in a row of 3 when it has 2 it will
def medium(screen,user_count,bot_count,dictionary,o,x,botDelete,delete,level):
    #this occurs when the bot is 1 move away from winning
    #this ensures that the bot will always win if its able to
    #find index of all bots placements
    for l in range(9):
        if screen[l] == "O":
            o.append(l)
    while True:
        if 2 in bot_count:
            #find missing value to win
            for i in range(3):
                if dictionary[bot_count.index(2)][i] not in o:
                    #fill in missing value if possibble
                    if screen[dictionary[bot_count.index(2)][i]] == "":
                        screen[dictionary[bot_count.index(2)][i]] = "O"
                        win(screen, user_count, bot_count, dictionary, o, x, botDelete, delete, level)
                    else:
                        bot_count[bot_count.index(2)] -= 1
        else:
            while True:
                bot = random.randint(0, 8)
                if screen[bot] == "":
                    screen[bot] = "O"
                    win(screen, user_count, bot_count, dictionary, o, x, botDelete, delete, level)

def hard(screen,user_count,bot_count,dictionary,o,x,botDelete,delete,level):
    # this occurs when the bot is 1 move away from winning
    # this ensures that the bot will always win if its able to
    # find index of all bots placements
    for l in range(9):
        if screen[l] == "O":
            o.append(l)
        elif screen[l] == "X":
            x.append(l)
    while True:
        if 2 in bot_count:
            # find missing value to win
            for i in range(3):
                if dictionary[bot_count.index(2)][i] not in o:
                    # fill in missing value if possibble
                    if screen[dictionary[bot_count.index(2)][i]] == "":
                        screen[dictionary[bot_count.index(2)][i]] = "O"
                        win(screen, user_count, bot_count, dictionary, o, x, botDelete, delete, level)
                    else:
                        bot_count[bot_count.index(2)] -= 1
        elif 2 in user_count:
            #block oponent from winning
            for i in range(3):
                if dictionary[user_count.index(2)][i] not in x:
                    # fill in missing value if possibble
                    if screen[dictionary[user_count.index(2)][i]] == "":
                        screen[dictionary[user_count.index(2)][i]] = "O"
                        win(screen, user_count, bot_count, dictionary, o, x, botDelete, delete, level)
                    else:
                        user_count[bot_count.index(2)] -= 1
        else:
            while True:
                bot = random.randint(0, 8)
                if screen[bot] == "":
                    screen[bot] = "O"
                    win(screen, user_count, bot_count, dictionary, o, x, botDelete, delete, level)
select(screen,user_count,bot_count,dictionary,o,x,botDelete,delete,level)