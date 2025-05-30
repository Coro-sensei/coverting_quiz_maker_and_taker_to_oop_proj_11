# Utilities 

from PIL import Image, ImageTk
from tkinter import messagebox, font

def load_image(path, size=None):
    try:
        image = Image.open(path)
        if size:
            image = image.resize(size, Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(image)
    except Exception as error:
        messagebox.showerror("Image Error", f"Failed to load {path}: {error}")
        return None

def load_fonts():
    try:
        label_font = font.Font(family="Kenney Mini Square", size=16)
        entry_font = font.Font(family="Kenney Mini Square", size=14)
        button_font = font.Font(family="Kenney Mini Square", size=16, weight="bold")
    except:
        label_font = font.Font(size=16)
        entry_font = font.Font(size=14)
        button_font = font.Font(size=16, weight="bold")
    return label_font, entry_font, button_font
