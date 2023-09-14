import tkinter as tk
from tkinter import messagebox
import random

# Define game settings
NUM_ROWS = 4
NUM_COLUMNS = 4
CARD_SIZE_W = 10
CARD_SIZE_H = 5
CARD_COLORS = ['red', 'blue', 'green', 'yellow',
               'purple', 'orange', 'cyan', 'magenta']
BACKGROUND_COLOR = "#343a40"
TEXT_COLOR = '#ffffff'
FONT_STYLE = ('Arial', 12, 'bold')
MAX_ATTEMPTS = 25

# Create a random grid of colors for the cards


def create_card_grid():
    colors = CARD_COLORS * 2
    random.shuffle(colors)
    grid = []

    for _ in range(NUM_ROWS):
        row = []
        for _ in range(NUM_COLUMNS):
            color = colors.pop()
            row.append(color)
        grid.append(row)
    return grid

# Handle player click on a card


def card_clicked(row, col):
    card = cards[row][col]
    color = card['bg']
    if color == 'black':
        card['bg'] = grid[row][col]
        revealed_cards.append(card)
        if len(revealed_cards) == 2:
            check_match()

# Check if the two revealed cards are the same


def check_match():
    card1, card2 = revealed_cards
    if card1['bg'] == card2['bg']:
        card1.after(1000, card1.destroy)
        card2.after(1000, card2.destroy)
        matching_cards.extend([card1, card2])
        revealed_cards.clear()
        check_win()
    else:
        card1.after(1000, lambda: card1.config(bg='black'))
        card2.after(1000, lambda: card2.config(bg='black'))
    revealed_cards.clear()
    update_score()

# Check if the player has won


def check_win():
    if len(matching_cards) == NUM_COLUMNS * NUM_ROWS:
        messagebox.showinfo('Congratulations!', 'You won the game!')
        window.quit()

# Update the score and check if the player has lost


def update_score():
    global num_attempts
    num_attempts += 1
    attempts_label.config(
        text='Attempts: {}/{}'.format(num_attempts, MAX_ATTEMPTS))
    if num_attempts >= MAX_ATTEMPTS:
        messagebox.showinfo('Game Over', 'You lost!')
        window.quit()


# Create the grid of cards
grid = create_card_grid()
cards = []
revealed_cards = []
matching_cards = []
num_attempts = 0

# Create the main window
window = tk.Tk()
window.title('Memory Game')
window.configure(bg=BACKGROUND_COLOR)

for row in range(NUM_ROWS):
    row_of_cards = []
    for col in range(NUM_COLUMNS):
        card = tk.Button(window, command=lambda r=row, c=col: card_clicked(
            r, c), width=CARD_SIZE_W, height=CARD_SIZE_H, bg='black', relief=tk.RAISED, bd=3)
        card.grid(row=row, column=col, padx=5, pady=5)
        row_of_cards.append(card)
    cards.append(row_of_cards)

# Customize button style
button_style = {'activebackground': '#f8f9fa',
                'font': FONT_STYLE, 'fg': TEXT_COLOR}
window.option_add('Button.*', button_style)

# Label for the number of attempts
attempts_label = tk.Label(window, text='Attempts: {}/{}'.format(
    num_attempts, MAX_ATTEMPTS), fg=TEXT_COLOR, bg=BACKGROUND_COLOR, font=FONT_STYLE)
attempts_label.grid(row=NUM_ROWS, columnspan=NUM_COLUMNS, padx=10, pady=10)

window.mainloop()
