import tkinter
import customtkinter
from PIL import Image

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")


class App(customtkinter.CTk):

    HEIGHT = 700
    WIDTH = 1000

    def __init__(self):
        super().__init__()
        self.title("MPG Tracker v0.2")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.resizable(False, False)

        self.Frame1 = customtkinter.CTkFrame(
            self,
            fg_color=[
                'gray86',
                'gray17'],
            width=350,
            height=700,
            corner_radius=0)
        self.Frame1.place(x=0, y=0)

        self.vehicle_selection = customtkinter.CTkComboBox(
            self, values=[], border_width=3, bg_color=['gray86', 'gray17'])
        self.vehicle_selection.place(x=5, y=5)

        self.odo_reading_label = customtkinter.CTkLabel(
            self,
            bg_color=[
                'gray86',
                'gray17'],
            font=customtkinter.CTkFont(
                'Roboto',
                size=13,
                weight='bold'),
            text="Current Odometer Reading")
        self.odo_reading_label.place(x=100, y=115)

        self.odometer_entry = customtkinter.CTkEntry(self, bg_color=['gray86', 'gray17'], width=150)
        self.odometer_entry.place(x=100, y=150)

        self.gas_price_label = customtkinter.CTkLabel(
            self,
            bg_color=[
                'gray86',
                'gray17'],
            font=customtkinter.CTkFont(
                'Roboto',
                size=13,
                weight='bold'),
            text="Gas Price (Gallon)")
        self.gas_price_label.place(x=100, y=200)

        self.Entry2 = customtkinter.CTkEntry(self, bg_color=['gray86', 'gray17'], width=150)
        self.Entry2.place(x=100, y=235)

        self.total_gallon_label = customtkinter.CTkLabel(
            self,
            bg_color=[
                'gray86',
                'gray17'],
            font=customtkinter.CTkFont(
                'Roboto',
                size=13,
                weight='bold'),
            text="Total Gallons")
        self.total_gallon_label.place(x=100, y=285)

        self.total_gallon_entry = customtkinter.CTkEntry(self, bg_color=['gray86', 'gray17'], width=150)
        self.total_gallon_entry.place(x=100, y=314)

        self.submit_button = customtkinter.CTkButton(
            self,
            bg_color=[
                'gray86',
                'gray17'],
            font=customtkinter.CTkFont(
                'Roboto',
                size=19,
                weight='bold'),
            width=160,
            text="Submit",
            fg_color="#008000")
        self.submit_button.place(x=101, y=400)

        self.info_box = customtkinter.CTkTextbox(self, bg_color=['gray86', 'gray17'], width=300, border_width=3)
        self.info_box.place(x=25, y=445)
        self.info_box.insert(1.0, '')

        self.add_vehicle_button = customtkinter.CTkButton(
            self,
            bg_color=[
                'gray86',
                'gray17'],
            font=customtkinter.CTkFont(
                'Roboto',
                size=13,
                weight='bold'),
            text="Add Vehicle")
        self.add_vehicle_button.place(x=205, y=5)

        self.info_frame = customtkinter.CTkFrame(self, width=662, height=280, corner_radius=0)
        self.info_frame.place(x=348, y=420)

        self.last_readings_label = customtkinter.CTkLabel(self, bg_color=['gray86', 'gray17'], font=customtkinter.CTkFont(
            'Roboto', size=17, weight='bold', underline=1), text="Last  Readings For Selected Vehicle")
        self.last_readings_label.place(x=535, y=470)

        self.odometer_button = customtkinter.CTkButton(self, bg_color=['gray86', 'gray17'], text="", hover=False)
        self.odometer_button.place(x=400, y=515)

        self.gas_price_button = customtkinter.CTkButton(self, bg_color=['gray86', 'gray17'], text="", hover=False)
        self.gas_price_button.place(x=600, y=515)

        self.total_gallons_button = customtkinter.CTkButton(self, bg_color=['gray86', 'gray17'], text="", hover=False)
        self.total_gallons_button.place(x=800, y=515)

        self.last_odo_label = customtkinter.CTkLabel(self, bg_color=['gray86', 'gray17'], text="Odometer")
        self.last_odo_label.place(x=441, y=555)

        self.last_gas_price_label = customtkinter.CTkLabel(self, bg_color=['gray86', 'gray17'], text="Gas Price")
        self.last_gas_price_label.place(x=639, y=555)

        self.gallons_label = customtkinter.CTkLabel(self, bg_color=['gray86', 'gray17'], text="Gallons")
        self.gallons_label.place(x=847, y=555)


if __name__ == "__main__":
    app = App()
    app.mainloop()
