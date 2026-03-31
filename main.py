import tkinter as tk
from tkinter import Tk
import random

class main:
    def __init__(self, root):
        self.root = root
        
        # set title to the window
        self.root.title(text="Game of Rock Paper Scissor")
        
        # set diamentions to window
        self.root.geometry("700x500")
        