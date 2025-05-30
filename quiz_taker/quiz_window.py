# Quiz taker UI

import tkinter as tk
from tkinter import messagebox
from tkinter import font as tkFont
from utilities import load_image

class QuizWindow:
    def __init__(self, root, quiz_data):
        self.root = root
        self.quiz_data = quiz_data
        self.current_index = 0
        self.score = 0
        self.selected_answer = tk.StringVar()

        self.set_fonts()
        self.setup_background()
        self.setup_frame()
        self.create_widgets()

    def set_fonts(self):
        try:
            self.title_font = tkFont.Font(family="Pokemon Hollow", size=48)
            self.question_font = tkFont.Font(family="Kenney Mini Square", size=20)
            self.option_font = tkFont.Font(family="Kenney Mini Square", size=16)
            self.button_font = tkFont.Font(family="Kenney Mini Square", size=18, weight="bold")
        except:
            self.title_font = tkFont.Font(family="Arial", size=36, weight="bold")
            self.question_font = tkFont.Font(family="Arial", size=18)
            self.option_font = tkFont.Font(family="Arial", size=14)
            self.button_font = tkFont.Font(family="Arial", size=16, weight="bold")

    def setup_background(self):
        background_image = load_image("pokeball_bg.jpeg", (1600, 800))
        if background_image:
            tk.Label(self.root, image=background_image).place(x=0, y=0, relwidth=1, relheight=1)
            self.root.bg_image = background_image
        else:
            self.root.configure(bg="yellow")

    def setup_frame(self):
        self.frame = tk.Frame(self.root, bg="yellow", width=1200, height=600)
        self.frame.place(relx=0.5, rely=0.5, anchor="center")

    def create_widgets(self):
        self.question_label = tk.Label(self.frame, font=self.question_font, bg="yellow", wraplength=1000, justify="left")
        self.question_label.pack(anchor="w", pady=20)

        self.radio_buttons = {}
        for letter in ['a', 'b', 'c', 'd']:
            radio_button = tk.Radiobutton(
                self.frame,
                text="",
                variable=self.selected_answer,
                value=letter,
                font=self.button_font,
                bg="yellow",
                anchor="w",
                justify="left"
            )
            radio_button.pack(anchor="w", fill='x', padx=20)
            self.radio_buttons[letter] = radio_button

        self.status_label = tk.Label(self.frame, font=self.option_font, bg="yellow", fg="black")
        self.status_label.pack(pady=20)

        self.submit_button = tk.Button(self.frame, text="Submit Answer", font=self.button_font, command=self.check_answer)
        self.submit_button.pack(anchor="e", pady=20)

    def show_question(self):
        if self.current_index < len(self.quiz_data):
            question_text, options, _ = self.quiz_data[self.current_index]
            self.question_label.config(text=f"Question {self.current_index + 1}: {question_text}")
            for key in ['a', 'b', 'c', 'd']:
                self.radio_buttons[key].config(text=f"{key.upper()}) {options[key]}")
            self.selected_answer.set("")
            self.status_label.config(text=f"Score: {self.score}/{len(self.quiz_data)}")
        else:
            self.end_quiz()

    def check_answer(self):
        if not self.selected_answer.get():
            messagebox.showwarning("Warning", "Please select an answer!")
            return

        _, _, correct_answer = self.quiz_data[self.current_index]
        if self.selected_answer.get() == correct_answer:
            self.score += 1
        self.current_index += 1
        self.show_question()

    def end_quiz(self):
        self.question_label.config(text="Quiz Completed!")
        for radio_button in self.radio_buttons.values():
            radio_button.pack_forget()
        self.submit_button.pack_forget()
        self.status_label.config(text=f"Final Score: {self.score}/{len(self.quiz_data)}")
