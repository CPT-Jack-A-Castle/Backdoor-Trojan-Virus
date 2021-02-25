import tkinter as tk


class CalculatorGUI(tk.Frame):
    expression = ''

    def __init__(self, parent, *args, **kwargs):
        self.input_text = tk.StringVar()
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        parent.title("Totally not a Distraction!!")
        parent.geometry("312x324")
        parent.resizable(0, 0)

        # Centering Window
        window_width = parent.winfo_reqwidth()
        window_height = parent.winfo_reqheight()

        position_right = int(parent.winfo_screenwidth() / 2 - window_width / 2)
        position_down = int(parent.winfo_screenheight() / 4 - window_height / 2)

        parent.geometry("+{}+{}".format(position_right, position_down))

        # Input Field
        input_frame = tk.Frame(self, width=312, height=50, bd=0, highlightbackground="#ccc", highlightcolor="#ccc",
                               highlightthickness=2)
        input_frame.pack(side=tk.TOP)
        input_field = tk.Entry(input_frame, font=('arial', 18, 'bold'), textvariable=self.input_text, width=50,
                               bg="#ccc", bd=0,
                               justify=tk.RIGHT)
        input_field.grid(row=0, column=0)
        input_field.config(state="disabled")  # This stops a user from typing in the input field
        input_field.pack(ipady=10)

        # Buttons
        btn_frame = tk.Frame(self, width=312, height=274, bg="#ccc")
        btn_frame.pack()

        # first row
        clear = tk.Button(btn_frame, text="C", fg="black", width=32, height=3, bd=0, bg="#d9d9d9", cursor="hand2",
                          command=lambda: self.clear_expression()).grid(row=0, column=0, columnspan=3, padx=1, pady=1)
        divide = tk.Button(btn_frame, text="/", fg="black", width=10, height=3, bd=0, bg="#d9d9d9", cursor="hand2",
                           command=lambda: self.append("/")).grid(row=0, column=3, padx=1, pady=1)

        # second row
        seven = tk.Button(btn_frame, text="7", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                          command=lambda: self.append(7)).grid(row=1, column=0, padx=1, pady=1)
        eight = tk.Button(btn_frame, text="8", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                          command=lambda: self.append(8)).grid(row=1, column=1, padx=1, pady=1)
        nine = tk.Button(btn_frame, text="9", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                         command=lambda: self.append(9)).grid(row=1, column=2, padx=1, pady=1)
        multiply = tk.Button(btn_frame, text="*", fg="black", width=10, height=3, bd=0, bg="#d9d9d9", cursor="hand2",
                             command=lambda: self.append("*")).grid(row=1, column=3, padx=1, pady=1)

        # third row
        four = tk.Button(btn_frame, text="4", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                         command=lambda: self.append(4)).grid(row=2, column=0, padx=1, pady=1)
        five = tk.Button(btn_frame, text="5", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                         command=lambda: self.append(5)).grid(row=2, column=1, padx=1, pady=1)
        six = tk.Button(btn_frame, text="6", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                        command=lambda: self.append(6)).grid(row=2, column=2, padx=1, pady=1)
        minus = tk.Button(btn_frame, text="-", fg="black", width=10, height=3, bd=0, bg="#d9d9d9", cursor="hand2",
                          command=lambda: self.append("-")).grid(row=2, column=3, padx=1, pady=1)

        # fourth row
        one = tk.Button(btn_frame, text="1", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                        command=lambda: self.append(1)).grid(row=3, column=0, padx=1, pady=1)
        two = tk.Button(btn_frame, text="2", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                        command=lambda: self.append(2)).grid(row=3, column=1, padx=1, pady=1)
        three = tk.Button(btn_frame, text="3", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                          command=lambda: self.append(3)).grid(row=3, column=2, padx=1, pady=1)
        plus = tk.Button(btn_frame, text="+", fg="black", width=10, height=3, bd=0, bg="#d9d9d9", cursor="hand2",
                         command=lambda: self.append("+")).grid(row=3, column=3, padx=1, pady=1)

        # fifth row
        blank = tk.Button(btn_frame, fg="black", width=10, height=3, bd=0, bg="#d9d9d9", cursor="arrow",
                          state=tk.DISABLED).grid(row=4, column=0, padx=1, pady=1)
        zero = tk.Button(btn_frame, text="0", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                         command=lambda: self.append(0)).grid(row=4, column=1, padx=1, pady=1)
        point = tk.Button(btn_frame, text=".", fg="black", width=10, height=3, bd=0, bg="#d9d9d9", cursor="hand2",
                          command=lambda: self.append(".")).grid(row=4, column=2, padx=1, pady=1)
        equals = tk.Button(btn_frame, text="=", fg="black", width=10, height=3, bd=0, bg="#d9d9d9", cursor="hand2",
                           command=lambda: self.calculate()).grid(row=4, column=3, padx=1, pady=1)

        self.pack(side="top", fill="both", expand=True)
        parent.mainloop()
    # Functions

    # Append to expression
    def append(self, item):
        self.expression = self.expression + str(item)
        self.input_text.set(self.expression)

    # Clear expression
    def clear_expression(self):
        self.expression = ""
        self.input_text.set("")

    # Calculate expression
    def calculate(self):
        result = str(eval(self.expression))  # 'eval':This function is used to evaluates the string expression directly
        self.input_text.set(result)
        self.expression = result


if __name__ == "__main__":
    root = tk.Tk()
    CalculatorGUI(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
