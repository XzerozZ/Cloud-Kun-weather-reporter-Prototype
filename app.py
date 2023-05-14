import requests
from tkinter import *
import tkinter as tk
from datetime import datetime

api_key = 'Your_Weatherstack_API'

def get_weather():
    location = city_entry.get()
    api_url = f"http://api.weatherstack.com/current?access_key={api_key}&query={location}"
    response = requests.get(api_url)
    weather_data = response.json()

    if 'current' in weather_data:
        date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

        weather_desc = weather_data['current']['weather_descriptions'][0]
        temperature_c = weather_data['current']['temperature']
        humidity = weather_data['current']['humidity']
        wind_speed = weather_data['current']['wind_speed']
        wind_dir = weather_data['current']['wind_dir']
        pressure = weather_data['current']['pressure']
        uv_index = weather_data['current']['uv_index']
        country = weather_data['location']['country']

        location_label.config(text=f"{location.title()}, {country}")
        weather_label.config(text=f"Weather Description : {weather_desc}")
        temp_label.config(text=f"Temperature : {temperature_c} °C")
        humidity_label.config(text=f"Humidity : {humidity}%")
        wind_speed_label.config(text=f"Wind Speed : {wind_speed} km/h")
        wind_dir_label.config(text=f"Wind Direction : {wind_dir}")
        pressure_label.config(text=f"Pressure : {pressure} mb")
        uv_index_label.config(text=f"UV Index : {uv_index}")
        datetime_label.config(text=f"({date_time})")
        lasttext_label.config(text=f"Have a nice day")

    else:
        location_label.config(text="Sorry, weather information not available for this city.")

root = Tk()
root.title("Cloud-Kun weather reporter (Prototype)")


root.config(bg="white")
input_frame = Frame(root,bg="midnight blue")
input_frame.pack(pady=10)

city_entry = Entry(input_frame, font=("Helvetica", 14),bg='black',fg='white')
city_entry.pack(side=LEFT, padx=10)

get_weather_button = Button(input_frame, text="Get Weather", font=("Helvetica", 14), bg="orange red", activebackground="deep sky blue",activeforeground = "white",fg="black" ,command=get_weather)
get_weather_button.pack(side=LEFT)

weather_frame = Frame(root,bg="white")
weather_frame.pack(padx=10, pady=10)

location_label = Label(weather_frame, font=("Helvetica", 18),bg="white")
location_label.pack()

datetime_label = Label(weather_frame, font=("Helvetica", 12),bg="white")
datetime_label.pack()

weather_label = Label(weather_frame, font=("Helvetica", 14),bg="white")
weather_label.pack()

temp_label = Label(weather_frame, font=("Helvetica", 14),bg="white")
temp_label.pack()

humidity_label = Label(weather_frame, font=("Helvetica", 14),bg="white")
humidity_label.pack()

wind_speed_label = Label(weather_frame, font=("Helvetica", 14),bg="white")
wind_speed_label.pack()

wind_dir_label = Label(weather_frame, font=("Helvetica", 14),bg="white")
wind_dir_label.pack()

pressure_label = Label(weather_frame, font=("Helvetica", 14),bg="white")
pressure_label.pack()

uv_index_label = Label(weather_frame, font=("Helvetica", 14),bg="white")
uv_index_label.pack()

lasttext_label = Label(weather_frame, font=("Helvetica", 14),bg="white")
lasttext_label.pack()

root.mainloop()
