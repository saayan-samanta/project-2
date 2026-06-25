import customtkinter as ctk
from pages.standard import StandardCalculator
from pages.scientific import ScientificCalculator
from pages.trigo import TrigonometryCalculator
from pages.converter import UnitConverter
from pages.currency import CurrencyConverter
from pages.statistics import StatisticsCalculator
from pages.programmer import ProgrammerCalculator
from pages.finance import FinanceCalculator
from pages.health import HealthCalculator
from pages.equation import EquationSolver

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class SmartCalcPro(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("SmartCalc Pro")
        self.geometry("1000x700+300+50")

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.create_sidebar()
        self.create_main_area()

    def create_sidebar(self):

        self.sidebar = ctk.CTkFrame(
            self,
            width=250,
            corner_radius=0,
        )

        self.sidebar.grid(row=0, column=0, sticky="ns")

        logo = ctk.CTkLabel(
            self.sidebar,
            text="🧮 SmartCalc Pro",
            font=("Segoe UI", 24, "bold")
        )

        logo.pack(pady=30,padx=10)

        buttons = [
            ("Calculator", self.show_standard),
            ("Scientific", self.show_scientific),
            ("Trigonometry", self.show_trigonometry),
            ("Converters", self.show_converter),
            ("Currency", self.show_currency),
            ("Statistics", self.show_statistics),
            ("Programmer", self.show_programmer),
            ("Finance", self.show_finance),
            ("Health", self.show_health),
            ("Equation Solver", self.equation_solver),
        ]
        self.menu_buttons = []

        for text, command in buttons:

            btn = ctk.CTkButton(
                self.sidebar,
                text=text,
                height=45,
                command=lambda c=command, t=text:
                self.select_page(c, t)
            )

            btn.pack(fill="x", padx=15, pady=5)

            self.menu_buttons.append((text, btn))

        switch = ctk.CTkSwitch(
            self.sidebar,
            text="Dark Mode",
            command=self.toggle_theme
        )

        switch.select()
        switch.pack(side="bottom", pady=20)

    def create_main_area(self):

        self.content = ctk.CTkFrame(self)
        self.content.grid(row=0, column=1, sticky="nsew")

        self.show_standard()
        self.highlight_button("Calculator")

    def clear_content(self):

        for widget in self.content.winfo_children():
            widget.destroy()

    def highlight_button(self, active_text):
        for text, btn in self.menu_buttons:

            if text == active_text:

                btn.configure(
                    fg_color="#007acc",
                    hover_color="#005f99",
                    text_color= "#ffffff"
                )

            else:

                btn.configure(
                    fg_color=("#f1f2f6", "#3c3c3c"),
                    hover_color=("#dff9fb", "#4d4d4d"),
                    text_color=("#2f3542", "#ffffff")
                )


    def select_page(self, command, button_name):

        self.highlight_button(button_name)
        command()

    def show_standard(self):

        self.clear_content()
        StandardCalculator(self.content).pack(
            fill="both",
            expand=True
        )

    def show_scientific(self):

        self.clear_content()
        ScientificCalculator(self.content).pack(
            fill="both",
            expand=True
        )
    
    def show_trigonometry(self):

        self.clear_content()

        TrigonometryCalculator(self.content).pack(
            fill="both",
            expand=True
        )

    def show_converter(self):

        self.clear_content()

        UnitConverter(self.content).pack(
            fill="both",
            expand=True
        )
        
    def show_currency(self):

        self.clear_content()

        CurrencyConverter(self.content).pack(
            fill="both",
            expand=True
        )

    def show_statistics(self):

        self.clear_content()

        StatisticsCalculator(self.content).pack(
            fill="both",
            expand=True
        )

    def show_programmer(self):

        self.clear_content()

        ProgrammerCalculator(self.content).pack(
            fill="both",
            expand=True
        )

    def show_finance(self):

        self.clear_content()

        FinanceCalculator(self.content).pack(
            fill="both",
            expand=True
        )

    def show_health(self):

        self.clear_content()

        HealthCalculator(self.content).pack(
            fill="both",
            expand=True
        )

    def equation_solver(self):
        self.clear_content()
        
        EquationSolver(self.content).pack(
            fill="both",
            expand=True
        )

    def empty_page(self):

        self.clear_content()

        lbl = ctk.CTkLabel(
            self.content,
            text="Coming Soon...",
            font=("Segoe UI", 40, "bold")
        )

        lbl.pack(expand=True)

    def toggle_theme(self):

        if ctk.get_appearance_mode() == "Dark":
            ctk.set_appearance_mode("light")
        else:
            ctk.set_appearance_mode("dark")


app = SmartCalcPro()
app.mainloop()