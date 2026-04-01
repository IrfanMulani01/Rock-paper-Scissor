import tkinter as tk
from tkinter import Tk
import random

class main:
    def __init__(self, root):
        
        self.root = root
        
        # set title to the window
        self.root.title("Game of Rock Paper Scissor")
        
        # set diamentions to window
        self.root.geometry("700x500")
        
        #set label
        self.label = tk.Label(root, text="Enter Options:", font=30)
        self.label.pack()
        self.label.place(x=10,y=20, height=50, width=200)
        
        # set entry 
        self.entry = tk.Entry(root, width=30)
        self.entry.pack()
        self.entry.place(x=250, y=20, height=50, width=400)
        
        # setting random in rock paper scissor wth help of chioce
        self.choise = ['rock', 'paper', 'scissor']
        self.random = random.choice(self.choise)
        
        #set button
        self.button = tk.Button(root, text="Submit", command=self.show)
        self.button.pack()
        self.button.place(x=280, y=100, height=50, width=100)
        
        # set label to show the rock, paper or scissor
        self.label1 = tk.Label(root, text="Your choice is ")
        self.label1.pack()
        self.label1.place(x=100,y=180, height=100, width=500)
        
        
    def show(self):
        guess = self.entry.get().lower()
        if guess not in self.choise:
            self.label1.config(text="You entered value is invalid")
            return
        if guess == self.random:
            result = "Game Tie!"
        elif guess == "paper" and self.random == "rock" or guess == "scissor" and self.random == "paper" or guess == "rock" and self.random == "scissor":
            self.label1.config(text=guess)
            result = "You Win"
        else:
            result = "You lose!"
        
        self.label1.config(
            text=f"You chose: {guess} | Computer chose: {self.random} → {result}"
        )
        
if __name__ == "__main__":
    root = Tk()
    obj = main(root)
    root.mainloop()