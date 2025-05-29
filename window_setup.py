# Move the window setup 
import os
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import tkinter.font as tkFont
from quiz_maker import QuizMaker

def setup_window(self):
    screen_width = self.root.winfo_screenwidth()
    screen_height = self.root.winfo_screenheight()

    coord_x = (screen_width - self.window_width) // 2
    coord_y = (screen_height - self.window_height) // 2
    self.root.geometry(f"{self.window_width}x{self.window}+{coord_x}+{coord_y}")

    bg_photo = self.load_image("pokeball_bg.jpeg", (self.window_wiidth, self.window_height))
    if bg_photo:
        tk.Label(self.root, image = bg_photo).place(x = 0, y = 0)
        self.bg_photo = bg_photo

    else:
        self.root.config(bg = "yellow")

