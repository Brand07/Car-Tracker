# Author: Brand07
# Date: 2/18/2025
import json
import os
from xml.etree.ElementTree import indent

import pandas as pd


# Check if the CSV file exists before initializing the DataFrame
if not os.path.isfile("fill_ups.csv"):
    fill_ups = pd.DataFrame(columns=["Date", "Odometer", "Gallons", "Gas Price", "Total Cost"])
    fill_ups.to_csv("fill_ups.csv", index=False)



class App:
    def __init__(self):
        self.tank_capacity = 0.00
        self.model = ""
        self.brand = ""
        self.year = ""
        self.tank_size = 0.00
        self.mpg = 0.00
        self.odometer = 0
        self.gas_price = 0.00
        self.total_cost = 0.00
        self.total_gallons = 0.00


    def insert_vehicle_info(self):
        self.model = input("Enter the model of the vehicle: ")
        self.brand = input("Enter the brand of the vehicle: ")
        self.year = input("Enter the year of the vehicle: ")
        self.tank_capacity = input("Enter the tank size of the vehicle: ")
        self.odometer = input("Enter the odometer reading of the vehicle: ")
        # Send the info the json file
        self.write_json()

    def write_json(self):
        vehicle_info = {
            "model": self.model,
            "brand": self.brand,
            "year": self.year,
            "tank_capacity": self.tank_capacity,
            "odometer": self.odometer,
        }

        with open('vehicle_info.json', 'w') as json_file:
            json.dump(vehicle_info, json_file, indent=4)

    def edit_vehicle_info(self):
        """Allows the user to edit the vehicle information"""
        try:
            with open('vehicle_info.json', 'r') as json_file:
                vehicle_info = json.load(json_file)
        except FileNotFoundError:
            print("No existing vehicle information found.")
            return

        print("What information do you need to update about your vehicle?")
        info_choice = input("1 - Model\n2 - Brand\n3 - Year\n4 - Tank Capacity\n5 - Odometer\n")
        if info_choice == "1":
            vehicle_info["model"] = input("Enter the model of the vehicle: ")
        elif info_choice == "2":
            vehicle_info["brand"] = input("Enter the brand of the vehicle: ")
        elif info_choice == "3":
            vehicle_info["year"] = input("Enter the year of the vehicle: ")
        elif info_choice == "4":
            vehicle_info["tank_capacity"] = input("Enter the tank size of the vehicle: ")
        elif info_choice == "5":
            vehicle_info["odometer"] = input("Enter the odometer reading of the vehicle: ")
        else:
            print("Invalid choice. Please try again.")
            self.edit_vehicle_info()
            return

        with open('vehicle_info.json', 'w') as json_file:
            json.dump(vehicle_info, json_file, indent=4)

    def add_fill_up(self):
        """Get the fill-up from the user and add it to the DataFrame"""
        print("Enter the following information for the fill-up:")
        date = input("Date (MM/DD/YYYY): ")
        # Check if the date is in the correct format
        if len(date) != 10 or date[2] != "/" or date[5] != "/":
            print("Invalid date format. Please try again.")
            self.add_fill_up()
            return

        odometer = input("Odometer reading: ")
        # Check if the odometer reading is a number
        try:
            odometer = int(odometer)
        except ValueError:
            print("Odometer reading must be a number. Please try again.")
            self.add_fill_up()
            return

        # Make sure the odometer reading is greater than the previous reading
        try:
            fill_ups = pd.read_csv('fill_ups.csv')
        except FileNotFoundError:
            fill_ups = pd.DataFrame(columns=["Date", "Odometer", "Gallons", "Gas Price", "Total Cost"])

        if not fill_ups.empty and odometer <= fill_ups["Odometer"].iloc[-1]:
            print("Odometer reading must be greater than the previous reading. Please try again.")
            self.add_fill_up()
            return

        gallons = input("Gallons purchased: ")
        # Check if the gallons purchased is a number
        try:
            gallons = float(gallons)
        except ValueError:
            print("Gallons purchased must be a number. Please try again.")
            self.add_fill_up()
            return

        gas_price = input("Price per gallon: ")
        # Check if the price per gallon is a number
        try:
            gas_price = float(gas_price)
        except ValueError:
            print("Price per gallon must be a number. Please try again.")
            self.add_fill_up()

        total_cost = input("Total cost: ")
        # Check if the total cost is a number
        try:
            total_cost = float(total_cost)
        except ValueError:
            print("Total cost must be a number. Please try again.")
            self.add_fill_up()
            return

        fill_up = {
            "Date": date,
            "Odometer": odometer,
            "Gallons": gallons,
            "Gas Price": gas_price,
            "Total Cost": total_cost
        }

        fill_ups = fill_ups._append(fill_up, ignore_index=True)
        fill_ups.to_csv('fill_ups.csv', index=False)



    def clear_fill_up_file(self):
        """Clears the csv file. Will prompt the user for confirmation"""
        confirm = input("Are you sure you want to clear the fill-up file? (Y/N): ")
        if confirm.lower() == "y":
            fill_ups = pd.DataFrame(columns=["Date", "Odometer", "Gallons", "Gas Price", "Total Cost"])
            fill_ups.to_csv("fill_ups.csv", index=False)
        else:
            print("File not cleared.")






if __name__ == '__main__':
    app = App()



