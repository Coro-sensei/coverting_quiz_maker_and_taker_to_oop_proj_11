# Main

import tkinter as tk
from tkinter import messagebox
from tkinter import font as tkFont
from PIL import ImageTk
from data_manager import QuizManager
from utilities import load_image
import os


if __name__ == "__main__":
    root = tk.Tk()
    app = QuizMakerGUI(root)
    root.mainloop()

