import tkinter as tk
import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        return "You win!"
    else:
        return "You lose!"

def user_choice(choice):
    computer_choice = random.choice(["Rock", "Paper", "Scissors"])

    user_choice_label.config(text=f"Your choice: {choice}")
    computer_choice_label.config(text=f"Computer's choice: {computer_choice}")
    
    result = determine_winner(choice, computer_choice)
    result_label.config(text=result)
    
    update_score(result)

def update_score(result):
    global user_score, computer_score
    if result == "You win!":
        user_score += 1
    elif result == "You lose!":
        computer_score += 1
    score_label.config(text=f"Your score: {user_score}  |  Computer's score: {computer_score}")

def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    score_label.config(text=f"Your score: {user_score}  |  Computer's score: {computer_score}")
    result_label.config(text="Select Rock, Paper, or Scissors to start.")

def play_again():
    response = tk.messagebox.askyesno("Play Again", "Do you want to play again?")
    if response:
        reset_game()
    else:
        root.quit()

root = tk.Tk()
root.title("Rock-Paper-Scissors Game")

user_score = 0
computer_score = 0

instructions_label = tk.Label(root, text="Choose Rock, Paper, or Scissors", font=("Arial", 14))
instructions_label.pack(pady=10)

user_choice_label = tk.Label(root, text="Your choice: ", font=("Arial", 12))
user_choice_label.pack(pady=5)

computer_choice_label = tk.Label(root, text="Computer's choice: ", font=("Arial", 12))
computer_choice_label.pack(pady=5)

result_label = tk.Label(root, text="Select Rock, Paper, or Scissors to start.", font=("Arial", 12))
result_label.pack(pady=10)

score_label = tk.Label(root, text=f"Your score: {user_score}  |  Computer's score: {computer_score}", font=("Arial", 12))
score_label.pack(pady=10)

rock_button = tk.Button(root, text="Rock", font=("Arial", 14), width=10, height=2, command=lambda: user_choice("Rock"))
rock_button.pack(side="left", padx=20, pady=20)

paper_button = tk.Button(root, text="Paper", font=("Arial", 14), width=10, height=2, command=lambda: user_choice("Paper"))
paper_button.pack(side="left", padx=20, pady=20)

scissors_button = tk.Button(root, text="Scissors", font=("Arial", 14), width=10, height=2, command=lambda: user_choice("Scissors"))
scissors_button.pack(side="left", padx=20, pady=20)

play_again_button = tk.Button(root, text="Play Again", font=("Arial", 14), width=15, height=2, command=play_again)
play_again_button.pack(pady=20)

root.mainloop()
