# Submit question

import os
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import tkinter.font as tkFont
from quiz_maker.quiz_maker import QuizMaker

def submit_question(self):
        question = self.entries["question"].get()
        letter_a = self.entries["a"].get()
        letter_b = self.entries["b"].get()
        letter_c = self.entries["c"].get()
        letter_d = self.entries["d"].get()
        correct = self.entries["correct"].get().lower()

        if not all([question, letter_a, letter_b, letter_c, letter_d, correct]):
            messagebox.showerror("Error", "Please fill in all fields")
            return

        if correct not in ['a', 'b', 'c', 'd']:
            messagebox.showerror("Error", "Correct answer must be a, b, c, or d")
            return

        try:
            with open("quiz_maker_data.txt", "a") as f:
                f.write(f"Question: {question}\n")
                f.write(f"a) {letter_a}\n")
                f.write(f"b) {letter_b}\n")
                f.write(f"c) {letter_c}\n")
                f.write(f"d) {letter_d}\n")
                f.write(f"Correct Answer: {correct}\n")
                f.write("-" * 40 + "\n")
            messagebox.showinfo("Success", "Question saved successfully!")
            self.clear_entries()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save question: {str(e)}")
