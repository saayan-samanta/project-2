import customtkinter as ctk


class HealthCalculator(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)

        # =========================
        # TITLE
        # =========================

        title = ctk.CTkLabel(
            self,
            text="BMI Calculator",
            font=("Segoe UI", 28, "bold")
        )
        title.pack(anchor="w", padx=20, pady=(15, 10))

        # =========================
        # MAIN FRAME
        # =========================

        main_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )
        main_frame.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=10
        )

        # =========================
        # LEFT PANEL
        # =========================

        left_panel = ctk.CTkFrame(main_frame)
        left_panel.pack(
            side="left",
            fill="y",
            padx=(0, 10)
        )

        # Weight

        ctk.CTkLabel(
            left_panel,
            text="Weight",
            font=("Segoe UI", 14)
        ).pack(anchor="w", padx=15, pady=(15, 5))

        weight_frame = ctk.CTkFrame(
            left_panel,
            fg_color="transparent"
        )
        weight_frame.pack(fill="x", padx=15)

        self.weight_entry = ctk.CTkEntry(
            weight_frame,
            height=40
        )
        self.weight_entry.pack(
            side="left",
            fill="x",
            expand=True,
            padx=(0, 5)
        )

        self.weight_unit = ctk.CTkOptionMenu(
            weight_frame,
            values=["kg", "lb"],
            width=70,
            fg_color="#5f27cd",
            button_color="#5f27cd",
            button_hover_color="#3498db",
            dropdown_fg_color="#303952",
            dropdown_hover_color="#3498db",
            height=40
        )
        self.weight_unit.set("kg")
        self.weight_unit.pack(side="right")

        # Height

        ctk.CTkLabel(
            left_panel,
            text="Height",
            font=("Segoe UI", 14)
        ).pack(anchor="w", padx=15, pady=(15, 5))

        height_frame = ctk.CTkFrame(
            left_panel,
            fg_color="transparent"
        )
        height_frame.pack(fill="x", padx=15)

        self.height_entry = ctk.CTkEntry(
            height_frame,
            height=40
        )
        self.height_entry.pack(
            side="left",
            fill="x",
            expand=True,
            padx=(0, 5)
        )

        self.height_unit = ctk.CTkOptionMenu(
            height_frame,
            values=["cm", "m", "ft"],
            fg_color="#be2edd",
            button_color="#be2edd",
            button_hover_color="#9b59b6",
            dropdown_fg_color="#303952",
            dropdown_hover_color="#9b59b6",
            width=70,
            height=40
        )
        self.height_unit.set("cm")
        self.height_unit.pack(side="right")

        # Calculate Button

        calc_btn = ctk.CTkButton(
            left_panel,
            text="Calculate BMI",
            height=42,
            fg_color="#1F6F5F",
            hover_color="#1B5E4D",
            command=self.calculate_bmi
        )
        calc_btn.pack(
            fill="x",
            padx=15,
            pady=(20, 8)
        )

        # Clear Button

        clear_btn = ctk.CTkButton(
            left_panel,
            text="Clear",
            height=42,
            fg_color="transparent",
            hover_color="#ff4d4d",
            border_width=1,
            command=self.clear_fields
        )
        clear_btn.pack(
            fill="x",
            padx=15,
            pady=(0, 15)
        )

        # =========================
        # RIGHT PANEL
        # =========================

        right_panel = ctk.CTkFrame(
            main_frame,
            fg_color="transparent"
        )
        right_panel.pack(
            side="left",
            fill="both",
            expand=True
        )

        # BMI Card

        bmi_card = ctk.CTkFrame(
            right_panel,
            corner_radius=12
        )
        bmi_card.pack(fill="x", pady=(0, 10))

        ctk.CTkLabel(
            bmi_card,
            text="Your BMI",
            font=("Segoe UI", 15)
        ).pack(pady=(15, 5))

        self.bmi_value = ctk.CTkLabel(
            bmi_card,
            text="0.00",
            font=("Segoe UI", 32, "bold")
        )
        self.bmi_value.pack(pady=(0, 15))

        # Category Card

        category_card = ctk.CTkFrame(
            right_panel,
            corner_radius=12
        )
        category_card.pack(fill="x")

        ctk.CTkLabel(
            category_card,
            text="Category",
            font=("Segoe UI", 15)
        ).pack(pady=(15, 5))

        self.category_label = ctk.CTkLabel(
            category_card,
            text="-",
            font=("Segoe UI", 28, "bold")
        )
        self.category_label.pack(pady=(0, 15))

        # =========================
        # BMI SCALE
        # =========================

        scale_frame = ctk.CTkFrame(self)
        scale_frame.pack(
            fill="x",
            padx=20,
            pady=(10, 20)
        )

        bmi_info = """
Underweight (<18.5)      Normal (18.5 - 24.9)      Overweight (25 - 29.9)      Obese (30+)
"""

        ctk.CTkLabel(
            scale_frame,
            text=bmi_info,
            font=("Segoe UI", 14)
        ).pack(pady=10)

    # =========================
    # BMI CALCULATION
    # =========================

    def calculate_bmi(self):

        try:

            weight = float(self.weight_entry.get())
            height = float(self.height_entry.get())

            # Weight conversion

            if self.weight_unit.get() == "lb":
                weight = weight * 0.453592

            # Height conversion

            if self.height_unit.get() == "cm":
                height = height / 100

            elif self.height_unit.get() == "ft":
                height = height * 0.3048

            bmi = weight / (height ** 2)

            self.bmi_value.configure(
                text=f"{bmi:.2f}"
            )

            # Category

            if bmi < 18.5:
                category = "Underweight"

            elif bmi < 25:
                category = "Normal"

            elif bmi < 30:
                category = "Overweight"

            else:
                category = "Obese"

            self.category_label.configure(
                text=category
            )

        except:
            self.bmi_value.configure(text="Error")
            self.category_label.configure(text="-")

    # =========================
    # CLEAR
    # =========================

    def clear_fields(self):

        self.weight_entry.delete(0, "end")
        self.height_entry.delete(0, "end")

        self.weight_unit.set("kg")
        self.height_unit.set("cm")

        self.bmi_value.configure(text="0.00")
        self.category_label.configure(text="-")