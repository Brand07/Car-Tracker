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


if __name__ == '__main__':
    app = App()
    app.get_vehicle_info()



