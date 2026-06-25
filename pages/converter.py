import customtkinter as ctk


class UnitConverter(ctk.CTkFrame):

    def __init__(self, parent):
     super().__init__(parent)

     self.categories = {
          "Length": [
               "Meter", "Kilometer", "Centimeter",
               "Millimeter", "Inch", "Foot", "Yard", "Mile"
          ],

          "Weight": [
               "Gram", "Kilogram", "Milligram",
               "Pound", "Ounce", "Ton"
          ],

          "Temperature": [
               "Celsius", "Fahrenheit", "Kelvin"
          ],

          "Area": [
               "Square Meter", "Square Kilometer",
               "Square Foot", "Square Yard",
               "Acre", "Hectare"
          ],

          "Volume": [
               "Liter", "Milliliter",
               "Cubic Meter", "Gallon"
          ],

          "Speed": [
               "m/s", "km/h", "mph", "knot"
          ],

          "Time": [
               "Second", "Minute",
               "Hour", "Day"
          ],

          "Pressure": [
               "Pascal", "Bar",
               "PSI", "Atmosphere"
          ],

          "Energy": [
               "Joule", "Kilojoule",
               "Calorie", "Kilocalorie"
          ],

          "Power": [
               "Watt", "Kilowatt",
               "Horsepower"
          ],

          "Data Storage": [
               "Byte", "KB",
               "MB", "GB", "TB"
          ]
     }

     self.category_var = ctk.StringVar(value="Length")

     # ==========================
     # TITLE
     # ==========================

     title = ctk.CTkLabel(
          self,
          text="Unit Converter",
          font=("Segoe UI", 30, "bold")
     )
     title.pack(anchor="w", padx=20, pady=(15, 20))

     # ==========================
     # MAIN FRAME
     # ==========================

     main_frame = ctk.CTkFrame(self, fg_color="transparent")
     main_frame.pack(fill="both", expand=True, padx=20, pady=10)

     # ==========================
     # LEFT PANEL
     # ==========================

     left_panel = ctk.CTkFrame(
          main_frame,
          width=180,
          corner_radius=10
     )
     left_panel.pack(
          side="left",
          fill="y",
          padx=(0, 20)
     )

     category_label = ctk.CTkLabel(
          left_panel,
          text="Category",
          font=("Segoe UI", 18, "bold")
     )
     category_label.pack(
          anchor="w",
          padx=15,
          pady=(15, 10)
     )

     self.category_menu = ctk.CTkOptionMenu(
          left_panel,
          values=list(self.categories.keys()),
          variable=self.category_var,
          command=self.update_units,
          width=150,
          fg_color="#575fcf",
          button_color="#575fcf",
          button_hover_color="#747dff",
          dropdown_fg_color="#303952",
          dropdown_hover_color="#747dff",
     )
     self.category_menu.pack(
          padx=15,
          pady=(0, 15)
     )

     # ==========================
     # RIGHT PANEL
     # ==========================

     right_panel = ctk.CTkFrame(
          main_frame,
          corner_radius=10
     )
     right_panel.pack(
          side="left",
          fill="both",
          expand=True
     )

     right_panel.grid_columnconfigure(0, weight=1)
     right_panel.grid_columnconfigure(1, weight=1)

     # ==========================
     # FROM
     # ==========================

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

     self.value_entry = ctk.CTkEntry(
          right_panel,
          width=220,
          height=45,
          placeholder_text="Enter Value",
     )
     self.value_entry.grid(
          row=1,
          column=0,
          padx=(20, 10),
          pady=5,
          sticky="ew"
     )

     self.from_unit = ctk.CTkOptionMenu(
          right_panel,
          values=self.categories["Length"],
          width=220,
          height=45,
          fg_color="#c23616",
          button_color="#c23616",
          button_hover_color="#e84118",
          dropdown_fg_color="#303952",
          dropdown_hover_color="#eb4d4b",
     )
     self.from_unit.grid(
          row=1,
          column=1,
          padx=(0, 20),
          pady=5,
          sticky="ew"
     )

     # ==========================
     # TO
     # ==========================

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

     self.to_unit = ctk.CTkOptionMenu(
          right_panel,
          values=self.categories["Length"],
          height=45,
          fg_color="#074A1D",
          button_color="#074A1D",
          button_hover_color="#0B6623",
          dropdown_fg_color="#303952",
          dropdown_hover_color="#0B6623",
     )
     self.to_unit.grid(
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

     # ==========================
     # BUTTONS
     # ==========================

     convert_btn = ctk.CTkButton(
          right_panel,
          text="Convert",
          height=45,
          fg_color="#F79F1F",
          hover_color="#ff9f43",
          font=("Segoe UI", 16, "bold"),
          command=self.convert
     )
     convert_btn.grid(
          row=6,
          column=0,
          padx=(20, 10),
          pady=20,
          sticky="ew"
     )

    def update_units(self, choice):

        units = self.categories[choice]

        self.from_unit.configure(values=units)
        self.to_unit.configure(values=units)

        self.from_unit.set(units[0])
        self.to_unit.set(units[1])

    def convert(self):

     try:

          value = float(self.value_entry.get())

          category = self.category_var.get()
          from_u = self.from_unit.get()
          to_u = self.to_unit.get()

          result = 0

          # Conversion Tables

          length = {
               "Meter": 1,
               "Kilometer": 1000,
               "Centimeter": 0.01,
               "Millimeter": 0.001,
               "Inch": 0.0254,
               "Foot": 0.3048,
               "Yard": 0.9144,
               "Mile": 1609.344
          }

          weight = {
               "Gram": 0.001,
               "Kilogram": 1,
               "Milligram": 0.000001,
               "Pound": 0.453592,
               "Ounce": 0.0283495,
               "Ton": 1000
          }

          area = {
               "Square Meter": 1,
               "Square Kilometer": 1000000,
               "Square Foot": 0.092903,
               "Square Yard": 0.836127,
               "Acre": 4046.86,
               "Hectare": 10000
          }

          volume = {
               "Liter": 1,
               "Milliliter": 0.001,
               "Cubic Meter": 1000,
               "Gallon": 3.78541
          }

          speed = {
               "m/s": 1,
               "km/h": 0.277778,
               "mph": 0.44704,
               "knot": 0.514444
          }

          time_units = {
               "Second": 1,
               "Minute": 60,
               "Hour": 3600,
               "Day": 86400
          }

          pressure = {
               "Pascal": 1,
               "Bar": 100000,
               "PSI": 6894.76,
               "Atmosphere": 101325
          }

          energy = {
               "Joule": 1,
               "Kilojoule": 1000,
               "Calorie": 4.184,
               "Kilocalorie": 4184
          }

          power = {
               "Watt": 1,
               "Kilowatt": 1000,
               "Horsepower": 745.7
          }

          data = {
               "Byte": 1,
               "KB": 1024,
               "MB": 1024**2,
               "GB": 1024**3,
               "TB": 1024**4
          }

          # Length
          if category == "Length":
               result = value * length[from_u] / length[to_u]

          # Weight
          elif category == "Weight":
               result = value * weight[from_u] / weight[to_u]

          # Area
          elif category == "Area":
               result = value * area[from_u] / area[to_u]

          # Volume
          elif category == "Volume":
               result = value * volume[from_u] / volume[to_u]

          # Speed
          elif category == "Speed":
               result = value * speed[from_u] / speed[to_u]

          # Time
          elif category == "Time":
               result = value * time_units[from_u] / time_units[to_u]

          # Pressure
          elif category == "Pressure":
               result = value * pressure[from_u] / pressure[to_u]

          # Energy
          elif category == "Energy":
               result = value * energy[from_u] / energy[to_u]

          # Power
          elif category == "Power":
               result = value * power[from_u] / power[to_u]

          # Data Storage
          elif category == "Data Storage":
               result = value * data[from_u] / data[to_u]

          # Temperature
          elif category == "Temperature":

               if from_u == "Celsius":
                    c = value

               elif from_u == "Fahrenheit":
                    c = (value - 32) * 5 / 9

               else:  # Kelvin
                    c = value - 273.15

               if to_u == "Celsius":
                    result = c

               elif to_u == "Fahrenheit":
                    result = (c * 9 / 5) + 32

               else:
                    result = c + 273.15

          self.result_label.configure(
                 text=f"{round(result, 8):,}"
          )

     except Exception as e:

          print("Conversion Error:", e)

          self.result_label.configure(
               text="Invalid Input"
          )