# Load image
import tkinter as tk 
from PIL import Image, ImageTk
from tkinter import messagebox
from quiz_maker import QuizMaker

def load_image(self, path, size = None):
    try:
        image = Image.open(path)
        if size:
            image = image.resize(size, Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(image)
    except Exception as ex:
        messagebox.showerror("Image Error", f"Failed to load {path}: {str(ex)}")
        return None
