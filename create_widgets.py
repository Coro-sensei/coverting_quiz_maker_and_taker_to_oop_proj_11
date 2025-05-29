# Create widgets

import os
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import tkinter.font as tkFont
from quiz_maker import QuizMaker

def create_widget(self):
        self.central_frame = tk.Frame(self.root, bg="yellow")
        self.central_frame.place(relx=0.5, rely=0.5, anchor="center")

        title_image = self.load_image("pokeball_title.png", (550, 250))
        if title_image:
                title_label = tk.Label(self.root, image=title_image, bg="yellow")
                title_label.image = title_image  # prevent garbage collection
        else:
                title_label = tk.Label(self.root, text="Pokemon Quiz Maker", font=("Kenney Mini Square", 24), bg="yellow")
        title_label.place(relx=0.5, rely=0.2, anchor="center")

        self.entries = {}
        self.create_label_entry("Enter your question:", "question", 0)
        self.create_label_entry("Option A:", "a", 1)
        self.create_label_entry("Option B:", "b", 2)
        self.create_label_entry("Option C:", "c", 3)
        self.create_label_entry("Option D:", "d", 4)
        self.create_label_entry("Correct answer (a/b/c/d):", "correct", 5, width=10)

        submit_btn = tk.Button(self.central_frame, text="Submit", font=self.button_font, command=self.submit_question)
        submit_btn.grid(row=6, column=1, sticky="e")

        clear_btn = tk.Button(self.central_frame, text="Clear All", font=self.button_font, command=self.clear_entries)
        clear_btn.grid(row=6, column=0, sticky="e")