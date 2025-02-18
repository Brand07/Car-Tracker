# Author: Brand07
# Date: 2/18/2025
import json
from xml.etree.ElementTree import indent


class App:
    def __init__(self):
        self.tank_capacity = 0.00
        self.model = ""
        self.brand = ""
        self.year = ""
        self.tank_size = ""
        self.mpg = 0.00
        self.odometer = 0
        self.mileage = 0
        self.gas_price = 0.00
        self.total_cost = 0.00
        self.total_miles = 0.00
        self.total_gallons = 0.00


    def get_vehicle_info(self):
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




if __name__ == '__main__':
    app = App()
    app.edit_vehicle_info()



