import tkinter as tk
from tkinter import messagebox
import random

# List of words for the game
words = ["python", "hangman", "programming", "coding", "challenge", "anaconda", "jupyter"]

# Initialize variables
word_to_guess = random.choice(words)
guessed_letters = []
attempts = 6

# Create a window
window = tk.Tk()
window.title("Hangman Game")
window.configure(bg="#ADD8E6")  # Light blue background

# Function to check if the game is over
def is_game_over():
    return check_win() or check_loss()

# Function to check if the player has won
def check_win():
    return all(letter in guessed_letters for letter in word_to_guess)

# Function to check if the player has lost
def check_loss():
    return attempts == 0

# Function to handle a letter guess
def guess_letter():
    global attempts
    letter = letter_entry.get().lower()
    if letter.isalpha() and len(letter) == 1:
        if letter in guessed_letters:
            display_message(f"You have already guessed '{letter}'")
        elif letter in word_to_guess:
            guessed_letters.append(letter)
            update_word_display()
            if check_win():
                display_message("Congratulations! You Win!")
                reset_game()
        else:
            guessed_letters.append(letter)
            attempts -= 1
            update_attempts_display()
            draw_hangman()
            if check_loss():
                display_message(f"You lose! The word was: {word_to_guess}")
                reset_game()
        letter_entry.delete(0, tk.END)  # Clear the input field
    else:
        display_message("Please enter a single letter.")

# Function to reset the game
def reset_game():
    global word_to_guess, guessed_letters, attempts
    word_to_guess = random.choice(words)
    guessed_letters = []
    attempts = 6
    update_word_display()
    update_attempts_display()
    draw_hangman(reset=True)

# Function to update the word display
def update_word_display():
    display_word = ""
    for letter in word_to_guess:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_"
        display_word += " "
    word_label.config(text=display_word)

# Function to update the attempts display
def update_attempts_display():
    attempts_label.config(text=f"Attempts Left: {attempts}")

# Function to draw the hangman figure
def draw_hangman(reset=False):
    if reset:
        canvas.delete("hangman")
    else:
        if attempts < 6:
            canvas.create_oval(125, 125, 175, 175, width=4, tags="hangman", outline="black")  # Head
        if attempts < 5:
            canvas.create_line(150, 175, 150, 225, width=4, tags="hangman", fill="black")  # Body
        if attempts < 4:
            canvas.create_line(150, 200, 125, 175, width=4, tags="hangman", fill="black")  # Left Arm
        if attempts < 3:
            canvas.create_line(150, 200, 175, 175, width=4, tags="hangman", fill="black")  # Right Arm
        if attempts < 2:
            canvas.create_line(150, 225, 125, 250, width=4, tags="hangman", fill="black")  # Left Leg
        if attempts < 1:
            canvas.create_line(150, 225, 175, 250, width=4, tags="hangman", fill="black")  # Right Leg

# Function to display messages on the canvas and remove after a delay
def display_message(message):
    message_item = canvas.create_rectangle(0, 0, 300, 60, fill="#ADD8E6", outline="#ADD8E6")  # Background for the message
    text_item = canvas.create_text(150, 30, text=message, font=("Arial", 14), fill="black")  # Adjusted font size and position
    
    def remove_message():
        canvas.delete(message_item)
        canvas.delete(text_item)
        
    window.after(2000, remove_message)  # Message will disappear after 3 seconds

# Create GUI elements
canvas = tk.Canvas(window, width=300, height=300, bg="#ADD8E6")  # Light blue background
word_label = tk.Label(window, text="", font=("Arial", 24), bg="#ADD8E6", fg="black")
attempts_label = tk.Label(window, text="", font=("Arial", 16), bg="#ADD8E6", fg="black")
letter_entry = tk.Entry(window, width=5, font=("Arial", 16))
guess_button = tk.Button(window, text="Guess", command=guess_letter)
reset_button = tk.Button(window, text="Reset", command=reset_game)

canvas.create_line(50, 250, 250, 250, width=4)  # Base line
canvas.create_line(200, 250, 200, 100, width=4)  # Post
canvas.create_line(100, 100, 200, 100, width=4)  # Beam
canvas.create_line(150, 100, 150, 120, width=4)  # Rope

# Pack GUI elements
canvas.pack()
word_label.pack()
attempts_label.pack()
letter_entry.pack()
reset_button.pack(side=tk.BOTTOM, pady=10)  # Placing the Reset button at the bottom
guess_button.pack(side=tk.BOTTOM, pady=10)  # Placing the Guess button at the bottom

# Update initial displays
update_word_display()
update_attempts_display()
draw_hangman(reset=True)

# Run the application
window.mainloop()






# In[ ]:




