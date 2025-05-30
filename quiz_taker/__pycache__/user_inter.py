# User Interface
import tkinter as tk
from tkinter import messagebox
import tkinter.font as tkFont
from questions import Question
from utilities import load_image

class QuizMakerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pokemon Quiz Maker")
        self.window_width = 1600
        self.window_height = 800
        self.configure_window()
        self.create_fonts()
        self.setup_background()
        self.create_widgets()

    def configure_window(self):
        self.root.geometry(f"{self.window_width}x{self.window_height}")
        self.root.resizable(False, False)
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - self.window_width) // 2
        y = (screen_height - self.window_height) // 2
        self.root.geometry(f"{self.window_width}x{self.window_height}+{x}+{y}")

    def create_fonts(self):
        try:
            self.label_font = tkFont.Font(family="Kenney Mini Square", size=16)
            self.entry_font = tkFont.Font(family="Kenney Mini Square", size=14)
            self.button_font = tkFont.Font(family="Kenney Mini Square", size=16, weight="bold")
        except:
            self.label_font = tkFont.Font(size=16)
            self.entry_font = tkFont.Font(size=14)
            self.button_font = tkFont.Font(size=16, weight="bold")

    def setup_background(self):
        bg_image = load_image("pokeball_bg.jpeg", (self.window_width, self.window_height))
        if bg_image:
            tk.Label(self.root, image=bg_image).place(x=0, y=0)
            self.root.bg_image = bg_image  # prevent garbage collection
        else:
            self.root.config(bg="yellow")

    def create_widgets(self):
        self.central_frame = tk.Frame(self.root, bg="yellow")
        self.central_frame.place(relx=0.5, rely=0.5, anchor="center")

        title_image = load_image("pokeball_title.png", (550, 250))
        if title_image:
            tk.Label(self.root, image=title_image, bg="yellow").place(relx=0.5, rely=0.2, anchor="center")
            self.root.title_image = title_image
        else:
            tk.Label(self.root, text="Pokemon Quiz Maker", font=self.label_font, bg="yellow").place(relx=0.5, rely=0.2, anchor="center")

        self.entries = {}
        self.add_label_entry("Enter your question:", "question", 0)
        self.add_label_entry("Option A:", "a", 1)
        self.add_label_entry("Option B:", "b", 2)
        self.add_label_entry("Option C:", "c", 3)
        self.add_label_entry("Option D:", "d", 4)
        self.add_label_entry("Correct answer (a/b/c/d):", "correct", 5, short=True)

        submit_btn = tk.Button(self.central_frame, text="Submit", font=self.button_font, command=self.submit_question)
        submit_btn.grid(row=6, column=1, sticky="e")

        clear_btn = tk.Button(self.central_frame, text="Clear All", font=self.button_font, command=self.clear_entries)
        clear_btn.grid(row=6, column=0, sticky="e")

    def add_label_entry(self, label_text, key, row, short=False):
        tk.Label(self.central_frame, text=label_text, font=self.label_font, bg="yellow").grid(row=row, column=0, sticky="e")
        entry_width = 10 if short else 80
        entry = tk.Entry(self.central_frame, width=entry_width, font=self.entry_font)
        entry.grid(row=row, column=1, sticky="w")
        self.entries[key] = entry

    def submit_question(self):
        question_text = self.entries["question"].get().strip()
        options = {
            "a": self.entries["a"].get().strip(),
            "b": self.entries["b"].get().strip(),
            "c": self.entries["c"].get().strip(),
            "d": self.entries["d"].get().strip(),
        }
        correct = self.entries["correct"].get().strip().lower()

        question = Question(question_text, options, correct)

        if not question.is_valid():
            messagebox.showerror("Error", "Please fill all fields and provide a valid correct answer (a/b/c/d)")
            return

        try:
            with open("quiz_maker_data.txt", "a") as file:
                file.write(question.to_text())
            messagebox.showinfo("Success", "Question saved successfully!")
            self.clear_entries()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save: {e}")

    def clear_entries(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)