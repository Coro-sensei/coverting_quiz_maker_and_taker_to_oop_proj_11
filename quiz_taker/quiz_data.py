# Quiz data

import os
from tkinter import messagebox

class QuizData:
    def __init__(self, file_path="quiz_maker_data.txt"):
        self.file_path = file_path
        self.questions = self.load_data()

    def load_data(self):
        if not os.path.exists(self.file_path):
            messagebox.showerror("Error", "Run quiz maker first to create questions!")
            return []

        quiz_data = []
        with open(self.file_path, "r") as f:
            content = f.read().strip()
            blocks = content.split("\n" + "-" * 40 + "\n")

            for block in blocks:
                lines = [line.strip() for line in block.split("\n") if line.strip()]
                if len(lines) < 6:
                    continue
                try:
                    question = lines[0].split("Question: ")[1]
                    options = {
                        'a': lines[1][3:].strip(),
                        'b': lines[2][3:].strip(),
                        'c': lines[3][3:].strip(),
                        'd': lines[4][3:].strip()
                    }
                    correct = lines[5].split(": ")[1].strip().lower()
                    if correct in ['a', 'b', 'c', 'd']:
                        quiz_data.append((question, options, correct))
                except Exception as e:
                    print(f"Error parsing question: {e}")
                    continue

        return quiz_data
