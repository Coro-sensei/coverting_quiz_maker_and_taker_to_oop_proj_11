# Create label entry

import os
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import tkinter.font as tkFont
from quiz_maker.quiz_maker import QuizMaker

def create_label_entry(self, label_text, key, row, width=80):
        tk.Label(self.central_frame, text=label_text, font=self.label_font, bg="yellow").grid(row=row, column=0, sticky="e")
        entry = tk.Entry(self.central_frame, width=width, font=self.entry_font)
        entry.grid(row=row, column=1, sticky="w")
        self.entries[key] = entry