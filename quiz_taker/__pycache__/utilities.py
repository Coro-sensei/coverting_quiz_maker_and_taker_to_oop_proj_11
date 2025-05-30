# Utilities

from PIL import Image, ImageTk
from tkinter import messagebox

def load_image(path, size=None):
    try:
        image = Image.open(path)
        if size:
            image = image.resize(size, Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(image)
    except Exception as e:
        messagebox.showerror("Image Error", f"Failed to load image at {path}: {str(e)}")
        return None
