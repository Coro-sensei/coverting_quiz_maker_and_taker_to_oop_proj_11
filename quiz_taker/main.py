# Main

from quiz_data import QuizData
from quiz_taker import QuizTaker
from tkinter import messagebox

if __name__ == "__main__":
    quiz_data = QuizData()
    if not quiz_data.questions:
        messagebox.showerror("Error", "No valid questions found!")
    else:
        QuizTaker(quiz_data.questions)
