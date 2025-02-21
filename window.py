import customtkinter

import functions
from picker import CTkDatePicker
from add_vehicle import VehicleAdder
from tools import MoreTools

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


class Window(customtkinter.CTk):
    HEIGHT = 600
    WIDTH = 800

    def __init__(self, *args, **kwargs):
        super().__init__()
        self.title("Vehicle Fuel Efficiency Tracker")
        self.geometry(f"{self.WIDTH}x{self.HEIGHT}")
        self.resizable(False, False)

        self.top_frame = customtkinter.CTkFrame(self, width=800, height=100)
        self.top_frame.place(x=0, y=0)

        self.Frame1 = customtkinter.CTkFrame(self, width=800, height=240)
        self.Frame1.place(x=0, y=360)

        self.odometer_button = customtkinter.CTkButton(
            self,
            bg_color=["gray86", "gray17"],
            fg_color="blue",
            width=160,
            text="Current Odometer",
            hover=False,
            font=customtkinter.CTkFont("Roboto", size=13, weight="bold"),
        )
        self.odometer_button.place(x=80, y=380)

        self.odometer_entry = customtkinter.CTkEntry(
            self, bg_color=["gray86", "gray17"], width=160
        )
        self.odometer_entry.place(x=80, y=420)

        self.fuel_price_button = customtkinter.CTkButton(
            self,
            bg_color=["gray86", "gray17"],
            fg_color="blue",
            text="Fuel Price",
            hover=False,
            width=160,
            font=customtkinter.CTkFont("Roboto", size=13, weight="bold"),
        )
        self.fuel_price_button.place(x=80, y=480)

        self.fuel_price_entry = customtkinter.CTkEntry(
            self, bg_color=["gray86", "gray17"], width=160
        )
        self.fuel_price_entry.place(x=80, y=520)

        self.total_gallons_button = customtkinter.CTkButton(
            self,
            bg_color=["gray86", "gray17"],
            fg_color="blue",
            text="Total Gallons Purchased",
            hover=False,
            width=160,
            font=customtkinter.CTkFont("Roboto", size=13, weight="bold"),
        )
        self.total_gallons_button.place(x=320, y=380)

        self.Entry3 = customtkinter.CTkEntry(
            self, bg_color=["gray86", "gray17"], width=160
        )
        self.Entry3.place(x=320, y=420)

        self.total_cost_button = customtkinter.CTkButton(
            self,
            bg_color=["gray86", "gray17"],
            fg_color="blue",
            text="Total Cost",
            hover=False,
            width=160,
            font=customtkinter.CTkFont("Roboto", size=13, weight="bold"),
        )
        self.total_cost_button.place(x=320, y=480)

        self.total_cost_entry = customtkinter.CTkEntry(
            self, bg_color=["gray86", "gray17"], width=160
        )
        self.total_cost_entry.place(x=320, y=520)

        self.more_button = customtkinter.CTkButton(
            self,
            bg_color=["gray86", "gray17"],
            font=customtkinter.CTkFont("Roboto", size=26, weight="bold"),
            height=50,
            text="More",
            fg_color="#00b900",
            text_color="#000000",
            command=lambda: functions.open_more_tools(self),
        )
        self.more_button.place(x=500, y=545)

        self.submit_button = customtkinter.CTkButton(
            self,
            bg_color=["gray86", "gray17"],
            font=customtkinter.CTkFont("Roboto", size=26, weight="bold"),
            height=50,
            text="Submit",
            fg_color="#00b900",
            text_color="#000000",
            command=lambda: functions.handle_submit_button(self),
        )
        self.submit_button.place(x=655, y=545)

        self.date_picker_label = customtkinter.CTkButton(
            self,
            bg_color=["gray86", "gray17"],
            fg_color="blue",
            text="Select a Date",
            hover=False,
            width=160,
            font=customtkinter.CTkFont("Roboto", size=13, weight="bold"),
        )
        self.date_picker_label.place(x=550, y=380)

        self.date_combobox = customtkinter.CTkComboBox(self)
        self.date_combobox.place(x=550, y=420)

        CTkDatePicker(self.date_combobox)

        self.vehicle_combo = customtkinter.CTkComboBox(
            self, values=[""], bg_color=["gray86", "gray17"], justify="center"
        )
        self.vehicle_combo.place(x=10, y=35)

        self.select_vehicle_label = customtkinter.CTkLabel(
            self, text="Select a vehicle"
        )
        self.select_vehicle_label.place(x=30, y=2)

        self.add_vehicle_button = customtkinter.CTkButton(
            self,
            bg_color=["gray86", "gray17"],
            text="Add Vehicle",
            command=self.open_vehicle_adder,
        )
        self.add_vehicle_button.place(x=650, y=10)

        self.info_box = customtkinter.CTkTextbox(
            self,
            bg_color=["gray92", "gray14"],
            width=792,
            height=250,
            corner_radius=5,
            border_width=3,
        )
        self.info_box.place(x=4, y=105)
        self.info_box.insert(1.0, "")

        self.load_vehicles()
        self.disable_info_box()


    def load_vehicles(self):
        functions.load_vehicles(self)

    # Auto-select the first vehicle in the list
    def load_first_vehicle(self):
        functions.load_first_vehicle(self)

    def open_vehicle_adder(self):
        VehicleAdder(self)

    def open_more_tools(self):
        MoreTools(self)

    def disable_info_box(self):
        functions.disable_info_box(self)
