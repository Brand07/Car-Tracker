import tkinter
import customtkinter
from PIL import Image
from pages.page_1 import Page_1

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


class App(customtkinter.CTk):

    HEIGHT = 600
    WIDTH = 800

    def __init__(self):
        super().__init__()
        self.title("Vehicle Fuel Efficiency Tacker")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.resizable(False, False)
        self.Page_1 = Page_1(self, fg_color='transparent', corner_radius=0, border_width=0)
        self.Page_1.pack(expand=True, fill='both')


if __name__ == "__main__":
    app = App()
    app.mainloop()
