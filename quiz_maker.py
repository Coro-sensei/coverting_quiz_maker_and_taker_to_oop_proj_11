# Make the quizmakerapp to oop

import os
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import tkinter.font as tkFont
class QuizMaker:
    def __init__(self, root):
        self.root = root