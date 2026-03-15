# GUI improvement commit for branch merge

import tkinter as tk
from tkinter import messagebox
from game_logic import TicTacToe

game = TicTacToe()

# Function to update the turn label
def update_turn_label():
    color = "blue" if game.current_player == "X" else "green"
    turn_label.config(text=f"Current Turn: Player {game.current_player}", fg=color)

# Function called when a button is clicked
def click_button(index):
    if game.make_move(index):
        player_color = "blue" if game.current_player == "X" else "green"
        buttons[index]["text"] = game.current_player
        buttons[index]["fg"] = player_color
        winner = game.check_winner()

        if winner:
            if winner == "Draw":
              messagebox.showinfo("Game Over", "No one wins! It's a draw!")
            else:
                messagebox.showinfo("Game Over", f"Player {winner} wins!")
            reset_game()
        else:
            game.switch_player()
            update_turn_label()

# Reset the game
def reset_game():
    global game
    game = TicTacToe()
    for b in buttons:
        b["text"] = ""
        b["fg"] = "black"
    update_turn_label()

# GUI setup
root = tk.Tk()
root.title("Tic Tac Toe")

# Turn label
turn_label = tk.Label(root, text=f"Current Turn: Player {game.current_player}", font=("Arial", 16))
turn_label.grid(row=0, column=0, columnspan=3, pady=10)

# Create 3x3 board
buttons = []
for i in range(9):
    button = tk.Button(root, text="", font=("Arial", 30), width=5, height=2,
                       command=lambda i=i: click_button(i))
    button.grid(row=(i//3)+1, column=i%3)
    buttons.append(button)

# Restart button
reset = tk.Button(root, text="Restart Game", command=reset_game, bg="orange", fg="white", font=("Arial", 14))
reset.grid(row=4, column=0, columnspan=3, sticky="we", pady=10)



# Start game
update_turn_label()
root.mainloop()
