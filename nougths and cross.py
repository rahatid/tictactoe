from tkinter import *
import random

def next_turn(row, column):
    global player, x_wins, o_wins, ties

    if buttons[row][column]['text'] == "" and check_winner() is False:
        buttons[row][column]['text'] = player

        if check_winner() is False:
            player = players[1] if player == players[0] else players[0]
            label.config(text=(player + " turn"))
        elif check_winner() is True:
            if player == "x":
                x_wins += 1
            else:
                o_wins += 1
            update_score()
            label.config(text=(player + " wins"))
        elif check_winner() == "Tie":
            ties += 1
            update_score()
            label.config(text="Tie!")

def update_score():
    score_label.config(text="X wins: {} | O wins: {} | Ties: {}".format(x_wins, o_wins, ties))

def check_winner():
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            for column in range(3):
                buttons[row][column].config(fg="red")
            return True

    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            for row in range(3):
                buttons[row][column].config(fg="red")
            return True

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        for i in range(3):
            buttons[i][i].config(fg="red")
        return True

    if buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(fg="red")
        buttons[1][1].config(fg="red")
        buttons[2][0].config(fg="red")
        return True

    if empty_spaces() is False:
        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="yellow")
        return "Tie"

    else:
        return False

def empty_spaces():
    spaces = 9
    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != "":
                spaces -= 1
    return spaces != 0

def new_game():
    global player
    player = random.choice(players)
    label.config(text=player + " turn")
    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="", bg="#F0F0F0", fg="black")

def new_game():
    global player
    player = random.choice(players)
    label.config(text=player + " turn")
    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="", bg="#F0F0F0", fg="black")

window = Tk()
window.title("Tic-Tac-Toe")
players = ["x", "o"]
player = random.choice(players)
x_wins = 0
o_wins = 0
ties = 0  # Initialize tie counter
buttons = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

label = Label(text=player + " turn", font=('consolas', 40))
label.pack(side="top")

score_label = Label(text="", font=('consolas', 20))
score_label.pack(side="top")
update_score()  # Update the score label initially

reset_button = Button(text="restart", font=('consolas', 20), command=new_game)
reset_button.pack(side="top")

frame = Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="", font=('consolas', 40), width=5, height=2,
                                      command=lambda row=row, column=column: next_turn(row, column))
        buttons[row][column].grid(row=row, column=column)

window.mainloop()