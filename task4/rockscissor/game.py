import tkinter as tk
from tkinter import messagebox
import random
import os

class RockPaperScissorsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock-Paper-Scissors Game")
        
        self.user_score = 0
        self.computer_score = 0
        self.high_score = self.load_high_score()
        
        self.create_widgets()
        
    def create_widgets(self):
        self.label = tk.Label(self.root, text="Choose Rock, Paper, or Scissors", font=('Helvetica', 16))
        self.label.pack(pady=10)
        
        self.rock_button = tk.Button(self.root, text="Rock", command=lambda: self.play('rock'))
        self.rock_button.pack(side=tk.LEFT, padx=20)
        
        self.paper_button = tk.Button(self.root, text="Paper", command=lambda: self.play('paper'))
        self.paper_button.pack(side=tk.LEFT, padx=20)
        
        self.scissors_button = tk.Button(self.root, text="Scissors", command=lambda: self.play('scissors'))
        self.scissors_button.pack(side=tk.LEFT, padx=20)
        
        self.result_label = tk.Label(self.root, text="", font=('Helvetica', 14))
        self.result_label.pack(pady=10)
        
        self.score_label = tk.Label(self.root, text=f"Score - You: {self.user_score} | Computer: {self.computer_score}", font=('Helvetica', 14))
        self.score_label.pack(pady=10)
        
        self.high_score_label = tk.Label(self.root, text=f"High Score: {self.high_score}", font=('Helvetica', 14))
        self.high_score_label.pack(pady=10)
        
    def get_computer_choice(self):
        choices = ['rock', 'paper', 'scissors']
        return random.choice(choices)
        
    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a tie!"
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'scissors' and computer_choice == 'paper') or \
             (user_choice == 'paper' and computer_choice == 'rock'):
            return "You win!"
        else:
            return "You lose!"
        
    def play(self, user_choice):
        computer_choice = self.get_computer_choice()
        result = self.determine_winner(user_choice, computer_choice)
        
        if result == "You win!":
            self.user_score += 1
        elif result == "You lose!":
            self.computer_score += 1
        
        self.result_label.config(text=f"You chose: {user_choice}\nComputer chose: {computer_choice}\n{result}")
        self.score_label.config(text=f"Score - You: {self.user_score} | Computer: {self.computer_score}")
        
        if self.user_score > self.high_score:
            self.high_score = self.user_score
            self.save_high_score()
            self.high_score_label.config(text=f"High Score: {self.high_score}")
        
        if messagebox.askyesno("Play Again", "Do you want to play another round?"):
            self.result_label.config(text="")
        else:
            self.root.quit()

    def save_high_score(self):
        with open('high_score.txt', 'w') as file:
            file.write(str(self.high_score))

    def load_high_score(self):
        if os.path.exists('high_score.txt'):
            with open('high_score.txt', 'r') as file:
                return int(file.read().strip())
        return 0

if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissorsApp(root)
    root.mainloop()
