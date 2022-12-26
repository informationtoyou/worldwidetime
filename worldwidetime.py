import tkinter as tk
import pytz
from datetime import datetime

def show_time():
    # Get the city name from the input field
    city = city_entry.get()

    # Use pytz to get the timezone for the given city
    tz = pytz.timezone(city)

    # Get the current time in the specified timezone
    time = datetime.now(tz)

    # Format the time as a string
    time_string = time.strftime("%I:%M %p %Z")

    # Update the label with the current time
    time_label.config(text=time_string)

# Create the main window

root = tk.Tk()
root.title("City Time")

# Create a label for the city input field
city_label = tk.Label(root, text="Enter a city name:")
city_label.pack()

# Create a city input field

city_entry = tk.Entry(root)
city_entry.pack()

# Create a button to show the time

time_button = tk.Button(root, text="Show Time", command=show_time)
time_button.pack()

# Create a label to display the time

time_label = tk.Label(root, text="")
time_label.pack()

# Run the tkinter event loop

root.mainloop()