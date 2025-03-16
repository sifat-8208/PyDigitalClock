import tkinter as tk
from time import strftime

class DigitalClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Digital Clock")
        self.root.configure(bg="#2E3B4E")
        self.root.resizable(False, False) 

        self.time_label = tk.Label(
            self.root,
            font=("Arial", 50, "bold"),
            background="#2E3B4E",
            foreground="#FFFFFF", 
            padx=20,
            pady=20
        )
        self.time_label.pack(anchor="center")

        self.update_time()

    def update_time(self):
        current_time = strftime("%I:%M:%S %p")
        self.time_label.config(text=current_time) 
        self.time_label.after(1000, self.update_time) 


root = tk.Tk()
clock = DigitalClock(root)
root.mainloop()
