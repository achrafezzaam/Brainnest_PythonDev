from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import urllib.request
import io
import requests
import json
import datetime

class WeatherApp:
    def __init__(self, api_key):
        self.api_key = api_key
        self.city = ""
        self.icons = []
        self.root = Tk()
        self.root.title("Weather App")
        self.frm1 = ttk.Frame(self.root)
        self.frm1.grid(padx=10,pady=20)
        self.frm2 = ttk.Frame(self.root)
        self.frm2.grid(pady=80)
        self.frm3 = ttk.Frame(self.root)
        self.frm3.grid(pady=5)
        self.BuildGUI()
    
    def getDatetime(self):
        today = datetime.datetime.now()
        return today.strftime("Day: %d %B %Y - Time: %H:%M")
    
    def Refresher(self,field):
        field.set(self.getDatetime())
        self.frm3.after(60000, self.Refresher, field)

    def ImgFromUrl(self,url):
        global image
        with urllib.request.urlopen(url) as connection:
            raw_data = connection.read()
        im = Image.open(io.BytesIO(raw_data))
        image = ImageTk.PhotoImage(im)
        return image

    def GetWeatherInfo(self): # this method gets the lat and lon for given city name then uses them to return the weather forcast
        r = requests.get("http://api.openweathermap.org/geo/1.0/direct?q={city}&appid={key}".format(city=self.city,key=str(self.api_key)))
        r_json = json.load(r)

        forcast_data = requests.get("http://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&units=metric".format(lat=r_json["lat"],lon=r_json["lon"]))
        forcast_data_json = json.load(forcast_data)

        daily_forcast = forcast_data_json["daily"] # Storing the daily forcast only

        daily_weath = []
        for elem in daily_forcast: # Creating a list of lists containing the weather state and icon for each day
            day_info = [elem["weather"]["main"],elem["weather"]["icon"]]
            daily_weath.append(day_info)
        return daily_weath

    def BuildForcast(self): # Building the display frame for the weather forcast state and icons in the root frame app
        forcast = self.GetWeatherInfo()
        count = 0
        for elem in forcast:
            url = "http://openweathermap.org/img/wn/{}.png".format(elem[1]) # Building the link for the icons
            self.icons.append(self.ImgFromUrl(url))
            today = datetime.datetime.now()
            day = today + datetime.timedelta(days=count)
            display = day.strftime("%d %b")
            weather = elem[0]
            ttk.Label(self.frm2, text=weather, width=14, anchor="center").grid(column=count, row=0)
            ttk.Label(self.frm2, image=self.icons[count], width=14).grid(column=count, row=1)
            ttk.Label(self.frm2, text=display, width=14, anchor="center").grid(column=count, row=2)
            count+=1

    def BuildGUI(self): # Building the root frame wich will containe the  other frames ( the form for city name entry and the forcast frame built with the BuildForcast method)
        def print_cont(text):
            output = text.get()
            self.city = str(output)
        ttk.Label(self.frm1, text="Enter city name:").grid(column=0, row=0)
        text = StringVar()
        ttk.Entry(self.frm1, textvariable=text).grid(column=1, row=0)
        ttk.Button(self.frm1, text="Quit", command=print_cont).grid(column=2, row=0)

        self.BuildForcast()

        frm3_label = StringVar() # Display of the current date and time
        ttk.Label(self.frm3, textvariable=frm3_label).grid(column=0, row=0)

        self.Refresher(frm3_label) # Making the date/time display frame refresh each 60s to keep track of time
        self.root.mainloop()

if __name__=="__main__":
    api_key = input("Enter your API Key")
    WeatherApp(str(api_key))