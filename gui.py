import tkinter
import customtkinter
from picker import CTkDatePicker
from add_vehicle import VehicleAdder
import pandas as pd
import os
import json

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


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

        self.select_vehicle_label = customtkinter.CTkLabel(self, text="Select a vehicle")
        self.select_vehicle_label.place(x=30, y=2)

        self.add_vehicle_button = customtkinter.CTkButton(self, bg_color=['gray86', 'gray17'], text="Add Vehicle", command=self.open_vehicle_adder)
        self.add_vehicle_button.place(x=650, y=10)

        self.info_box = customtkinter.CTkTextbox(self,bg_color=['gray92','gray14'],
            width=460,
            height=250,
            corner_radius=5,
            border_width=3)
        self.info_box.place(x=4, y=105)
        self.info_box.insert(1.0, '')

        self.load_vehicles()

    def insert_into_info_box(self, text):
        self.info_box.configure(state='normal')
        self.info_box.insert(1.0, text)
        self.info_box.configure(state='disabled')


    def open_vehicle_adder(self):
        vehicle_adder = VehicleAdder(self)
        vehicle_adder.mainloop()

    def load_vehicles(self):
        if os.path.isfile('Resources/vehicles.json'):
            try:
                vehicles = pd.read_json('Resources/vehicles.json')
                vehicle_names = [str(name) for name in vehicles['Nickname'].tolist()]
                self.vehicle_combo.configure(values=vehicle_names)
            except ValueError:
                print("Error: vehicles.json is empty or contains invalid JSON.")
                self.vehicle_combo.configure(values=[])

    def get_odo_reading(self):
        # Get the user input on the odometer reading
        current_odometer_reading = self.odometer_entry.get()
        # Get the last odometer reading from the Excel file based on the selected vehicle
        vehicle_nickname = self.vehicle_combo.get()
        print(f"Currently selected vehicle: {vehicle_nickname}")
        file_name = f"Resources/{vehicle_nickname}_fill-ups.xlsx"
        print(f"Excel file path: {file_name}")

        if os.path.isfile(file_name) and os.path.getsize(file_name) > 0:
            fill_ups = pd.read_excel(file_name)
            print(f"Excel file loaded. Number of records: {len(fill_ups)}")
            print(f"Excel columns: {fill_ups.columns.tolist()}")
            if not fill_ups.empty:
                vehicle_fill_ups = fill_ups[fill_ups["Vehicle Nickname"] == vehicle_nickname]
                print(f"Filtered records for vehicle '{vehicle_nickname}': {len(vehicle_fill_ups)}")
                print(vehicle_fill_ups)
                if not vehicle_fill_ups.empty:
                    last_odometer = vehicle_fill_ups["Odometer"].astype(int).max()
                    print(f"Last odometer reading: {last_odometer}")
                    if int(current_odometer_reading) <= last_odometer:
                        print("New odometer reading must be greater than the previous reading. Please try again.")
                        return False
                    else:
                        print("New odometer reading is valid.")
                        self.odometer_entry.delete(0, tkinter.END)
                        return True
                else:
                    print("No records found for the selected vehicle.")
            else:
                print("Excel file is empty.")
        else:
            print("Excel file does not exist or is empty.")
        return True

    def handle_submit_button(self):
        """Handles the submit button click"""

        odometer = self.odometer_entry.get()
        vehicle_nickname = self.vehicle_combo.get()
        self.insert_into_info_box(f"Currently selected vehicle: {vehicle_nickname}\n")

        # Check if the entry is a number
        try:
            odometer = int(odometer.strip())  # Strip spaces and convert to integer
        except ValueError:
            print("Odometer reading must be a number. Please try again.")
            self.odometer_button.configure(fg_color="red")
            # Clear the entry
            self.odometer_entry.delete(0, tkinter.END)
            return

        # Define the file name based on the vehicle nickname
        file_name = f"Resources/{vehicle_nickname}_fill-ups.xlsx"
        print(f"File name: {file_name}")

        # Check if the Excel file exists and is not empty
        if os.path.isfile(file_name) and os.path.getsize(file_name) > 0:
            print("File exists and is not empty.")
            fill_ups = pd.read_excel(file_name, engine='openpyxl')
            print(f"Loaded fill-ups: {fill_ups}")
            if not fill_ups.empty:
                fill_ups["Vehicle Nickname"] = fill_ups["Vehicle Nickname"].astype(str)
                vehicle_fill_ups = fill_ups[fill_ups["Vehicle Nickname"] == vehicle_nickname]
                print(f"Filtered fill-ups: {vehicle_fill_ups}")
                if not vehicle_fill_ups.empty:
                    last_odometer = vehicle_fill_ups["Odometer"].astype(int).max()
                    print(f"Last odometer reading: {last_odometer}")
                    if int(odometer) <= last_odometer:
                        print("New odometer reading must be greater than the previous reading. Please try again.")
                        self.odometer_button.configure(fg_color="red")
                        self.insert_into_info_box(f"New odometer reading must be greater than the previous reading. Please try again.\n")
                        self.odometer_entry.delete(0, tkinter.END)
                        return
                    else:
                        self.odometer_button.configure(fg_color="blue")
        else:
            print("File does not exist or is empty.")
            fill_ups = pd.DataFrame(
                columns=["Vehicle Nickname", "Date", "Odometer", "Gallons", "Gas Price", "Total Cost"])

        fuel_price = self.fuel_price_entry.get()
        # Check if the entry is a number or float
        try:
            fuel_price = float(fuel_price)
        except ValueError:
            print("Fuel price must be a number. Please try again.")
            self.fuel_price_button.configure(fg_color="red")
            self.fuel_price_entry.delete(0, tkinter.END)
            return
        if fuel_price <= 0:
            self.fuel_price_button.configure(fg_color="red")
            print("Fuel price must be greater than zero. Please try again.")
            self.fuel_price_entry.delete(0, tkinter.END)
            return
        else:
            self.fuel_price_button.configure(fg_color="blue")

        total_gallons = self.Entry3.get()
        try:
            total_gallons = float(total_gallons)
        except ValueError:
            print("Total gallons must be a number. Please try again.")
            self.Entry3.delete(0, tkinter.END)
            return
        if total_gallons <= 0:
            print("Total gallons must be greater than zero. Please try again.")
            self.Entry3.delete(0, tkinter.END)
            return

        total_cost = self.total_cost_entry.get()
        try:
            total_cost = float(total_cost)
        except ValueError:
            print("Total cost must be a number. Please try again.")
            self.total_cost_entry.delete(0, tkinter.END)
            return
        if total_cost <= 0:
            print("Total cost must be greater than zero. Please try again.")
            self.total_cost_entry.delete(0, tkinter.END)
            return

        date = self.date_combobox.get()

        fill_up = {
            "Vehicle Nickname": vehicle_nickname,
            "Date": date,
            "Odometer": odometer,
            "Gallons": total_gallons,
            "Gas Price": fuel_price,
            "Total Cost": total_cost,
        }

        fill_ups = pd.concat([fill_ups, pd.DataFrame([fill_up])], ignore_index=True)
        fill_ups.to_excel(file_name, index=False, engine='openpyxl')

        self.odometer_entry.delete(0, tkinter.END)
        self.fuel_price_entry.delete(0, tkinter.END)
        self.Entry3.delete(0, tkinter.END)
        self.total_cost_entry.delete(0, tkinter.END)
        self.show_total_cost_for_vehicle()



    def show_total_cost_for_vehicle(self):
        vehicle_nickname = self.vehicle_combo.get()
        file_name = f"Resources/{vehicle_nickname}_fill-ups.xlsx"
        if os.path.isfile(file_name):
            fill_ups = pd.read_excel(file_name)
            total_cost = fill_ups["Total Cost"].sum()
            self.insert_into_info_box(f"Total cost for {vehicle_nickname}: ${total_cost:.2f}\n")
        else:
            self.insert_into_info_box(f"No data available for {vehicle_nickname}.\n")





if __name__ == "__main__":
    app = App()
    app.mainloop()