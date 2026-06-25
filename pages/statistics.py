import customtkinter as ctk
import statistics


class StatisticsCalculator(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)

        self.grid_columnconfigure((0, 1), weight=1)

        # Store Numbers
        self.numbers = []

        # =====================
        # TITLE
        # =====================

        title = ctk.CTkLabel(
            self,
            text="Statistics Calculator",
            font=("Segoe UI", 28, "bold")
        )
        title.grid(
            row=0,
            column=0,
            pady=20
        )

        # =====================
        # INPUT SECTION
        # =====================

        input_frame = ctk.CTkFrame(self)
        input_frame.grid(
            row=1,
            column=0,
            padx=20,
            pady=20,
            sticky="nsew"
        )

        ctk.CTkLabel(
            input_frame,
            text="Data Input",
            font=("Segoe UI", 22, "bold")
        ).pack(pady=10)

        ctk.CTkLabel(
            input_frame,
            text="Enter numbers one by one"
        ).pack()

        # =====================
        # NUMBER ENTRY
        # =====================

        entry_frame = ctk.CTkFrame(
            input_frame,
            fg_color="transparent"
        )
        entry_frame.pack(
            fill="x",
            padx=10,
            pady=10
        )

        self.number_entry = ctk.CTkEntry(
            entry_frame,
            height=40,
            placeholder_text="Enter Number"
        )

        self.number_entry.pack(
            side="left",
            fill="x",
            expand=True,
            padx=(0, 10)
        )

        ctk.CTkButton(
            entry_frame,
            text="Add",
            width=100,
            height = 40,
            fg_color="#009432",
            hover_color="#00b894",
            command=self.add_number
        ).pack(side="right")

        # =====================
        # SERIES DISPLAY
        # =====================

        ctk.CTkLabel(
            input_frame,
            text="Series",
            font=("Segoe UI", 18, "bold")
        ).pack(pady=(10, 5))

        self.series_box = ctk.CTkTextbox(
            input_frame,
            height=180
        )

        self.series_box.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        # =====================
        # BUTTONS
        # =====================

        button_frame = ctk.CTkFrame(
            input_frame,
            fg_color="transparent"
        )

        button_frame.pack(pady=10)

        ctk.CTkButton(
            button_frame,
            text="Calculate",
            height=45,
            fg_color="#be2edd",
            hover_color="#9b59b6",
            font=("Segoe UI", 16, "bold"),
            command=self.calculate_statistics
        ).pack(
            side="left",
            padx=10
        )

        ctk.CTkButton(
            button_frame,
            text="Clear",
            height=45,
            fg_color="#e58e26",
            hover_color="#ff793f",
            font=("Segoe UI", 16, "bold"),
            command=self.clear_data
        ).pack(
            side="left",
            padx=10
        )

        # =====================
        # RESULT SECTION
        # =====================

        result_frame = ctk.CTkFrame(self)
        result_frame.grid(
            row=1,
            column=1,
            padx=20,
            pady=20,
            sticky="nsew"
        )

        ctk.CTkLabel(
            result_frame,
            text="Results",
            font=("Segoe UI", 22, "bold")
        ).pack(pady=10)

        self.result_box = ctk.CTkTextbox(
            result_frame,
            height=350
        )

        self.result_box.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

    # =====================
    # ADD NUMBER
    # =====================

    def add_number(self):

        try:

            num = float(
                self.number_entry.get()
            )

            self.numbers.append(num)

            self.series_box.delete(
                "0.0",
                "end"
            )

            self.series_box.insert(
                "end",
                ", ".join(
                    str(n)
                    for n in self.numbers
                )
            )

            self.number_entry.delete(
                0,
                "end"
            )

        except:

            pass

    # =====================
    # CALCULATE
    # =====================

    def calculate_statistics(self):

        self.result_box.delete(
            "0.0",
            "end"
        )

        try:

            numbers = self.numbers.copy()

            if len(numbers) == 0:
                raise ValueError(
                    "No data entered."
                )

            count = len(numbers)
            total = sum(numbers)
            mean = statistics.mean(numbers)
            median = statistics.median(numbers)

            try:
                mode = statistics.mode(numbers)
            except:
                mode = "No Unique Mode"

            variance = (
                statistics.variance(numbers)
                if count > 1
                else 0
            )

            std_dev = (
                statistics.stdev(numbers)
                if count > 1
                else 0
            )

            minimum = min(numbers)
            maximum = max(numbers)
            data_range = maximum - minimum

            result = f"""
Count               : {count}

Sum                 : {total:.2f}

Mean                : {mean:.2f}

Median              : {median:.2f}

Mode                : {mode}

Minimum             : {minimum:.2f}

Maximum             : {maximum:.2f}

Range               : {data_range:.2f}

Variance            : {variance:.2f}

Standard Deviation  : {std_dev:.2f}
"""

            self.result_box.insert(
                "end",
                result
            )

        except Exception as e:

            self.result_box.insert(
                "end",
                f"Error : {e}"
            )

    # =====================
    # CLEAR
    # =====================

    def clear_data(self):

        self.numbers.clear()

        self.number_entry.delete(
            0,
            "end"
        )

        self.series_box.delete(
            "0.0",
            "end"
        )

        self.result_box.delete(
            "0.0",
            "end"
        )