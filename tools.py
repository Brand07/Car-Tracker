import customtkinter


class MoreTools(customtkinter.CTkToplevel):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.title("More Tools")
        self.geometry("500x300")
        self.resizable(False, False)
        self.grab_set()

        # Add a label to the window
        label = customtkinter.CTkLabel(self, text="More Tools")
        label.pack(pady=20)
