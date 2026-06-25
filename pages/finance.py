import customtkinter as ctk


class FinanceCalculator(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)

        # ====================================
        # TITLE
        # ====================================

        title = ctk.CTkLabel(
            self,
            text="EMI Calculator",
            font=("Segoe UI", 28, "bold")
        )
        title.pack(anchor="w", padx=20, pady=(15, 10))

        # ====================================
        # MAIN FRAME
        # ====================================

        main_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )
        main_frame.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=(0, 15)
        )

        # ====================================
        # LEFT PANEL
        # ====================================

        left_panel = ctk.CTkFrame(
            main_frame,
            corner_radius=12
        )

        left_panel.pack(
            side="left",
            fill="both",
            padx=(0, 10),
            pady=5
        )

        # Loan Amount

        loan_label = ctk.CTkLabel(
            left_panel,
            text="Loan Amount (₹)",
            font=("Segoe UI", 14)
        )
        loan_label.pack(anchor="w", padx=15, pady=(15, 5))

        self.loan_entry = ctk.CTkEntry(
            left_panel,
            height=40,
            placeholder_text="Enter Loan Amount"
        )
        self.loan_entry.pack(fill="x", padx=15)

        # Interest Rate

        rate_label = ctk.CTkLabel(
            left_panel,
            text="Interest Rate (%)",
            font=("Segoe UI", 14)
        )
        rate_label.pack(anchor="w", padx=15, pady=(15, 5))

        self.rate_entry = ctk.CTkEntry(
            left_panel,
            height=40,
            placeholder_text="Enter Interest Rate"
        )
        self.rate_entry.pack(fill="x", padx=15)

        # Loan Tenure

        tenure_label = ctk.CTkLabel(
            left_panel,
            text="Loan Tenure",
            font=("Segoe UI", 14)
        )
        tenure_label.pack(anchor="w", padx=15, pady=(15, 5))

        tenure_frame = ctk.CTkFrame(
            left_panel,
            fg_color="transparent"
        )
        tenure_frame.pack(fill="x", padx=15)

        self.tenure_entry = ctk.CTkEntry(
            tenure_frame,
            height=40
        )
        self.tenure_entry.pack(
            side="left",
            fill="x",
            expand=True,
            padx=(0, 5)
        )

        self.tenure_type = ctk.CTkOptionMenu(
            tenure_frame,
            height=40,
            fg_color="#B53471",
            button_color="#B53471",
            button_hover_color="#e84393",
            dropdown_fg_color="#303952",
            dropdown_hover_color="#FC427B",
            values=["Years", "Months"],
            width=100
        )
        self.tenure_type.set("Years")

        self.tenure_type.pack(side="right")

        # Calculate Button

        calculate_btn = ctk.CTkButton(
            left_panel,
            text="Calculate EMI",
            height=42,
            fg_color="#c56cf0",
            hover_color="#a55eea",
            command=self.calculate_emi
        )
        calculate_btn.pack(
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

        # ====================================
        # RIGHT PANEL
        # ====================================

        right_panel = ctk.CTkFrame(
            main_frame,
            fg_color="transparent"
        )

        right_panel.pack(
            side="left",
            fill="both",
            expand=True,
            pady=5
        )

        # EMI CARD

        emi_card = ctk.CTkFrame(
            right_panel,
            corner_radius=12
        )
        emi_card.pack(fill="x", pady=(0, 10))

        ctk.CTkLabel(
            emi_card,
            text="Monthly EMI",
            font=("Segoe UI", 15)
        ).pack(pady=(15, 5))

        self.emi_value = ctk.CTkLabel(
            emi_card,
            text="₹ 0.00",
            font=("Segoe UI", 30, "bold")
        )
        self.emi_value.pack(pady=(0, 15))

        # INTEREST CARD

        interest_card = ctk.CTkFrame(
            right_panel,
            corner_radius=12
        )
        interest_card.pack(fill="x", pady=(0, 10))

        ctk.CTkLabel(
            interest_card,
            text="Total Interest",
            font=("Segoe UI", 15)
        ).pack(pady=(15, 5))

        self.interest_value = ctk.CTkLabel(
            interest_card,
            text="₹ 0.00",
            font=("Segoe UI", 24, "bold")
        )
        self.interest_value.pack(pady=(0, 15))

        # TOTAL PAYMENT CARD

        total_card = ctk.CTkFrame(
            right_panel,
            corner_radius=12
        )
        total_card.pack(fill="x")

        ctk.CTkLabel(
            total_card,
            text="Total Amount",
            font=("Segoe UI", 15)
        ).pack(pady=(15, 5))

        self.total_value = ctk.CTkLabel(
            total_card,
            text="₹ 0.00",
            font=("Segoe UI", 24, "bold")
        )
        self.total_value.pack(pady=(0, 15))

    # ====================================
    # EMI CALCULATION
    # ====================================

    def calculate_emi(self):

        try:

            principal = float(self.loan_entry.get())
            annual_rate = float(self.rate_entry.get())
            tenure = float(self.tenure_entry.get())

            if self.tenure_type.get() == "Years":
                months = tenure * 12
            else:
                months = tenure

            monthly_rate = annual_rate / (12 * 100)

            emi = (
                principal *
                monthly_rate *
                (1 + monthly_rate) ** months
            ) / (
                (1 + monthly_rate) ** months - 1
            )

            total_payment = emi * months
            total_interest = total_payment - principal

            self.emi_value.configure(
                text=f"₹ {emi:,.2f}"
            )

            self.interest_value.configure(
                text=f"₹ {total_interest:,.2f}"
            )

            self.total_value.configure(
                text=f"₹ {total_payment:,.2f}"
            )

        except Exception:

            self.emi_value.configure(text="Error")
            self.interest_value.configure(text="Error")
            self.total_value.configure(text="Error")

    # ====================================
    # CLEAR
    # ====================================

    def clear_fields(self):

        self.loan_entry.delete(0, "end")
        self.rate_entry.delete(0, "end")
        self.tenure_entry.delete(0, "end")

        self.tenure_type.set("Years")

        self.emi_value.configure(text="₹ 0.00")
        self.interest_value.configure(text="₹ 0.00")
        self.total_value.configure(text="₹ 0.00")