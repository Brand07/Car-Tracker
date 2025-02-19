import tkinter
import customtkinter
from picker import CTkDatePicker
import pandas as pd
import os

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

class VehicleAdder(customtkinter.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Add Vehicle")
        self.geometry("400x500")
        self.resizable(False, False)

        # Configure the grid layout with 5 rows and 5 columns
        for _ in range (6):
            self.grid_rowconfigure(_, weight=1)
            self.grid_columnconfigure(_, weight=1)

        # Vehicile Brand Label and Entry
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
        self.vehicle_mileage_label = customtkinter.CTkLabel(self, text="Vehicle Mileage")
        self.vehicle_mileage_label.grid(row=3, column=0, padx=10, pady=10)
        self.vehicle_mileage_entry = customtkinter.CTkEntry(self)
        self.vehicle_mileage_entry.grid(row=3, column=1, padx=10, pady=10)

        # Vehicle Nickname Label and Entry
        self.vehicle_nickname_label = customtkinter.CTkLabel(self, text="Vehicle Nickname")
        self.vehicle_nickname_label.grid(row=4, column=0, padx=10, pady=10)
        self.vehicle_nickname_entry = customtkinter.CTkEntry(self)
        self.vehicle_nickname_entry.grid(row=4, column=1, padx=10, pady=10)



        # Submit Button
        self.submit_button = customtkinter.CTkButton(self, text="Submit", command=self.handle_submit_button)
        self.submit_button.grid(row=6, column=0, columnspan=3, padx=10, pady=10)

    def handle_submit_button(self):
        vehicle = {
            "Nickname": self.vehicle_nickname_entry.get(),
            "Brand": self.vehicle_brand_entry.get(),
            "Model": self.vehicle_model_entry.get(),
            "Year": self.vehicle_year_entry.get(),
            "Mileage": self.vehicle_mileage_entry.get(),

        }

        if not os.path.isfile("vehicles.json"):
            vehicles = pd.DataFrame(columns=["Nickname", "Brand", "Model", "Year", "Mileage"])
            vehicles.to_json("vehicles.json", orient="records")

        vehicles = pd.read_json("vehicles.json")
        vehicles = pd.concat([vehicles, pd.DataFrame([vehicle])], ignore_index=True)

        with open("vehicles.json", "w") as file:
            json.dump(vehicles.to_dict(orient="records"), file, indent=4)

        self.destroy()



class App(customtkinter.CTk):

    HEIGHT = 600
    WIDTH = 800

    def __init__(self, *args, **kwargs):
        super().__init__()
        self.title("Vehicle Fuel Efficiency Tracker")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.resizable(False, False)

        self.top_frame = customtkinter.CTkFrame(self, width=800, height=100)
        self.top_frame.place(x=0, y=0)


        self.Frame1 = customtkinter.CTkFrame(self, width=800, height=240)
        self.Frame1.place(x=0, y=360)

        self.odometer_button = customtkinter.CTkButton(self, bg_color=['gray86', 'gray17'],fg_color="blue", text="Current Odometer Reading", hover=False, font=customtkinter.CTkFont('Roboto', size=13, weight='bold'))
        self.odometer_button.place(x=80, y=380)

        self.odometer_entry = customtkinter.CTkEntry(self, bg_color=['gray86', 'gray17'], width=160)
        self.odometer_entry.place(x=80, y=420)

        self.fuel_price_button = customtkinter.CTkButton(self, bg_color=['gray86', 'gray17'],fg_color="blue", text="Fuel Price", hover=False, width=160, font=customtkinter.CTkFont('Roboto', size=13, weight='bold'))
        self.fuel_price_button.place(x=80, y=480)

        self.fuel_price_entry = customtkinter.CTkEntry(self, bg_color=['gray86', 'gray17'], width=160)
        self.fuel_price_entry.place(x=80, y=520)

        self.total_gallons_button = customtkinter.CTkButton(self, bg_color=['gray86', 'gray17'],fg_color="blue", text="Total Gallons Purchased", hover=False, width=160, font=customtkinter.CTkFont('Roboto', size=13, weight='bold'))
        self.total_gallons_button.place(x=320, y=380)

        self.Entry3 = customtkinter.CTkEntry(self, bg_color=['gray86', 'gray17'], width=160)
        self.Entry3.place(x=320, y=420)

        self.total_cost_button = customtkinter.CTkButton(self, bg_color=['gray86', 'gray17'],fg_color="blue", text="Total Cost", hover=False, width=160, font=customtkinter.CTkFont('Roboto', size=13, weight='bold'))
        self.total_cost_button.place(x=320, y=480)

        self.total_cost_entry = customtkinter.CTkEntry(self, bg_color=['gray86', 'gray17'], width=160)
        self.total_cost_entry.place(x=320, y=520)

        self.submit_button = customtkinter.CTkButton(self, bg_color=['gray86', 'gray17'], font=customtkinter.CTkFont('Roboto', size=26, weight='bold'), height=50, text="Submit", fg_color="#00b900", text_color="#000000", command=self.handle_submit_button)
        self.submit_button.place(x=655, y=545)

        self.date_picker_label = customtkinter.CTkButton(self, bg_color=['gray86', 'gray17'],fg_color="blue", text="Select a Date", hover=False, width=160, font=customtkinter.CTkFont('Roboto', size=13, weight='bold'))
        self.date_picker_label.place(x=550, y=380)

        self.date_combobox = customtkinter.CTkComboBox(self)
        self.date_combobox.place(x=550, y=420)

        CTkDatePicker(self.date_combobox)

        self.vehicle_combo = customtkinter.CTkComboBox(self, values=[], bg_color=['gray86', 'gray17'], justify="center")
        self.vehicle_combo.place(x=10, y=35)

        self.select_vehicle_label = customtkinter.CTkLabel(self, bg_color=['gray86', 'gray17'], text="Select a vehicle")
        self.select_vehicle_label.place(x=30, y=2)

        self.add_vehicle_button = customtkinter.CTkButton(self, bg_color=['gray86', 'gray17'], text="Add Vehicle", command=self.open_vehicle_adder)
        self.add_vehicle_button.place(x=650, y=10)

        self.load_vehicles()

    def load_vehicles(self):
        if os.path.isfile("vehicles.json"):
            vehicles = pd.read_json("vehicles.json")
            vehicle_names = vehicles["Nickname"].tolist()
            self.vehicle_combo.configure(values=vehicle_names)

    def open_vehicle_adder(self):
        self.vehicle_adder = VehicleAdder()
        self.vehicle_adder.mainloop()




        # Check if the CSV file exists before initializing the DataFrame
        if not os.path.isfile("fill_ups.csv"):
            fill_ups = pd.DataFrame(columns=["Date", "Odometer", "Gallons", "Gas Price", "Total Cost"])
            fill_ups.to_csv("fill_ups.csv", index=False)

    def handle_submit_button(self):
        """Handles the submit button click"""

        odometer = self.odometer_entry.get()
        # Check if the entry is a number
        try:
            odometer = int(odometer)
        except ValueError:
            print("Odometer reading must be a number. Please try again.")
            self.odometer_button.configure(fg_color="red")
            # Clear the entry
            self.odometer_entry.delete(0, tkinter.END)
            return

        # Check if the odometer reading is less than what it was before
        fill_ups = pd.read_csv("fill_ups.csv")
        if len(fill_ups) > 0:
            if int(odometer) < fill_ups["Odometer"].iloc[-1]:
                print("Odometer reading must be greater than the previous reading. Please try again.")
                # Clear the entry
                self.odometer_button.configure(fg_color="red")
                self.odometer_entry.delete(0, tkinter.END)
                return
            else:
                self.odometer_button.configure(fg_color="blue")

        fuel_price = self.fuel_price_entry.get()
        # Check if the entry is a number or float
        try:
            fuel_price = float(fuel_price)
        except ValueError:
            print("Fuel price must be a number. Please try again.")
            self.fuel_price_button.configure(fg_color="red")
            # Clear the entry
            self.fuel_price_entry.delete(0, tkinter.END)
            return
        # Check if the fuel price is less than or equal to zero
        if float(fuel_price) <= 0:
            self.fuel_price_button.configure(fg_color="red")
            print("Fuel price must be greater than zero. Please try again.")
            # Clear the entry
            self.fuel_price_entry.delete(0, tkinter.END)
            return
        else:
            self.fuel_price_button.configure(fg_color="blue")

        total_gallons = self.Entry3.get()
        # Check if the entry is a number or float
        try:
            total_gallons = float(total_gallons)
        except ValueError:
            print("Total gallons must be a number. Please try again.")
            # Clear the entry
            self.Entry3.delete(0, tkinter.END)
        # Check if the total gallons is less than or equal to zero
        if float(total_gallons) <= 0:
            print("Total gallons must be greater than zero. Please try again.")
            # Clear the entry
            self.Entry3.delete(0, tkinter.END)
            return

        total_cost = self.total_cost_entry.get()
        # Check if the entry is a number or float
        try:
            total_cost = float(total_cost)
        except ValueError:
            print("Total cost must be a number. Please try again.")
            # Clear the entry
            self.total_cost_entry.delete(0, tkinter.END)
            return
        # Check if the total cost is less than or equal to zero
        if float(total_cost) <= 0:
            print("Total cost must be greater than zero. Please try again.")
            # Clear the entry
            self.total_cost_entry.delete(0, tkinter.END)
        date = self.date_combobox.get()

        # Get the selected vehicle nickname
        vehicle_nickname = self.vehicle_combo.get()

        fill_up = {
            "Date": date,
            "Odometer": odometer,
            "Gallons": total_gallons,
            "Gas Price": fuel_price,
            "Total Cost": total_cost,
            "Vehicle Nickname": vehicle_nickname
        }

        fill_ups = pd.read_csv("fill_ups.csv")
        fill_ups = pd.concat([fill_ups, pd.DataFrame([fill_up])], ignore_index=True)
        fill_ups.to_csv("fill_ups.csv", index=False)

        # Clear the entries
        self.odometer_entry.delete(0, tkinter.END)
        self.fuel_price_entry.delete(0, tkinter.END)
        self.Entry3.delete(0, tkinter.END)
        self.total_cost_entry.delete(0, tkinter.END)

    def show_total_fill_ups(self):
        fill_ups = pd.read_csv("fill_ups.csv")
        print(fill_ups)





if __name__ == "__main__":
    app = App()
    app.show_total_fill_ups()
    app.mainloop()