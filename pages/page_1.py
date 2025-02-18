import tkinter
import customtkinter
from PIL import Image
from picker import CTkDatePicker

class Page_1(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master

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
        self.total_cost_entry.place(x=318, y=520)

        self.submit_button = customtkinter.CTkButton(self, bg_color=['gray86', 'gray17'], font=customtkinter.CTkFont('Roboto', size=26, weight='bold'), height=50, text="Submit", fg_color="#00b900", text_color="#000000")
        self.submit_button.place(x=655, y=544)

        self.date_picker_label = customtkinter.CTkButton(self, bg_color=['gray86', 'gray17'], text="Select a Date", hover=False, width=160, font=customtkinter.CTkFont('Roboto', size=13, weight='bold'))
        self.date_picker_label.place(x=550, y=380)

        self.date_combobox = customtkinter.CTkComboBox(self)
        self.date_combobox.place(x=550, y=420)

        CTkDatePicker(self.date_combobox)


        self.top_frame = customtkinter.CTkFrame(self, width=800, height=100)
        self.top_frame.place(x=4, y=0)