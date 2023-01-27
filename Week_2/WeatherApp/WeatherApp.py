''' The goal of this project is to create a weather app that shows the current weather conditions and forecast for a specific location.

Here are the steps you can take to create this project:

    Use the requests library to make an API call to a weather service (e.g. OpenWeatherMap) to retrieve the weather data for a specific location.

    Use the json library to parse the JSON data returned by the API call.

    Use the tkinter library to create a GUI for the app, including widgets such as labels, buttons and text boxes.

    Use the Pillow library to display the weather icons.

    Use the datetime library to display the current time and date. '''

from tkinter import *
from tkinter import ttk
import requests
import json

country_lat = {"lat":0,"lon":0}
api_key = "enter your API key"

city_name = print_cont()

r = requests.get("http://api.openweathermap.org/geo/1.0/direct?q={city}&appid={key}".format(city=str(city_name),key=str(api_key)))
r_json = json.load(r)

forcast_data = requests.get("http://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&units=metric".format(lat=r_json["lat"],lon=r_json["lon"]))
forcast_data_json = json.load(forcast_data)

daily_forcast = forcast_data_json["daily"]

daily_temp = []
for elem in daily_forcast:
    day_info = [elem["weather"]["main"],elem["weather"]["icon"]]
    daily_temp.append(day_info)

'''

root = Tk()
root.title("Weather App")
root.geometry("1000x562")

def print_cont():
    output = text.get()
    return output

frm = ttk.Frame(root, padding=10)
frm.grid()

ttk.Label(frm, text="Enter city name:").grid(column=0, row=0)
text = StringVar()
ttk.Entry(frm, textvariable=text).grid(column=1, row=0)
ttk.Button(frm, text="Quit", command=print_cont).grid(column=2, row=0)



root.mainloop()

'''