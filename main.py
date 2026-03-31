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
        self.label = tk.Label(root, text="Enter Options")
        self.label.pack()
        
        # set entry 
        self.entry = tk.Entry(root, width=30)
        self.entry.pack()
        
        # setting random in rock paper scissor wth help of chioce
        self.choise = ['rock', 'paper', 'scissor']
        self.random = random.choice(self.choise)
        
        #set button
        self.button = tk.Button(root, text="Submit", command=self.show)
        self.button.pack()
        
        # set label to show the rock, paper or scissor
        self.label1 = tk.Label(root, text="Your choice is ")
        self.label1.pack()
        
        
    def show(self):
        guess = self.entry.get().lower()
        if guess not in self.choise:
            self.label1.config(text="You entered value is invalid")
            return
       
        
if __name__ == "__main__":
    root = tk.Tk()
    obj = main(root)
    root.mainloop()