# Load image
import os
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import tkinter.font as tkFont
from quiz_maker.quiz_maker import QuizMaker

def load_image(self, path, size = None):
    try:
        image = Image.open(path)
        if size:
            image = image.resize(size, Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(image)
    except Exception as ex:
        messagebox.showerror("Image Error", f"Failed to load {path}: {str(ex)}")
        return None
