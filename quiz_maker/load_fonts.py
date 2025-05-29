# Loading fonts

import os
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import tkinter.font as tkFont
from quiz_maker.quiz_maker import QuizMaker

def load_fonts(self):
    try: 
        self.label_font = tkFont.Font(family="Kenney Mini Square", size=16)
        self.entry_font = tkFont.Font(family="Kenney Mini Square", size=14)
        self.button_font = tkFont.Font(family="Kenney Mini Square", size=16, weight="bold")
    except:
            self.label_font = tkFont.Font(size=16)
            self.entry_font = tkFont.Font(size=14)
            self.button_font = tkFont.Font(size=16, weight="bold")
