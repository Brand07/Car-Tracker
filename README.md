# MPG Tracker (Work In Progress)

Car Tracker is a Python application that allows users to track their vehicle's fuel fill-ups, odometer readings, and fuel costs. The application uses a graphical user interface (GUI) built with `tkinter` and `customtkinter`, and stores data in Excel files using the `pandas` library.

## Features

- Add new fill-up records for different vehicles.
- Validate odometer readings to ensure they are greater than the previous readings.
- Store fill-up data in Excel files.
- Display total fill-ups.

## Requirements

- Python 3.13 or higher
- `pandas`
- `openpyxl`
- `tkinter`
- `customtkinter`

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Brand07/Car-Tracker.git
    cd Car-Tracker
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv .venv
    .venv\Scripts\activate  # On Windows
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Ensure you have a `Resources` folder in the project directory. If not, it will be created automatically when you run the application.

2. Run the application:
    ```sh
    python main.py
    ```

3. Use the GUI to add new fill-up records. The application will validate the odometer readings and store the data in Excel files located in the `Resources` folder.

## Project Structure

- `main.py`: Entry point of the application.
- `gui.py`: Contains the GUI logic and event handlers.
- `Resources/`: Directory where Excel files for each vehicle are stored.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.