import customtkinter as ctk


class ProgrammerCalculator(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)

        self.grid_columnconfigure((0, 1), weight=1)

        # =========================
        # TITLE
        # =========================

        title = ctk.CTkLabel(
            self,
            text="Programmer Calculator",
            font=("Segoe UI", 28, "bold")
        )
        title.grid(row=0, column=0, pady=20)

        # =========================
        # CONVERSION SECTION
        # =========================

        conversion_frame = ctk.CTkFrame(self)
        conversion_frame.grid(
            row=1,
            column=0,
            padx=20,
            pady=20,
            sticky="nsew"
        )

        ctk.CTkLabel(
            conversion_frame,
            text="Number Converter",
            font=("Segoe UI", 20, "bold")
        ).pack(pady=10)

        self.number_entry = ctk.CTkEntry(
            conversion_frame,
            height=40
        )
        self.number_entry.pack(
            fill="x",
            padx=10,
            pady=10
        )

        self.base_option = ctk.CTkOptionMenu(
            conversion_frame,
            fg_color="#ffa502",
            button_color="#ffa502",
            button_hover_color="#ff6348",
            dropdown_fg_color="#303952",
            dropdown_hover_color="#ffa502",
            values=[
                "Decimal",
                "Binary",
                "Octal",
                "Hexadecimal"
            ]
        )

        self.base_option.pack(
            padx=10,
            pady=10
        )

        ctk.CTkButton(
            conversion_frame,
            fg_color="#3c40c6",
            hover_color="#5758BB",
            text="Convert",
            command=self.convert_number
        ).pack(
            padx=10,
            pady=10
        )

        self.result_box = ctk.CTkTextbox(
            conversion_frame,
            height=200
        )

        self.result_box.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        # =========================
        # BITWISE SECTION
        # =========================

        bitwise_frame = ctk.CTkFrame(self)
        bitwise_frame.grid(
            row=1,
            column=1,
            padx=20,
            pady=20,
            sticky="nsew"
        )

        ctk.CTkLabel(
            bitwise_frame,
            text="Bitwise Operations",
            font=("Segoe UI", 20, "bold")
        ).pack(pady=10)

        self.a_entry = ctk.CTkEntry(
            bitwise_frame,
            placeholder_text="Value A"
        )
        self.a_entry.pack(
            fill="x",
            padx=10,
            pady=5
        )

        self.b_entry = ctk.CTkEntry(
            bitwise_frame,
            placeholder_text="Value B"
        )
        self.b_entry.pack(
            fill="x",
            padx=10,
            pady=5
        )

        self.operation = ctk.CTkOptionMenu(
            bitwise_frame,
            fg_color="#ffa502",
            button_color="#ffa502",
            button_hover_color="#ff6348",
            dropdown_fg_color="#303952",
            dropdown_hover_color="#ffa502",
            values=[
                "AND",
                "OR",
                "XOR",
                "NOT",
                "LEFT SHIFT",
                "RIGHT SHIFT"
            ]
        )

        self.operation.pack(
            padx=10,
            pady=10
        )

        ctk.CTkButton(
            bitwise_frame,
            text="Calculate",
            fg_color="#3c40c6",
            hover_color="#5758BB",
            command=self.bitwise_calculation
        ).pack(
            padx=10,
            pady=10
        )

        self.bitwise_result = ctk.CTkLabel(
            bitwise_frame,
            text="Result : ",
            font=("Segoe UI", 18)
        )

        self.bitwise_result.pack(
            pady=20
        )

    # ==================================
    # NUMBER CONVERSION
    # ==================================

    def convert_number(self):

        self.result_box.delete("0.0", "end")

        try:

            number = self.number_entry.get()
            mode = self.base_option.get()

            if mode == "Decimal":

                value = int(number)

            elif mode == "Binary":

                value = int(number, 2)

            elif mode == "Octal":

                value = int(number, 8)

            elif mode == "Hexadecimal":

                value = int(number, 16)

            result = f"""
Decimal     : {value}

Binary      : {bin(value)[2:]}

Octal       : {oct(value)[2:]}

Hexadecimal : {hex(value)[2:].upper()}
"""

            self.result_box.insert("end", result)

        except Exception as e:

            self.result_box.insert(
                "end",
                f"Error : {e}"
            )

    # ==================================
    # BITWISE OPERATIONS
    # ==================================

    def bitwise_calculation(self):

        try:

            a = int(self.a_entry.get())

            operation = self.operation.get()

            if operation == "NOT":

                result = ~a

            else:

                b = int(self.b_entry.get())

                if operation == "AND":
                    result = a & b

                elif operation == "OR":
                    result = a | b

                elif operation == "XOR":
                    result = a ^ b

                elif operation == "LEFT SHIFT":
                    result = a << b

                elif operation == "RIGHT SHIFT":
                    result = a >> b

            self.bitwise_result.configure(
                text=f"Result : {result}"
            )

        except Exception as e:

            self.bitwise_result.configure(
                text=f"Error : {e}"
            )