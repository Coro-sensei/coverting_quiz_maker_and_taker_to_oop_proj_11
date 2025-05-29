# Clear entries

import os
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import tkinter.font as tkFont
from quiz_maker.quiz_maker import QuizMaker

def clear_entries(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)