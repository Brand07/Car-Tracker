import os
from window import Window

# Create a Resources folder if it doesn't exist
if not os.path.isdir("Resources"):
    os.mkdir("Resources")


if __name__ == "__main__":
    app = Window()
    app.mainloop()
