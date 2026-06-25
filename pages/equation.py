import customtkinter as ctk
from sympy import Eq, solve, sympify
from tkinter import messagebox


class EquationSolver(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)

        # ==========================
        # TITLE
        # ==========================

        title = ctk.CTkLabel(
            self,
            text="Equation Solver",
            font=("Segoe UI", 28, "bold")
        )
        title.pack(anchor="w", padx=20, pady=(15, 10))

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
            padx=15,
            pady=(0, 15)
        )

        # ==========================
        # LEFT PANEL
        # ==========================

        left_panel = ctk.CTkFrame(main_frame)
        left_panel.pack(
            side="left",
            fill="both",
            expand=True,
            padx=(0, 10)
        )

        ctk.CTkLabel(
            left_panel,
            text="Enter Equation",
            font=("Segoe UI", 14)
        ).pack(anchor="w", padx=15, pady=(15, 5))

        self.equation_entry = ctk.CTkEntry(
            left_panel,
            height=45,
            placeholder_text="Example: x**2 - 5*x + 6 = 0"
        )

        self.equation_entry.pack(
            fill="x",
            padx=15
        )

        # ==========================
        # BUTTONS
        # ==========================

        solve_btn = ctk.CTkButton(
            left_panel,
            text="Solve",
            fg_color="#8a2be2",
            hover_color="#7a1fe0",
            height=42,
            command=self.solve_equation
        )

        solve_btn.pack(
            fill="x",
            padx=15,
            pady=(15, 5)
        )

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

        # ==========================
        # SOLUTION SECTION
        # ==========================

        ctk.CTkLabel(
            left_panel,
            text="Solution",
            font=("Segoe UI", 16, "bold")
        ).pack(anchor="w", padx=15)

        self.solution_label = ctk.CTkLabel(
            left_panel,
            text="?",
            font=("Segoe UI", 28, "bold")
        )

        self.solution_label.pack(
            pady=40
        )

        # ==========================
        # RIGHT PANEL
        # ==========================

        right_panel = ctk.CTkFrame(main_frame)

        right_panel.pack(
            side="left",
            fill="both",
            expand=True
        )

        ctk.CTkLabel(
            right_panel,
            text="Steps",
            font=("Segoe UI", 16, "bold")
        ).pack(
            anchor="w",
            padx=15,
            pady=(15, 10)
        )

        self.steps_box = ctk.CTkTextbox(
            right_panel,
            height=350
        )

        self.steps_box.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=(0, 15)
        )

    # ==========================
    # CLEAR FIELDS
    # ==========================

    def clear_fields(self):

        confirm = messagebox.askyesno(
            "Clear",
            "Do you want to clear all fields?"
        )

        if confirm:
            self.equation_entry.delete(0, "end")
            self.solution_label.configure(text="?")
            self.steps_box.delete("1.0", "end")

    # ==========================
    # SOLVE EQUATION
    # ==========================

    def solve_equation(self):

        try:

            equation = self.equation_entry.get().strip()

            if "=" not in equation:
                raise ValueError(
                    "Equation must contain '='"
                )

            left, right = equation.split("=")

            # Convert to SymPy expressions
            left_expr = sympify(left)
            right_expr = sympify(right)

            eq = Eq(
                left_expr,
                right_expr
            )

            # Detect variables automatically
            variables = list(
                eq.free_symbols
            )

            if not variables:
                raise ValueError(
                    "No variable detected"
                )

            # Solve equation
            solutions = solve(
                eq,
                variables
            )

            # =====================
            # DISPLAY SOLUTION
            # =====================

            if isinstance(solutions, dict):

                solution_text = "\n".join(
                    f"{var} = {val}"
                    for var, val in solutions.items()
                )

            elif isinstance(solutions, list):

                if len(solutions) == 0:

                    solution_text = "No Solution"

                else:

                    variable_name = str(
                        variables[0]
                    )

                    formatted = []

                    for sol in solutions:

                        formatted.append(
                            f"{variable_name} = {sol}"
                        )

                    solution_text = "\n".join(
                        formatted
                    )

            else:

                solution_text = str(
                    solutions
                )

            self.solution_label.configure(
                text=solution_text
            )

            # =====================
            # DISPLAY STEPS
            # =====================

            self.steps_box.delete(
                "1.0",
                "end"
            )

            steps = f"""
Given Equation:

{equation}

--------------------------------------------------

Detected Variables:
{", ".join(str(v) for v in variables)}

--------------------------------------------------

Standard Form:

{left_expr} = {right_expr}

--------------------------------------------------

Solutions:

{solution_text}
"""

            self.steps_box.insert(
                "end",
                steps
            )

        except Exception as e:

            self.solution_label.configure(
                text="Invalid"
            )

            self.steps_box.delete(
                "1.0",
                "end"
            )

            self.steps_box.insert(
                "end",
                f"""Error:

{e}

Examples:

2*x + 5 = 15
x**2 - 5*x + 6 = 0
(x+1)/2 = 5
3*y + 7 = 22
"""
            )


# ==========================
# TESTING
# ==========================

if __name__ == "__main__":

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    root = ctk.CTk()
    root.title("Equation Solver")
    root.geometry("1000x600")

    solver = EquationSolver(root)
    solver.pack(fill="both", expand=True)

    root.mainloop()