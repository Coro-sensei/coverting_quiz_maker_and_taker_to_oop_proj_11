# Utilities for images 

from PIL import Image, ImageTk
from tkinter import messagebox

def load_image(path, size=None):
    try:
        image = Image.open(path)
        if size:
            image = image.resize(size, Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(image)
    except Exception as error:
        messagebox.showerror("Image Error", f"Failed to load {path}: {str(error)}")
        return None
