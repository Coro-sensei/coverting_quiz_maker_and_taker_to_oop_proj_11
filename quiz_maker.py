# Make the quizmakerapp to oop

import os
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import tkinter.font as tkFont
class QuizMaker:
    def __init__(self, root):
        self.root = root
        self.root.tile("Pokemon Quiz Maker")
        self.window_width = 1600
        self.window_height = 800
        self.root.resizable(False, False)