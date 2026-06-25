import customtkinter as ctk
import math


class TrigonometryCalculator(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)

        # ==========================
        # TITLE
        # ==========================

        title = ctk.CTkLabel(
            self,
            text="Trigonometry Calculator",
            font=("Segoe UI", 30, "bold")
        )
        title.pack(anchor="w", padx=20, pady=(15, 20))

        # ==========================
        # MAIN FRAME
        # ==========================

        main_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )
        main_frame.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=10
        )

        right_panel = ctk.CTkFrame(main_frame)
        right_panel.pack(fill="both", expand=True)

        right_panel.grid_columnconfigure(0, weight=1)
        right_panel.grid_columnconfigure(1, weight=1)

        # ==========================
        # ANGLE INPUT
        # ==========================

        angle_label = ctk.CTkLabel(
            right_panel,
            text="Angle / Value",
            font=("Segoe UI", 18)
        )
        angle_label.grid(
            row=0,
            column=0,
            sticky="w",
            padx=20,
            pady=(20, 5)
        )

        self.angle_entry = ctk.CTkEntry(
            right_panel,
            height=45,
            placeholder_text="Enter Angle or Value"
        )
        self.angle_entry.grid(
            row=1,
            column=0,
            padx=(20, 10),
            pady=5,
            sticky="ew"
        )

        # ==========================
        # MODE
        # ==========================

        self.mode_menu = ctk.CTkOptionMenu(
            right_panel,
            height=45,
            fg_color="#b33939",
            button_color="#b33939",
            button_hover_color="#eb4d4b",
            dropdown_fg_color="#303952",
            dropdown_hover_color="#eb4d4b",
            values=["Degree", "Radian"]
        )

        self.mode_menu.set("Degree")

        self.mode_menu.grid(
            row=1,
            column=1,
            padx=(0, 20),
            pady=5,
            sticky="ew"
        )

        # ==========================
        # FUNCTION
        # ==========================

        func_label = ctk.CTkLabel(
            right_panel,
            text="Function",
            font=("Segoe UI", 18)
        )
        func_label.grid(
            row=2,
            column=0,
            sticky="w",
            padx=20,
            pady=(15, 5)
        )

        self.function_menu = ctk.CTkOptionMenu(
            right_panel,
            height=45,
            fg_color="#006266",
            button_color="#006266",
            button_hover_color="#1289A7",
            dropdown_fg_color="#303952",
            dropdown_hover_color="#006266",
            values=[
                "sin",
                "cos",
                "tan",
                "sec",
                "cosec",
                "cot",
                "sin⁻¹",
                "cos⁻¹",
                "tan⁻¹"
            ]
        )

        self.function_menu.grid(
            row=3,
            column=0,
            columnspan=2,
            padx=20,
            pady=5,
            sticky="ew"
        )

        # ==========================
        # RESULT
        # ==========================

        result_title = ctk.CTkLabel(
            right_panel,
            text="Result",
            font=("Segoe UI", 18)
        )
        result_title.grid(
            row=4,
            column=0,
            sticky="w",
            padx=20,
            pady=(15, 5)
        )

        self.result_label = ctk.CTkLabel(
            right_panel,
            text="0",
            height=55,
            corner_radius=8,
            font=("Segoe UI", 24, "bold")
        )

        self.result_label.grid(
            row=5,
            column=0,
            columnspan=2,
            padx=20,
            pady=5,
            sticky="ew"
        )

        # ==========================
        # BUTTONS
        # ==========================

        calc_btn = ctk.CTkButton(
            right_panel,
            text="Calculate",
            height=45,
            fg_color="#3c40c6",
            hover_color="#575fcf",
            font=("Segoe UI", 16, "bold"),
            command=self.calculate
        )

        calc_btn.grid(
            row=6,
            column=0,
            padx=(20, 10),
            pady=20,
            sticky="ew"
        )

        clear_btn = ctk.CTkButton(
            right_panel,
            text="Clear",
            height=45,
            fg_color="#e58e26",
            hover_color="#ff793f",
            font=("Segoe UI", 16, "bold"),
            command=self.clear_fields
        )

        clear_btn.grid(
            row=6,
            column=1,
            padx=(0, 20),
            pady=20,
            sticky="ew"
        )

        # ==========================
        # QUICK ANGLES
        # ==========================

        quick_frame = ctk.CTkFrame(right_panel)

        quick_frame.grid(
            row=7,
            column=0,
            columnspan=2,
            padx=20,
            pady=10,
            sticky="ew"
        )

        quick_angles = [0, 30, 45, 60, 90, 180]

        for angle in quick_angles:

            btn = ctk.CTkButton(
                quick_frame,
                text=f"{angle}°",
                width=80,
                fg_color="#57606f",
                hover_color="#747d8c",
                command=lambda a=angle: self.set_angle(a)
            )

            btn.pack(
                side="left",
                padx=5,
                pady=10
            )

    # ==========================
    # QUICK ANGLES
    # ==========================

    def set_angle(self, angle):

        self.angle_entry.delete(0, "end")
        self.angle_entry.insert(0, str(angle))

    # ==========================
    # CLEAR
    # ==========================

    def clear_fields(self):

        self.angle_entry.delete(0, "end")

        self.result_label.configure(
            text="0"
        )

    # ==========================
    # CALCULATE
    # ==========================

    def calculate(self):

        try:

            value = float(self.angle_entry.get())

            func = self.function_menu.get()
            mode = self.mode_menu.get()

            if mode == "Degree":
                angle = math.radians(value)
            else:
                angle = value

            # --------------------
            # BASIC FUNCTIONS
            # --------------------

            if func == "sin":
                result = math.sin(angle)

            elif func == "cos":
                result = math.cos(angle)

            elif func == "tan":
                result = math.tan(angle)

            elif func == "sec":
                result = 1 / math.cos(angle)

            elif func == "cosec":
                result = 1 / math.sin(angle)

            elif func == "cot":
                result = 1 / math.tan(angle)

            # --------------------
            # INVERSE FUNCTIONS
            # --------------------

            elif func == "sin⁻¹":

                result = math.asin(value)

                if mode == "Degree":
                    result = math.degrees(result)

            elif func == "cos⁻¹":

                result = math.acos(value)

                if mode == "Degree":
                    result = math.degrees(result)

            elif func == "tan⁻¹":

                result = math.atan(value)

                if mode == "Degree":
                    result = math.degrees(result)

            self.result_label.configure(
                text=f"{result:.10f}"
            )

        except Exception:

            self.result_label.configure(
                text="Math Error"
            )