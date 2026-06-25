import customtkinter as ctk


class CurrencyConverter(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)

        # =========================
        # TITLE
        # =========================

        title = ctk.CTkLabel(
            self,
            text="Currency Exchange",
            font=("Segoe UI", 30, "bold")
        )
        title.pack(anchor="w", padx=20, pady=(15, 20))

        # =========================
        # MAIN FRAME
        # =========================

        main_frame = ctk.CTkFrame(self, fg_color="transparent")
        main_frame.pack(fill="both", expand=True, padx=20, pady=10)

        right_panel = ctk.CTkFrame(main_frame)
        right_panel.pack(fill="both", expand=True)

        right_panel.grid_columnconfigure(0, weight=1)
        right_panel.grid_columnconfigure(1, weight=1)

        currencies = [
            "USD", "EUR", "GBP", "INR",
            "JPY", "AUD", "CAD", "CHF",
            "CNY", "SGD"
        ]

        # =========================
        # FROM
        # =========================

        from_label = ctk.CTkLabel(
            right_panel,
            text="From",
            font=("Segoe UI", 18)
        )
        from_label.grid(
            row=0,
            column=0,
            sticky="w",
            padx=20,
            pady=(20, 5)
        )

        self.amount_entry = ctk.CTkEntry(
            right_panel,
            height=45,
            placeholder_text="Enter Amount"
        )
        self.amount_entry.grid(
            row=1,
            column=0,
            padx=(20, 10),
            pady=5,
            sticky="ew"
        )

        self.from_currency = ctk.CTkOptionMenu(
            right_panel,
            fg_color="#303952",
            button_color="#009432",
            button_hover_color="#18A558",
            dropdown_fg_color="#303952",
            dropdown_hover_color="#009432",
            height=45,
            values=currencies
        )
        self.from_currency.set("USD")

        self.from_currency.grid(
            row=1,
            column=1,
            padx=(0, 20),
            pady=5,
            sticky="ew"
        )

        # =========================
        # TO
        # =========================

        to_label = ctk.CTkLabel(
            right_panel,
            text="To",
            font=("Segoe UI", 18)
        )
        to_label.grid(
            row=2,
            column=0,
            sticky="w",
            padx=20,
            pady=(15, 5)
        )

        self.to_currency = ctk.CTkOptionMenu(
            right_panel,
            height=45,
            fg_color="#303952",
            button_color="#b71540",
            button_hover_color="#ff4757",
            dropdown_fg_color="#303952",
            dropdown_hover_color="#ff4757",
            values=currencies
        )
        self.to_currency.set("INR")

        self.to_currency.grid(
            row=3,
            column=0,
            columnspan=2,
            padx=20,
            pady=5,
            sticky="ew"
        )

        # =========================
        # RESULT
        # =========================

        result_title = ctk.CTkLabel(
            right_panel,
            text="Converted Amount",
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
            text="0.00",
            height=55,
            corner_radius=8,
            fg_color=("#1e272e","#ffffff"),
            text_color=("#ffffff","#1e272e"),
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

        # =========================
        # BUTTONS
        # =========================

        convert_btn = ctk.CTkButton(
            right_panel,
            text="Convert",
            height=45,
            fg_color="#009432",
            hover_color="#18A558",
            text_color="#ffffff",
            font=("Segoe UI", 16, "bold"),
            command=self.convert_currency
        )
        convert_btn.grid(
            row=6,
            column=0,
            padx=(20, 10),
            pady=20,
            sticky="ew"
        )

        swap_btn = ctk.CTkButton(
            right_panel,
            text="Swap",
            height=45,
            fg_color="#b71540",
            hover_color="#ff4757",
            text_color="#ffffff",
            font=("Segoe UI", 16, "bold"),
            command=self.swap_currency
        )
        swap_btn.grid(
            row=6,
            column=1,
            padx=(0, 20),
            pady=20,
            sticky="ew"
        )

    # ==================================
    # SWAP
    # ==================================

    def swap_currency(self):

        from_curr = self.from_currency.get()
        to_curr = self.to_currency.get()

        self.from_currency.set(to_curr)
        self.to_currency.set(from_curr)

    # ==================================
    # CONVERT
    # ==================================

    def convert_currency(self):

        try:

            amount = float(self.amount_entry.get())

            # Sample rates relative to USD
            rates = {
                "USD": 1,
                "EUR": 0.86,
                "GBP": 0.74,
                "INR": 85.75,
                "JPY": 144.25,
                "AUD": 1.53,
                "CAD": 1.37,
                "CHF": 0.81,
                "CNY": 7.18,
                "SGD": 1.28
            }

            from_curr = self.from_currency.get()
            to_curr = self.to_currency.get()

            usd_amount = amount / rates[from_curr]
            result = usd_amount * rates[to_curr]

            self.result_label.configure(
                text=f"{result:,.2f} {to_curr}"
            )

        except:
            self.result_label.configure(
                text="Invalid Input"
            )