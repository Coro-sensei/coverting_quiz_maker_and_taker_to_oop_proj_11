# Loader of the quiz taker

import os
from tkinter import messagebox

def load_quiz_data(file_path="quiz_maker_data.txt"):
    quiz_data = []

    if not os.path.exists(file_path):
        messagebox.showerror("Error", "Run quiz maker first to create questions!")
        return []

    with open(file_path, "r") as file:
        content = file.read().strip()
        question_blocks = content.split("\n" + "-" * 40 + "\n")

    for block in question_blocks:
        lines = [line.strip() for line in block.split("\n") if line.strip()]
        if len(lines) < 6:
            continue

        try:
            question_text = lines[0].split("Question: ")[1]
            options = {
                'a': lines[1][3:].strip(),
                'b': lines[2][3:].strip(),
                'c': lines[3][3:].strip(),
                'd': lines[4][3:].strip(),
            }
            correct_answer = lines[5].split(": ")[1].strip().lower()
            quiz_data.append((question_text, options, correct_answer))
        except Exception:
            continue

    return quiz_data
