import tkinter as tk
from tkinter import messagebox

class Puzzle(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Puzzle Game - Python")
        self.buttons = []
        self.create_buttons()

    def create_buttons(self):
        positions = [(0, 0), (1, 0), (2, 0),
                     (0, 1), (1, 1), (2, 1),
                     (0, 2), (1, 2), (2, 2)]
        values = ["1", " ", "3", "4", "5", "6", "7", "8", "2"]
        for i in range(9):
            button = tk.Button(self, text=values[i], width=6, height=3)
            button.config(command=lambda button=button: self.button_click(button))
            button.grid(row=positions[i][0], column=positions[i][1])
            self.buttons.append(button)

        next_button = tk.Button(self, text="Next", width=10, height=3, bg="black", fg="green", command=self.next_button_click)
        next_button.grid(row=3, column=1, columnspan=2)

    def button_click(self, button):
        button_index = self.buttons.index(button)
        empty_button_index = self.buttons.index(" ")
        if self.is_adjacent(button_index, empty_button_index):
            self.buttons[button_index], self.buttons[empty_button_index] = self.buttons[empty_button_index], self.buttons[button_index]
            self.update_buttons()
            self.check_win()

    def next_button_click(self):
        self.buttons[1], self.buttons[8] = self.buttons[8], self.buttons[1]
        self.buttons[0], self.buttons[4] = self.buttons[4], self.buttons[0]
        self.buttons[3], self.buttons[6] = self.buttons[6], self.buttons[3]
        self.update_buttons()
        self.check_win()

    def update_buttons(self):
        for i in range(9):
            self.buttons[i].config(text=self.buttons[i])

    def is_adjacent(self, index1, index2):
        positions = [(0, 0), (1, 0), (2, 0),
                     (0, 1), (1, 1), (2, 1),
                     (0, 2), (1, 2), (2, 2)]
        x1, y1 = positions[index1]
        x2, y2 = positions[index2]
        return abs(x1 - x2) + abs(y1 - y2) == 1

    def check_win(self):
        if self.buttons[0] == "1" and self.buttons[1] == "2" and self.buttons[2] == "3" and \
            self.buttons[3] == "4" and self.buttons[4] == "5" and self.buttons[5] == "6" and \
            self.buttons[6] == "7" and self.buttons[7] == "8" and self.buttons[8] == " ":
            messagebox.showinfo("Congratulations!", "You won!")

if __name__ == "__main__":
    puzzle = Puzzle()
    puzzle.mainloop()
