# Move the window setup 

def setup_window(self):
    screen_width = self.root.winfo_screenwidth()
    screen_height = self.root.winfo_screenheight()

    coord_x = (screen_width - self.window_width) // 2
    coord_y = (screen_height - self.window_height) // 2
    self.root.geometry(f"{self.window_width}x{self.window}+{coord_x}+{coord_y}")
    