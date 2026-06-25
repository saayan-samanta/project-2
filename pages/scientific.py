import customtkinter as ctk
import math


class ScientificCalculator(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(parent)

        self.expression = ""
        self.display_text = ""

        self.display = ctk.CTkEntry(
            self,
            height=100,
            font=("Segoe UI", 40),
            fg_color=("black", "white"),
            text_color=("white", "black"),
            justify="right"
        )

        self.display.pack(
            fill="x",
            padx=20,
            pady=20
        )

        buttons = [
            ['sin', 'cos', 'tan', 'log', 'ln', '(', ')'],
            ['√', '∛', 'x²', 'x³', 'xʸ', 'AC', 'C'],
            ['7', '8', '9', '/', '!', 'π', 'e'],
            ['4', '5', '6', '*', '10ˣ', '', ''],
            ['1', '2', '3', '-', 'eˣ', '', ''],
            ['0', '.', '=', '+', '%', '', '']
        ]

        keypad = ctk.CTkFrame(self)
        keypad.pack(fill="both", expand=True, padx=20, pady=20)

        for col in range(7):
            keypad.grid_columnconfigure(col, weight=1)

        for row in range(6):
            keypad.grid_rowconfigure(row, weight=1)

        for r, row in enumerate(buttons):

            for c, text in enumerate(row):

                if text == "":
                    continue

                # Orange operators
                if text in ['+', '-', '*', '/', '=']:
                    color = "#FF9500"
                    hover = "#E68600"

                # Blue scientific functions
                elif text in [
                    'sin', 'cos', 'tan',
                    'log', 'ln',
                    '√', '∛',
                    'x²', 'x³', 'xʸ',
                    '10ˣ', 'eˣ',
                    'π', 'e',
                    '!'
                ]:
                    color = "#0078D7"
                    hover = "#0063B1"

                # Red clear buttons
                elif text in ['AC', 'C']:
                    color = "#D83B01"
                    hover = "#B83200"

                # Black numbers
                else:
                    color = "#192a56"
                    hover = "#273c75"

                btn = ctk.CTkButton(
                    keypad,
                    text=text,
                    font=("Segoe UI", 22),
                    height=70,
                    fg_color=color,
                    hover_color=hover,
                    command=lambda t=text: self.click(t)
                )

                btn.grid(
                    row=r,
                    column=c,
                    padx=5,
                    pady=5,
                    sticky="nsew"
                )

    def click(self, value):

        if value == "=":

            try:

                open_brackets = self.expression.count("(")
                close_brackets = self.expression.count(")")

                self.expression += ")" * (open_brackets - close_brackets)

                result = str(
                    round(
                        eval(self.expression, {"math": math}),
                        10
                    )
                )

                self.display.delete(0, "end")
                self.display.insert(0, result)

                self.expression = result
                self.display_text = result

            except Exception as e:

                print(e)

                self.display.delete(0, "end")
                self.display.insert(0, "Error")

                self.expression = ""
                self.display_text = ""

        elif value == "AC":

            self.expression = ""
            self.display_text = ""

            self.display.delete(0, "end")

        elif value == "C":

            self.expression = self.expression[:-1]
            self.display_text = self.display_text[:-1]

            self.display.delete(0, "end")

        elif value == "π":

            self.expression += str(math.pi)
            self.display_text += "π"

        elif value == "e":

            self.expression += str(math.e)
            self.display_text += "e"

        elif value == "√":

            self.expression += "math.sqrt("
            self.display_text += "√("

        elif value == "∛":

            self.expression += "("
            self.display_text += "∛("

        elif value == "x²":

            self.expression += "**2"
            self.display_text += "²"

        elif value == "x³":

            self.expression += "**3"
            self.display_text += "³"

        elif value == "xʸ":

            self.expression += "**"
            self.display_text += "^"

        elif value == "log":

            self.expression += "math.log10("
            self.display_text += "log("

        elif value == "ln":

            self.expression += "math.log("
            self.display_text += "ln("

        elif value == "10ˣ":

            self.expression += "10**("
            self.display_text += "10^("

        elif value == "eˣ":

            self.expression += "math.exp("
            self.display_text += "e^("

        elif value == "!":

            try:
                num = int(eval(self.expression, {"math": math}))
                result = str(math.factorial(num))

                self.expression = result
                self.display_text += "!"

                self.display.delete(0, "end")
                self.display.insert(0, result)

                return

            except:
                self.display.delete(0, "end")
                self.display.insert(0, "Error")

                self.expression = ""
                self.display_text = ""
                return

        elif value == "sin":

            self.expression += "math.sin(math.radians("
            self.display_text += "sin("

        elif value == "cos":

            self.expression += "math.cos(math.radians("
            self.display_text += "cos("

        elif value == "tan":

            self.expression += "math.tan(math.radians("
            self.display_text += "tan("

        elif value == ")":

            self.expression += ")"
            self.display_text += ")"

        else:

            self.expression += value
            self.display_text += value

        self.display.delete(0, "end")
        self.display.insert(0, self.display_text)