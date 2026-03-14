import tkinter as tk
from tkinter import messagebox
import random

# Words and categories
words = ["python", "hangman", "keele", "assignment", "programming"]
categories = {
    "python": "A programming language",
    "hangman": "Classic word guessing game",
    "keele": "University",
    "assignment": "School or course work",
    "programming": "Computer activity"
}

# Game variables
word = random.choice(words)
guessed = ["_" for _ in word]
attempts_left = 6
wrong_letters = []

# Hangman stages as ASCII art (6 wrong attempts)
stages = [
    """
     _______
    |       |
    |
    |
    |
    |
    """,
    """
     _______
    |       |
    |       O
    |
    |
    |
    """,
    """
     _______
    |       |
    |       O
    |       |
    |
    |
    """,
    """
     _______
    |       |
    |       O
    |      /|
    |
    |
    """,
    """
     _______
    |       |
    |       O
    |      /|\\
    |
    |
    """,
    """
     _______
    |       |
    |       O
    |      /|\\
    |      /
    |
    """,
    """
     _______
    |       |
    |       O
    |      /|\\
    |      / \\
    |
    """
]

def guess_letter():
    global attempts_left
    letter = entry.get().lower()
    entry.delete(0, tk.END)

    if letter in guessed or letter in wrong_letters:
        messagebox.showinfo("Hangman", f"You already guessed '{letter}'")
        return

    if letter in word:
        for i, l in enumerate(word):
            if l == letter:
                guessed[i] = letter
        word_label.config(text=" ".join(guessed))
    else:
        wrong_letters.append(letter)
        attempts_left -= 1
        attempts_label.config(text=f"Attempts left: {attempts_left}")
        hangman_label.config(text=stages[6 - attempts_left])
        wrong_label.config(text="Wrong guesses: " + ", ".join(wrong_letters))

    if "_" not in guessed:
        messagebox.showinfo("Hangman", "Congratulations! You won!")
        reset_game()
    elif attempts_left == 0:
        messagebox.showinfo("Hangman", f"You lost! The word was '{word}'")
        reset_game()

def reset_game():
    global word, guessed, attempts_left, wrong_letters
    word = random.choice(words)
    guessed = ["_" for _ in word]
    attempts_left = 6
    wrong_letters = []
    word_label.config(text=" ".join(guessed))
    attempts_label.config(text=f"Attempts left: {attempts_left}")
    hangman_label.config(text=stages[0])
    wrong_label.config(text="Wrong guesses: ")

def show_hint():
    messagebox.showinfo("Hint", categories[word])

# GUI setup
root = tk.Tk()
root.title("Hangman Game")

tk.Label(root, text="Guess the word:").pack()
word_label = tk.Label(root, text=" ".join(guessed), font=("Helvetica", 24))
word_label.pack()

entry = tk.Entry(root)
entry.pack()

tk.Button(root, text="Guess", command=guess_letter).pack()
tk.Button(root, text="Show Hint", command=show_hint).pack(pady=5)

attempts_label = tk.Label(root, text=f"Attempts left: {attempts_left}")
attempts_label.pack()

hangman_label = tk.Label(root, text=stages[0], font=("Courier", 16), fg="red")
hangman_label.pack()

wrong_label = tk.Label(root, text="Wrong guesses: ")
wrong_label.pack()

root.mainloop()