# Entry Point 

import os
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import tkinter.font as tkFont
from quiz_maker import QuizMaker

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizMakerApp(root)
    root.mainloop()
