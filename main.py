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
        
if __name__ == "__main__":
    root = tk.Tk()
    obj = main(root)
    root.mainloop()