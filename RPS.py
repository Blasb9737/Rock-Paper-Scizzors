# Tick Tac Toe Version Two
# updated title to tic tac toe rather than RPS
# this version will have a UI for rock paper scizzors using Tkinter

# tkinters
from tkinter import *
# random is used for the easy robot
import random

# create the screen window
window = Tk()

# images needed for the game (the x the o and the empty space)
cross = PhotoImage(file="cross.png")
circle = PhotoImage(file="circle.png")
empty = PhotoImage(file="empty.PNG")

# a list with 9 list in it for 9 tiles
buttons = [[] for i in range(9)]

# list of all available tiles
blank = [0, 1, 2, 3, 4, 5, 6, 7, 8]

# all the vairables needed for checking whether who won
# the nine tiles
screen = ["", "", "", "", "", "", "", "", ""]
# a count of how many o and x fill up any of the possible win combinations (if the count reaches 3 then=win)
bot_count = [0, 0, 0, 0, 0, 0, 0, 0]
user_count = [0, 0, 0, 0, 0, 0, 0, 0]
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

# the game mode
selected = ""
# all the labels to display whether the user won or lost or drawed
win_label = Label(window, text="X wins!!", font=("Arial", 20))
lose_label = Label(window, text="O wins!!", font=("Arial", 15))
draw_label = Label(window, text="DRAW!! Nobody wins!", font=("Arial", 20))
xwin = Label(window, text="X wins!", font=("Arial", 20))
owin = Label(window, text="O wins!", font=("Arial", 20))


# check whether some-one wins
def check_win(screen):
    # check whether the user or the bot won
    # resets the user count (tally of how close the user is to finishing the board)
    user_count = [0, 0, 0, 0, 0, 0, 0, 0]
    bot_count = [0, 0, 0, 0, 0, 0, 0, 0]
    # resets number of x and O counted
    x = []
    o = []
    # except occurs when everything has been sorted
    # find all o and x locations
    for l in range(9):
        if screen[l] == "O":
            o.append(l)
        elif screen[l] == "X":
            x.append(l)
    # check and add for every time a number is part of a win combination
    for i in range(8):
        # check each character to see if its in the dictionary
        for j in range(len(x)):
            if x[j] in dictionary[i]:
                user_count[i] += 1
            # index error can occur :(
            try:
                if o[j] in dictionary[i]:
                    bot_count[i] += 1
            except:
                pass

    # end game conditions
    if 3 in user_count:
        # display that the user won
        win_label.grid(row=3, column=0, columnspan=3)
        # disable all buttons
        for i in range(len(blank)):
            buttons[blank[i]].config(state=DISABLED)
    if 3 in bot_count:
        # display that the user lost
        lose_label.grid(row=3, column=0, columnspan=3)
        # disable all buttons
        for i in range(len(blank)):
            buttons[blank[i]].config(state=DISABLED)
    if len(x) + len(o) == 9:
        # display that its a draw
        draw_label.grid(row=3, column=0, columnspan=3)
        # disable all buttons
        for i in range(len(blank)):
            buttons[blank[i]].config(state=DISABLED)


# easy bot will select a random move each turn
def easy_mode(pos, blank, screen):
    # occurs when theer is no tiles left
    try:
        # blank is used to keep track of the available tiles
        blank.pop(blank.index(pos))
        screen[pos] = "X"
        # add user input
        buttons[pos].config(image=cross, height=100, width=100, state=DISABLED)
        # bot input
        bot_move = random.choice(blank)
        buttons[bot_move].config(image=circle, height=100, width=100, state=DISABLED)
        # track bot input
        blank.pop(blank.index(bot_move))
        screen[bot_move] = "O"
    except:
        pass
    # check whther the user won
    window.after(10, check_win(screen))


# medium robot
def medium(pos, screen, blank):
    # this robot will act like the easy robot, but it will also go for the win every time the bot is able to win
    # user input
    # blank is used to keep track of the available tiles
    blank.pop(blank.index(pos))
    screen[pos] = "X"
    # add user input
    buttons[pos].config(image=cross, height=100, width=100, state=DISABLED)

    # clear th counter
    bot_count = [0, 0, 0, 0, 0, 0, 0, 0]
    o = []
    # needed to find how close the bot is to winning
    for l in range(9):
        if screen[l] == "O":
            o.append(l)
    # calculatehow close the robot is to winning
    # check and add for every time a number is part of a win combination
    for i in range(8):
        # check each character to see if its in the dictionary
        for j in range(len(o)):
            if o[j] in dictionary[i]:
                bot_count[i] += 1
    # except occurs if there is 9 tiles filled
    try:
        # if the bot can win
        if 2 in bot_count:
            # find missing value to win
            for i in range(3):
                if dictionary[bot_count.index(2)][i] not in o:
                    # fill in missing value if possibble
                    if screen[dictionary[bot_count.index(2)][i]] == "":
                        screen[dictionary[bot_count.index(2)][i]] = "O"
                        buttons[dictionary[bot_count.index(2)][i]].config(image=circle, height=100, width=100,
                                                                          state=DISABLED)
                        blank.pop(blank.index(dictionary[bot_count.index(2)][i]))
                        break
                    elif screen[dictionary[bot_count.index(2)][i]] == "X":
                        # rndomly select bot move
                        # bot input
                        bot_move = random.choice(blank)
                        buttons[bot_move].config(image=circle, height=100, width=100, state=DISABLED)
                        # track bot input
                        blank.pop(blank.index(bot_move))
                        screen[bot_move] = "O"
                        break
        elif 2 not in bot_count:
            # rndomly select bot move
            # bot input
            bot_move = random.choice(blank)
            buttons[bot_move].config(image=circle, height=100, width=100, state=DISABLED)
            # track bot input
            blank.pop(blank.index(bot_move))
            screen[bot_move] = "O"
    except:
        pass
    window.after(10, check_win(screen))


# hard robot
def hard(pos, screen, blank):
    # this robot will act like the easy robot, but it will also go for the win every time the bot is able to win
    # user input
    # blank is used to keep track of the available tiles
    blank.pop(blank.index(pos))
    screen[pos] = "X"
    # add user input
    buttons[pos].config(image=cross, height=100, width=100, state=DISABLED)

    # clear th counter
    bot_count = [0, 0, 0, 0, 0, 0, 0, 0]
    user_count = [0, 0, 0, 0, 0, 0, 0, 0]
    o = []
    x = []

    # needed to find how close the bot is to winning
    for l in range(9):
        if screen[l] == "O":
            o.append(l)
        elif screen[l] == "X":
            x.append(l)
    # calculatehow close the robot is to winning
    # check and add for every time a number is part of a win combination
    for i in range(8):
        # check each character to see if its in the dictionary
        for j in range(len(x)):
            if x[j] in dictionary[i]:
                user_count[i] += 1
            # index error can occur :(
            try:
                if o[j] in dictionary[i]:
                    bot_count[i] += 1
            except:
                pass
    # except occurs if there is 9 tiles filled
    try:
        # if the bot can win
        if 2 in bot_count:
            # find missing value to win
            for i in range(3):
                if dictionary[bot_count.index(2)][i] not in o:
                    # fill in missing value if possibble
                    if screen[dictionary[bot_count.index(2)][i]] == "":
                        screen[dictionary[bot_count.index(2)][i]] = "O"
                        buttons[dictionary[bot_count.index(2)][i]].config(image=circle, height=100, width=100,
                                                                          state=DISABLED)
                        blank.pop(blank.index(dictionary[bot_count.index(2)][i]))
                        break
                    elif screen[dictionary[bot_count.index(2)][i]] == "X":
                        # rndomly select bot move
                        # bot input
                        bot_move = random.choice(blank)
                        buttons[bot_move].config(image=circle, height=100, width=100, state=DISABLED)
                        # track bot input
                        blank.pop(blank.index(bot_move))
                        screen[bot_move] = "O"
                        break
        # bock the user from winning
        elif 2 in user_count:
            # find value needed to block yoour oponent
            for i in range(3):
                if dictionary[user_count.index(2)][i] not in x:
                    # fill in missing value if possibble
                    if screen[dictionary[user_count.index(2)][i]] == "":
                        screen[dictionary[user_count.index(2)][i]] = "O"
                        buttons[dictionary[user_count.index(2)][i]].config(image=circle, height=100, width=100,
                                                                           state=DISABLED)
                        blank.pop(blank.index(dictionary[user_count.index(2)][i]))
                        break
        elif 2 not in bot_count:
            # rndomly select bot move
            # bot input
            bot_move = random.choice(blank)
            buttons[bot_move].config(image=circle, height=100, width=100, state=DISABLED)
            # track bot input
            blank.pop(blank.index(bot_move))
            screen[bot_move] = "O"
    except:
        pass
    window.after(10, check_win(screen))


# 2-player mode
def coop(pos, screen):
    x = []
    o = []
    # document all the locations of x and o
    for e in range(len(screen)):
        if screen[e] == "X":
            x.append(e)
        elif screen[e] == "O":
            o.append(e)
    # determines whhos turn it is
    if len(o) == len(x):
        # user input
        # blank is used to keep track of the available tiles
        screen[pos] = "X"
        # add user input
        buttons[pos].config(image=cross, height=100, width=100, state=DISABLED)
    else:
        # other user input
        # blank is used to keep track of the available tiles
        screen[pos] = "O"
        # add user input
        buttons[pos].config(image=circle, height=100, width=100, state=DISABLED)
    # check win
    window.after(10, check_win(screen))


# user selects dificulty
def get_selected_option():
    pos = 0
    selected_value = var.get()
    if selected_value == 1:
        selected = "easy"
    elif selected_value == 2:
        selected = "medium"
    elif selected_value == 3:
        selected = "hard"
    elif selected_value == 4:
        selected = "coop"
    easy_radio.destroy()
    medium_radio.destroy()
    hard_radio.destroy()
    two_player_radio.destroy()
    window.after(10, tiles(selected))


def tiles(selected):
    # the nine buttons
    for i in range(9):
        # creatre the buttons
        buttons[i] = Button(window, image=empty, height=100, width=100, bd=10,
                            command=lambda pos=i: easy_mode(pos, blank, screen) if selected == "easy" else (
                                medium(pos, screen, blank) if selected == "medium" else (
                                    hard(pos, screen, blank) if selected == "hard" else coop(pos, screen))))
        # specify the row and the colum of the buttons
        set = i % 3
        if i in [0, 1, 2]:
            colum = 0
        elif i in [3, 4, 5]:
            colum = 1
        else:
            colum = 2
        buttons[i].grid(row=set, column=colum)


# user options.
# variable taht returns the value of the button selected
var = IntVar()
# easy mode selected
easy_radio = Radiobutton(window, text="Easy", variable=var, value=1, command=get_selected_option)
easy_radio.pack()

medium_radio = Radiobutton(window, text="Medium", variable=var, value=2, command=get_selected_option)
medium_radio.pack()

hard_radio = Radiobutton(window, text="Hard", variable=var, value=3, command=get_selected_option)
hard_radio.pack()

two_player_radio = Radiobutton(window, text="2 Player", variable=var, value=4, command=get_selected_option)
two_player_radio.pack()

window.mainloop()
