# Application itself

import tkinter as tk
from quiz_window import QuizWindow
from quiz_data_loader import load_quiz_data

class QuizTakerApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Pokemon Quiz Taker")
        self.root.geometry("1600x800")
        self.root.resizable(False, False)

        self.quiz_data = load_quiz_data()
        if not self.quiz_data:
            raise ValueError("No valid quiz data found.")

        self.quiz_window = QuizWindow(self.root, self.quiz_data)

    def run(self):
        self.quiz_window.show_question()
        self.root.mainloop()
