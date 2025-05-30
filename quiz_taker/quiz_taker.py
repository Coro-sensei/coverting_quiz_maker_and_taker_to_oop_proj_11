# Quiz taker
import tkinter as tk
from tkinter import messagebox
import tkinter.font as tkFont
from image_helper import ImageHelper

class QuizTaker:
    def __init__(self, quiz_data):
        self.quiz_data = quiz_data
        self.current_question = 0
        self.score = 0
        self.selected_answer = tk.StringVar()
        self.window = tk.Tk()
        self.setup_gui()
        self.show_question()
        self.window.mainloop()

    def setup_gui(self):
        self.window.title("Pokemon Quiz Taker")
        self.window.geometry("1600x800")
        self.window.resizable(False, False)

        # Load background
        bg_photo = ImageHelper.load("pokeball_bg.jpeg", (1600, 800))
        if bg_photo:
            tk.Label(self.window, image=bg_photo).place(x=0, y=0, relwidth=1, relheight=1)
            self.bg_photo = bg_photo  # Prevent garbage collection
        else:
            self.window.configure(bg="yellow")

        # Fonts
        try:
            self.title_font = tkFont.Font(family="Pokemon Hollow", size=48)
            self.question_font = tkFont.Font(family="Kenney Mini Square", size=20)
            self.option_font = tkFont.Font(family="Kenney Mini Square", size=16)
            self.button_font = tkFont.Font(family="Kenney Mini Square", size=18, weight="bold")
        except:
            self.title_font = tkFont.Font(family="Helvetica", size=36, weight="bold")
            self.question_font = tkFont.Font(family="Arial", size=18)
            self.option_font = tkFont.Font(family="Arial", size=14)
            self.button_font = tkFont.Font(family="Arial", size=16, weight="bold")

        # Frame and widgets
        self.frame = tk.Frame(self.window, bg="yellow", width=1200, height=600)
        self.frame.place(relx=0.5, rely=0.5, anchor="center")

        self.question_label = tk.Label(self.frame, font=self.question_font, bg="yellow",
                                    wraplength=1000, justify="left")
        self.question_label.pack(anchor="w", pady=20)

        self.radio_buttons = {}
        for letter in ['a', 'b', 'c', 'd']:
            rb = tk.Radiobutton(self.frame, text="", variable=self.selected_answer,
                                value=letter, font=self.button_font, bg="yellow",
                                anchor="w", justify="left")
            rb.pack(anchor="w", fill='x', padx=20)
            self.radio_buttons[letter] = rb

        self.status_label = tk.Label(self.frame, font=self.option_font, bg="yellow", fg="black")
        self.status_label.pack(pady=20)

        self.submit_button = tk.Button(self.frame, text="Submit Answer", font=self.button_font,
                                    command=self.check_answer)
        self.submit_button.pack(anchor="e", pady=20)

    def show_question(self):
        if self.current_question < len(self.quiz_data):
            question, options, _ = self.quiz_data[self.current_question]
            self.question_label.config(text=f"Question {self.current_question + 1}: {question}")
            for letter in ['a', 'b', 'c', 'd']:
                self.radio_buttons[letter].config(text=f"{letter.upper()}) {options[letter]}")
            self.selected_answer.set("")
            self.status_label.config(text=f"Score: {self.score}/{len(self.quiz_data)}")
        else:
            self.end_quiz()

    def check_answer(self):
        if not self.selected_answer.get():
            messagebox.showwarning("Warning", "Please select an answer!")
            return

        _, _, correct = self.quiz_data[self.current_question]
        if self.selected_answer.get() == correct:
            self.score += 1

        self.current_question += 1
        self.show_question()

    def end_quiz(self):
        self.question_label.config(text="Quiz Completed!")
        for rb in self.radio_buttons.values():
            rb.pack_forget()
        self.submit_button.pack_forget()
        self.status_label.config(text=f"Final Score: {self.score}/{len(self.quiz_data)}")
