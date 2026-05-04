import tkinter as tk

# global variables
players = ["X", "O"]
current_player = players[0]
buttons = [[None for _ in range(3)] for _ in range(3)]

# functions
def next_turn(row, column):
    global current_player

    if buttons[row][column]["text"] == "":
        buttons[row][column]["text"] = current_player

        if check_winner():
            status_label.config(text=current_player + " wins!")
        elif is_full():
            status_label.config(text="It's a tie!")
        else:
            current_player = players[1] if current_player == players[0] else players[0]
            status_label.config(text=current_player + " turn")

def check_winner():
    # check rows
    for row in range(3):
        if buttons[row][0]["text"] == buttons[row][1]["text"] == buttons[row][2]["text"] != "":
            return True

    # check columns
    for col in range(3):
        if buttons[0][col]["text"] == buttons[1][col]["text"] == buttons[2][col]["text"] != "":
            return True

    # check diagonals
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        return True

    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        return True

    return False

def is_full():
    for row in buttons:
        for button in row:
            if button["text"] == "":
                return False
    return True

def new_game():
    global current_player
    current_player = players[0]
    status_label.config(text=current_player + " turn")

    for row in buttons:
        for button in row:
            button.config(text="")

# GUI
window = tk.Tk()
window.title("Tic Tac Toe")

status_label = tk.Label(window, text=current_player + " turn", font=('Times New Roman', 30))
status_label.pack()

frame = tk.Frame(window)
frame.pack()

for row in range(3):
    for col in range(3):
        buttons[row][col] = tk.Button(frame, text="", font=('Times New Roman', 40),
                                      width=5, height=2,
                                      command=lambda row=row, col=col: next_turn(row, col))
        buttons[row][col].grid(row=row, column=col)

reset_button = tk.Button(window, text="Restart", font=('Times New Roman', 20), command=new_game)
reset_button.pack()

window.mainloop()