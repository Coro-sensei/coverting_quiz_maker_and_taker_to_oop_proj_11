# User Interface

import tkinter as tk
from tkinter import messagebox
from utilities import load_image, load_fonts
from data_manager import QuizManager

class QuizMakerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Pokemon Quiz Maker")
        self.root.geometry("1600x800")
        self.root.resizable(False, False)

        self.manager = QuizManager()
        self.label_font, self.entry_font, self.button_font = load_fonts()

        self.background_image = load_image("assets/pokeball_bg.jpeg", (1600, 800))
        self.title_image = load_image("assets/pokeball_title.png", (550, 250))

        self.setup_ui()

    def setup_ui(self):
        if self.background_image:
            tk.Label(self.root, image=self.background_image).place(x=0, y=0)
        else:
            self.root.config(bg="yellow")

        if self.title_image:
            tk.Label(self.root, image=self.title_image, bg="yellow").place(relx=0.5, rely=0.2, anchor="center")
        else:
            tk.Label(self.root, text="Pokemon Quiz Maker", font=("Arial", 24), bg="yellow").place(relx=0.5, rely=0.2, anchor="center")

        self.form_frame = tk.Frame(self.root, bg="yellow")
        self.form_frame.place(relx=0.5, rely=0.5, anchor="center")

        self.entries = {}
        fields = [
            "Question",
            "Option A",
            "Option B",
            "Option C",
            "Option D",
            "Correct Answer (a/b/c/d)"
        ]
        for index, field_label in enumerate(fields):
            tk.Label(self.form_frame, text=field_label + ":", font=self.label_font, bg="yellow").grid(row=index, column=0, sticky="e")
            input_entry = tk.Entry(self.form_frame, width=80 if index < 5 else 10, font=self.entry_font)
            input_entry.grid(row=index, column=1, sticky="w")
            self.entries[field_label] = input_entry

        tk.Button(self.form_frame, text="Submit", font=self.button_font, command=self.submit).grid(row=6, column=1, sticky="e")
        tk.Button(self.form_frame, text="Clear", font=self.button_font, command=self.clear_entries).grid(row=6, column=0, sticky="w")

    def submit(self):
        question_text = self.entries["Question"].get()
        option_a_text = self.entries["Option A"].get()
        option_b_text = self.entries["Option B"].get()
        option_c_text = self.entries["Option C"].get()
        option_d_text = self.entries["Option D"].get()
        correct_answer_letter = self.entries["Correct Answer (a/b/c/d)"].get().lower()

        if not all([question_text, option_a_text, option_b_text, option_c_text, option_d_text, correct_answer_letter]):
            messagebox.showerror("Error", "Please fill all fields")
            return

        if correct_answer_letter not in ['a', 'b', 'c', 'd']:
            messagebox.showerror("Error", "Correct answer must be a, b, c, or d")
            return

        self.manager.save_question(
            question_text,
            {
                'a': option_a_text,
                'b': option_b_text,
                'c': option_c_text,
                'd': option_d_text
            },
            correct_answer_letter
        )
        messagebox.showinfo("Saved", "Question saved successfully!")
        self.clear_entries()

    def clear_entries(self):
        for entry_widget in self.entries.values():
            entry_widget.delete(0, tk.END)
