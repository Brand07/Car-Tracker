import os
import pandas as pd
from gui import App

#Create a Resources folder if it doesn't exist
if not os.path.isdir("Resources"):
    os.mkdir("Resources")

if __name__ == '__main__':
    app = App()
    app.mainloop()