import os
import pandas as pd
from gui import App

# Check if the CSV file exists before initializing the DataFrame
if not os.path.isfile("fill_ups.csv"):
    fill_ups = pd.DataFrame(columns=["Nickname","Date", "Odometer", "Gallons", "Gas Price", "Total Cost"])
    fill_ups.to_csv("fill_ups.csv", index=False)

if __name__ == '__main__':
    app = App()
    app.mainloop()