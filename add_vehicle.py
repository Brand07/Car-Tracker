import os
import json

import customtkinter
import pandas as pd


class VehicleAdder(customtkinter.CTk):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.parent = parent
        self.title("Add Vehicle")
        self.geometry("400x500")
        self.resizable(False, False)

        # Configure the grid layout with 5 rows and 5 columns
        for _ in range(6):
            self.grid_rowconfigure(_, weight=1)
            self.grid_columnconfigure(_, weight=1)

        # Vehicle Brand Label and Entry
        self.vehicle_brand_label = customtkinter.CTkLabel(self, text="Vehicle Brand")
        self.vehicle_brand_label.grid(row=0, column=0, padx=10, pady=10)
        self.vehicle_brand_entry = customtkinter.CTkEntry(self)
        self.vehicle_brand_entry.grid(row=0, column=1, padx=10, pady=10)

        # Vehicle Model Label and Entry
        self.vehicle_model_label = customtkinter.CTkLabel(self, text="Vehicle Model")
        self.vehicle_model_label.grid(row=1, column=0, padx=10, pady=10)
        self.vehicle_model_entry = customtkinter.CTkEntry(self)
        self.vehicle_model_entry.grid(row=1, column=1, padx=10, pady=10)

        # Vehicle Year Label and Entry
        self.vehicle_year_label = customtkinter.CTkLabel(self, text="Vehicle Year")
        self.vehicle_year_label.grid(row=2, column=0, padx=10, pady=10)
        self.vehicle_year_entry = customtkinter.CTkEntry(self)
        self.vehicle_year_entry.grid(row=2, column=1, padx=10, pady=10)

        # Vehicle Mileage Label and Entry
        self.vehicle_mileage_label = customtkinter.CTkLabel(
            self, text="Vehicle Mileage"
        )
        self.vehicle_mileage_label.grid(row=3, column=0, padx=10, pady=10)
        self.vehicle_mileage_entry = customtkinter.CTkEntry(self)
        self.vehicle_mileage_entry.grid(row=3, column=1, padx=10, pady=10)

        # Vehicle Nickname Label and Entry
        self.vehicle_nickname_label = customtkinter.CTkLabel(
            self, text="Vehicle Nickname"
        )
        self.vehicle_nickname_label.grid(row=4, column=0, padx=10, pady=10)
        self.vehicle_nickname_entry = customtkinter.CTkEntry(self)
        self.vehicle_nickname_entry.grid(row=4, column=1, padx=10, pady=10)

        # Submit Button
        self.submit_button = customtkinter.CTkButton(
            self, text="Submit", command=self.handle_submit_button
        )
        self.submit_button.grid(row=6, column=0, columnspan=3, padx=10, pady=10)

    def handle_submit_button(self):
        vehicle = {
            "Nickname": self.vehicle_nickname_entry.get(),
            "Brand": self.vehicle_brand_entry.get(),
            "Model": self.vehicle_model_entry.get(),
            "Year": self.vehicle_year_entry.get(),
            "Mileage": self.vehicle_mileage_entry.get(),
        }

        if not os.path.isfile("Resources/vehicles.json"):
            vehicles = pd.DataFrame(
                columns=["Nickname", "Brand", "Model", "Year", "Mileage"]
            )
            vehicles.to_json("Resources/vehicles.json", orient="records")

        try:
            vehicles = pd.read_json("Resources/vehicles.json")
        except ValueError:
            vehicles = pd.DataFrame(
                columns=["Nickname", "Brand", "Model", "Year", "Mileage"]
            )

        vehicles = pd.concat([vehicles, pd.DataFrame([vehicle])], ignore_index=True)

        with open("Resources/vehicles.json", "w") as file:
            json.dump(vehicles.to_dict(orient="records"), file, indent=4)

        # Update the combo box in the parent window
        self.parent.load_vehicles()

        self.destroy()
