import tkinter
import customtkinter
from picker import CTkDatePicker
import pandas as pd
import os

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")

class App(customtkinter.CTk):

    HEIGHT = 600
    WIDTH = 800

    def __init__(self):
        super().__init__()
        self.title("Vehicle Fuel Efficiency Tracker")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.resizable(False, False)

        self.Frame1 = customtkinter.CTkFrame(self, width=800, height=240)
        self.Frame1.place(x=0, y=360)

        self.odometer_button = customtkinter.CTkButton(self, bg_color=['gray86', 'gray17'], text="Current Odometer Reading", hover=False, font=customtkinter.CTkFont('Roboto', size=13, weight='bold'))
        self.odometer_button.place(x=80, y=380)

        self.odometer_entry = customtkinter.CTkEntry(self, bg_color=['gray86', 'gray17'], width=160)
        self.odometer_entry.place(x=80, y=420)

        self.fuel_price_button = customtkinter.CTkButton(self, bg_color=['gray86', 'gray17'], text="Fuel Price", hover=False, width=160, font=customtkinter.CTkFont('Roboto', size=13, weight='bold'))
        self.fuel_price_button.place(x=80, y=480)

        self.fuel_price_entry = customtkinter.CTkEntry(self, bg_color=['gray86', 'gray17'], width=160)
        self.fuel_price_entry.place(x=80, y=520)

        self.total_gallons_button = customtkinter.CTkButton(self, bg_color=['gray86', 'gray17'], text="Total Gallons Purchased", hover=False, width=160, font=customtkinter.CTkFont('Roboto', size=13, weight='bold'))
        self.total_gallons_button.place(x=320, y=380)

        self.Entry3 = customtkinter.CTkEntry(self, bg_color=['gray86', 'gray17'], width=160)
        self.Entry3.place(x=320, y=420)

        self.total_cost_button = customtkinter.CTkButton(self, bg_color=['gray86', 'gray17'], text="Total Cost", hover=False, width=160, font=customtkinter.CTkFont('Roboto', size=13, weight='bold'))
        self.total_cost_button.place(x=320, y=480)

        self.total_cost_entry = customtkinter.CTkEntry(self, bg_color=['gray86', 'gray17'], width=160)
        self.total_cost_entry.place(x=320, y=520)

        self.submit_button = customtkinter.CTkButton(self, bg_color=['gray86', 'gray17'], font=customtkinter.CTkFont('Roboto', size=26, weight='bold'), height=50, text="Submit", fg_color="#00b900", text_color="#000000", command=self.handle_submit_button)
        self.submit_button.place(x=655, y=545)

        self.date_picker_label = customtkinter.CTkButton(self, bg_color=['gray86', 'gray17'], text="Select a Date", hover=False, width=160, font=customtkinter.CTkFont('Roboto', size=13, weight='bold'))
        self.date_picker_label.place(x=550, y=380)

        self.date_combobox = customtkinter.CTkComboBox(self)
        self.date_combobox.place(x=550, y=420)

        CTkDatePicker(self.date_combobox)

        self.top_frame = customtkinter.CTkFrame(self, width=800, height=100)
        self.top_frame.place(x=0, y=0)

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
            #Clear the entry
            self.odometer_entry.delete(0, tkinter.END)
            return

        # Check if the odometer reading is less than what it was before
        fill_ups = pd.read_csv("fill_ups.csv")
        if len(fill_ups) > 0:
            if int(odometer) < fill_ups["Odometer"].iloc[-1]:
                print("Odometer reading must be greater than the previous reading. Please try again.")
                #Clear the entry
                self.odometer_entry.delete(0, tkinter.END)
                return

        fuel_price = self.fuel_price_entry.get()
        # Check if the entry is a number or float
        try:
            fuel_price = float(fuel_price)
        except ValueError:
            print("Fuel price must be a number. Please try again.")
            #Clear the entry
            self.fuel_price_entry.delete(0, tkinter.END)
            return
        # Check if the fuel price is less than or equal to zero
        if float(fuel_price) <= 0:
            print("Fuel price must be greater than zero. Please try again.")
            #Clear the entry
            self.fuel_price_entry.delete(0, tkinter.END)
            return

        total_gallons = self.Entry3.get()
        # Check if the entry is a number or float
        try:
            total_gallons = float(total_gallons)
        except ValueError:
            print("Total gallons must be a number. Please try again.")
            #Clear the entry
            self.Entry3.delete(0, tkinter.END)
        # Check if the total gallons is less than or equal to zero
        if float(total_gallons) <= 0:
            print("Total gallons must be greater than zero. Please try again.")
            #Clear the entry
            self.Entry3.delete(0, tkinter.END)
            return

        total_cost = self.total_cost_entry.get()
        # Check if the entry is a number or float
        try:
            total_cost = float(total_cost)
        except ValueError:
            print("Total cost must be a number. Please try again.")
            #Clear the entry
            self.total_cost_entry.delete(0, tkinter.END)
            return
        # Check if the total cost is less than or equal to zero
        if float(total_cost) <= 0:
            print("Total cost must be greater than zero. Please try again.")
            #Clear the entry
            self.total_cost_entry.delete(0, tkinter.END)
        date = self.date_combobox.get()

        # Check if the odometer reading is a number
        try:
            odometer = int(odometer)
        except ValueError:
            print("Odometer reading must be a number. Please try again.")
            #Clear the entry
            self.odometer_entry.delete(0, tkinter.END)
            return

        # Check if the fuel price is a number
        try:
            fuel_price = float(fuel_price)
        except ValueError:
            print("Fuel price must be a number. Please try again.")
            #Clear the entry
            self.fuel_price_entry.delete(0, tkinter.END)
            return

        # Check if the total gallons is a number
        try:
            total_gallons = float(total_gallons)
        except ValueError:
            print("Total gallons must be a number. Please try again.")
            #Clear the entry
            self.Entry3.delete(0, tkinter.END)
            return

        # Check if the total cost is a number
        try:
            total_cost = float(total_cost)
        except ValueError:
            print("Total cost must be a number. Please try again.")
            #Clear the entry
            self.total_cost_entry.delete(0, tkinter.END)
            return

        fill_up = {
            "Date": date,
            "Odometer": odometer,
            "Gallons": total_gallons,
            "Gas Price": fuel_price,
            "Total Cost": total_cost
        }

        fill_ups = pd.read_csv("fill_ups.csv")
        fill_ups = pd.concat([fill_ups, pd.DataFrame([fill_up])], ignore_index=True)
        fill_ups.to_csv("fill_ups.csv", index=False)

        # Clear the entries
        self.odometer_entry.delete(0, tkinter.END)
        self.fuel_price_entry.delete(0, tkinter.END)
        self.Entry3.delete(0, tkinter.END)
        self.total_cost_entry.delete(0, tkinter.END)


if __name__ == "__main__":
    app = App()
    app.mainloop()