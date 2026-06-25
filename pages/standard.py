import customtkinter as ctk


class StandardCalculator(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(parent)

        self.expression = ""

        self.display = ctk.CTkEntry(
            self,
            height=100,
            fg_color=("black", "white"),   # Light Mode, Dark Mode
            text_color=("white", "black"),
            font=("Segoe UI", 40)
        )

        self.display.pack(
            fill="x",
            padx=20,
            pady=20
        )

        keypad = ctk.CTkFrame(self)
        keypad.pack()

        buttons = [
            ['AC', '(', ')', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', '.', '=', '%']
        ]

        for r, row in enumerate(buttons):

            for c, text in enumerate(row):

                # Orange buttons
                if text in ['+', '-', '*', '/', '%']:
                    btn_color = "#FF9500"
                    hover = "#E68600"

                # Blue buttons
                elif text in ['AC', '=', '(', ')']:
                    btn_color = "#0078D7"
                    hover = "#0063B1"

                # Black buttons
                else:
                    btn_color = "#192a56"
                    hover = "#273c75"    

                btn = ctk.CTkButton(
                    keypad,
                    text=text,
                    width=120,
                    height=80,
                    fg_color=btn_color,
                    hover_color=hover,
                    font=("Segoe UI", 25),
                    command=lambda t=text:
                    self.click(t)
                )

                btn.grid(
                    row=r,
                    column=c,
                    padx=5,
                    pady=5
                )

    def click(self, value):

        if value == "=":

            try:
                result = str(eval(self.expression))
                self.display.delete(0, "end")
                self.display.insert(0, result)
                self.expression = result

            except:
                self.display.delete(0, "end")
                self.display.insert(0, "Error")

        elif value == "AC":

            self.expression = ""
            self.display.delete(0, "end")

        else:

            self.expression += value

            self.display.delete(0, "end")
            self.display.insert(
                0,
                self.expression
            )