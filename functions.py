import os
import pandas as pd
import tkinter
from tools import MoreTools

def insert_into_info_box(app, text):
    app.info_box.configure(state="normal")
    app.info_box.insert(1.0, text)
    app.info_box.configure(state="disabled")

def clear_info_box(app):
    app.info_box.configure(state="normal")
    app.info_box.delete(1.0, tkinter.END)
    app.info_box.configure(state="disabled")

def load_vehicles(app):
    if os.path.isfile("Resources/vehicles.json"):
        try:
            vehicles = pd.read_json("Resources/vehicles.json")
            vehicle_names = [str(name) for name in vehicles["Nickname"].tolist()]
            app.vehicle_combo.configure(values=vehicle_names)
        except ValueError:
            print("Error: vehicles.json is empty or contains invalid JSON.")
            app.vehicle_combo.configure(values=[])

def get_odo_reading(app):
    current_odometer_reading = app.odometer_entry.get()
    vehicle_nickname = app.vehicle_combo.get()
    file_name = f"Resources/{vehicle_nickname}_fill-ups.xlsx"
    if os.path.isfile(file_name) and os.path.getsize(file_name) > 0:
        fill_ups = pd.read_excel(file_name)
        if not fill_ups.empty:
            vehicle_fill_ups = fill_ups[fill_ups["Vehicle Nickname"] == vehicle_nickname]
            if not vehicle_fill_ups.empty:
                last_odometer = vehicle_fill_ups["Odometer"].astype(int).max()
                if int(current_odometer_reading) <= last_odometer:
                    print("New odometer reading must be greater than the previous reading. Please try again.")
                    return False
                else:
                    app.odometer_entry.delete(0, tkinter.END)
                    return True
    return True

def handle_submit_button(app):
    odometer = app.odometer_entry.get()
    vehicle_nickname = app.vehicle_combo.get()
    #insert_into_info_box(app, f"Currently selected vehicle: {vehicle_nickname}\n")
    try:
        odometer = int(odometer.strip())
    except ValueError:
        print("Odometer reading must be a number. Please try again.")
        app.odometer_button.configure(fg_color="red")
        app.odometer_entry.delete(0, tkinter.END)
        return
    file_name = f"Resources/{vehicle_nickname}_fill-ups.xlsx"
    if os.path.isfile(file_name) and os.path.getsize(file_name) > 0:
        fill_ups = pd.read_excel(file_name, engine="openpyxl")
        if not fill_ups.empty:
            fill_ups["Vehicle Nickname"] = fill_ups["Vehicle Nickname"].astype(str)
            vehicle_fill_ups = fill_ups[fill_ups["Vehicle Nickname"] == vehicle_nickname]
            if not vehicle_fill_ups.empty:
                last_odometer = vehicle_fill_ups["Odometer"].astype(int).max()
                if int(odometer) <= last_odometer:
                    print("New odometer reading must be greater than the previous reading. Please try again.")
                    app.odometer_button.configure(fg_color="red")
                    insert_into_info_box(app, "New odometer reading must be greater than the previous reading. Please try again.\n")
                    app.odometer_entry.delete(0, tkinter.END)
                    return
                else:
                    app.odometer_button.configure(fg_color="blue")
    else:
        fill_ups = pd.DataFrame(columns=["Vehicle Nickname", "Date", "Odometer", "Gallons", "Gas Price", "Total Cost"])
    fuel_price = app.fuel_price_entry.get()
    try:
        fuel_price = float(fuel_price)
    except ValueError:
        print("Fuel price must be a number. Please try again.")
        app.fuel_price_button.configure(fg_color="red")
        app.fuel_price_entry.delete(0, tkinter.END)
        return
    if fuel_price <= 0:
        app.fuel_price_button.configure(fg_color="red")
        print("Fuel price must be greater than zero. Please try again.")
        app.fuel_price_entry.delete(0, tkinter.END)
        return
    else:
        app.fuel_price_button.configure(fg_color="blue")
    total_gallons = app.Entry3.get()
    try:
        total_gallons = float(total_gallons)
    except ValueError:
        print("Total gallons must be a number. Please try again.")
        app.Entry3.delete(0, tkinter.END)
        return
    if total_gallons <= 0:
        print("Total gallons must be greater than zero. Please try again.")
        app.Entry3.delete(0, tkinter.END)
        return
    total_cost = app.total_cost_entry.get()
    try:
        total_cost = float(total_cost)
    except ValueError:
        print("Total cost must be a number. Please try again.")
        app.total_cost_entry.delete(0, tkinter.END)
        return
    if total_cost <= 0:
        print("Total cost must be greater than zero. Please try again.")
        app.total_cost_entry.delete(0, tkinter.END)
        return
    date = app.date_combobox.get()
    fill_up = {
        "Vehicle Nickname": vehicle_nickname,
        "Date": date,
        "Odometer": odometer,
        "Gallons": total_gallons,
        "Gas Price": fuel_price,
        "Total Cost": total_cost,
    }
    fill_ups = pd.concat([fill_ups, pd.DataFrame([fill_up])], ignore_index=True)
    fill_ups.to_excel(file_name, index=False, engine="openpyxl")
    app.odometer_entry.delete(0, tkinter.END)
    app.fuel_price_entry.delete(0, tkinter.END)
    app.Entry3.delete(0, tkinter.END)
    app.total_cost_entry.delete(0, tkinter.END)

def show_total_cost_for_vehicle(app):
    vehicle_nickname = app.vehicle_combo.get()
    file_name = f"Resources/{vehicle_nickname}_fill-ups.xlsx"
    if os.path.isfile(file_name):
        fill_ups = pd.read_excel(file_name)
        total_cost = fill_ups["Total Cost"].sum()
        insert_into_info_box(app, f"Statistics on  {vehicle_nickname}: \n${total_cost:.2f}\n{len(fill_ups)} fill-ups\n")
    else:
        insert_into_info_box(app, f"No data available for {vehicle_nickname}.\n")

def calculate_fuel_efficiency(app, vehicle_nickname):
    file_name = f"Resources/{vehicle_nickname}_fill-ups.xlsx"
    if os.path.isfile(file_name):
        fill_ups = pd.read_excel(file_name)
        if not fill_ups.empty:
            fill_ups["Odometer"] = fill_ups["Odometer"].astype(int)
            fill_ups["Gallons"] = fill_ups["Gallons"].astype(float)
            fill_ups.sort_values(by="Date", inplace=True)
            fill_ups["Fuel Efficiency"] = (fill_ups["Odometer"].diff() / fill_ups["Gallons"].diff()).fillna(0)
            insert_into_info_box(app, f"Fuel Efficiency for {vehicle_nickname}: \n{fill_ups['Fuel Efficiency'].mean():.2f} MPG\n")
        else:
            insert_into_info_box(app, f"No data available for {vehicle_nickname}.\n")
    else:
        insert_into_info_box(app, f"No data available for {vehicle_nickname}.\n")

def open_more_tools(app):
    MoreTools(app)

