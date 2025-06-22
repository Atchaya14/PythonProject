import tkinter as tk
from tkinter import messagebox
import math

class ScientificCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Scientific Calculator")
        self.root.geometry("400x650")
        self.root.configure(bg='black')

        self.expression = ""
        self.input_text = tk.StringVar()
        self.create_ui()

    def create_ui(self):
        input_frame = tk.Frame(self.root, bd=10, relief=tk.RIDGE, bg='black')
        input_frame.pack(side=tk.TOP)

        input_field = tk.Entry(input_frame, font=('arial', 20, 'bold'), textvariable=self.input_text,
                               width=30, bg='black', fg='white', bd=10, justify=tk.RIGHT)
        input_field.grid(row=0, column=0)

        btns_frame = tk.Frame(self.root, bg='black')
        btns_frame.pack()

        buttons = [
            ('7', '8', '9', '/'),
            ('4', '5', '6', '*'),
            ('1', '2', '3', '-'),
            ('0', '.', '=', '+'),
            ('sin', 'cos', 'tan', 'log'),
            ('sqrt', 'exp', '(', ')'),
            ('C', 'CE', 'π', 'e')
        ]

        for row_index, row in enumerate(buttons):
            for col_index, btn_text in enumerate(row):
                btn = tk.Button(btns_frame, text=btn_text, font=('arial', 18, 'bold'), bg='white', fg='black',
                                height=2, width=6, bd=5, relief=tk.RAISED,
                                command=lambda x=btn_text: self.on_button_click(x))
                btn.grid(row=row_index, column=col_index, padx=2, pady=2)

    def on_button_click(self, button_text):
        if button_text == "C":
            self.expression = ""
        elif button_text == "CE":
            self.expression = self.expression[:-1]
        elif button_text == "=":
            try:
                self.expression = str(eval(self.expression))
            except Exception:
                messagebox.showerror("Error", "Invalid Input")
                self.expression = ""
        elif button_text == "π":
            self.expression += str(math.pi)
        elif button_text == "e":
            self.expression += str(math.e)
        elif button_text in ('sin', 'cos', 'tan', 'log', 'sqrt', 'exp'):
            try:
                if button_text == 'sin':
                    self.expression = str(math.sin(math.radians(float(self.expression))))
                elif button_text == 'cos':
                    self.expression = str(math.cos(math.radians(float(self.expression))))
                elif button_text == 'tan':
                    self.expression = str(math.tan(math.radians(float(self.expression))))
                elif button_text == 'log':
                    self.expression = str(math.log10(float(self.expression)))
                elif button_text == 'sqrt':
                    self.expression = str(math.sqrt(float(self.expression)))
                elif button_text == 'exp':
                    self.expression = str(math.exp(float(self.expression)))
            except Exception:
                messagebox.showerror("Error", "Invalid Input")
                self.expression = ""
        else:
            self.expression += button_text

        self.input_text.set(self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = ScientificCalculator(root)
    root.mainloop()