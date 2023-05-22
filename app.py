import requests
from tkinter import *
import tkinter.messagebox

root = Tk()
root.geometry("1250x650")
root.title("Weather App")
root.configure(bg='light sky blue')

lable_0 = Label(root, text="  WEATHER NOW  ", anchor='e', font=("comic sans", 48, "bold",), bg='lawn green', fg='black',
                bd=7, relief='raised')
lable_0.place(x=400, y=30)

city_names = StringVar()
entry_1 = Entry(root, font=("arial", 23), bg='pale green', textvariable=city_names, width=24)
entry_1.place(x=700, y=160)

lable_7 = Label(root, text="Enter the city name ", width=20, font=("comic sans", 23, "bold"), bg='green2', fg='grey2',
                borderwidth=3, relief="raised")
lable_7.place(x=200, y=160)

lable_temp = Label(root, text="Temperature : ", width=20, font=("comic sans", 17), fg='light yellow', bg='dark green',
                borderwidth=3, relief="raised")
lable_temp.place(x=110, y=310)

lable_wind_speed = Label(root, text="Wind Speed : ", width=20, font=("comic sans", 17), fg='light yellow', bg='dark green',
                borderwidth=3, relief="raised")
lable_wind_speed.place(x=110, y=380)

lable_wind_dir = Label(root, text="Wind Direction : ", width=20, font=("comic sans", 17), fg='light yellow', bg='dark green',
                borderwidth=3, relief="raised")
lable_wind_dir.place(x=110, y=450)

lable_uv_index = Label(root, text="UV Index : ", width=20, font=("comic sans", 17), fg='light yellow', bg='dark green',
                borderwidth=3, relief="raised")
lable_uv_index.place(x=750, y=310)

lable_time = Label(root, text="Time : ", width=20, font=("comic sans", 17), fg='light yellow', bg='dark green',
                borderwidth=3, relief="raised")
lable_time.place(x=750, y=380)

lable_location = Label(root, text="Location : ", width=20, font=("comic sans", 17), fg='light yellow', bg='dark green',
                borderwidth=3, relief="raised")
lable_location.place(x=750, y=450)

lable_desc = Label(root, text=" Description :", width=20, font=("comic sans", 17), fg='light yellow', bg='dark green',
                borderwidth=3, relief="raised")
lable_desc.place(x=320, y=540)

lable_temp_val = Label(root, text="...", width=7, bg='white', font=("bold", 25), fg='black')
lable_temp_val.place(x=460, y=310)

lable_wind_speed_val = Label(root, text="...", width=7, bg='white', font=("bold", 25), fg='black')
lable_wind_speed_val.place(x=460, y=380)

lable_wind_dir_val = Label(root, text="...", width=7, bg='white', font=("bold", 25), fg='black')
lable_wind_dir_val.place(x=460, y=450)

lable_uv_index_val = Label(root, text="...", width=7, bg='white', font=("bold", 25), fg='black')
lable_uv_index_val.place(x=1030, y=310)

lable_time_val = Label(root, text="...", width=15, bg='white', font=("bold", 17), fg='black')
lable_time_val.place(x=1030, y=380)

lable_location_val = Label(root, text="...", width=15, bg='white', font=("bold", 17), fg='black')
lable_location_val.place(x=1030, y=450)

lable_desc_val = Label(root, text="...", width=24, bg='white', font=("bold", 17), fg='black')
lable_desc_val.place(x=693, y=540)

def getWeather():
    access_key = 'Your Weatherstack API'  
    city_name = entry_1.get()

    response = requests.get(f'http://api.weatherstack.com/current?access_key={access_key}&query={city_name}')

    if response.status_code == 200:
        data = response.json()

        if 'current' in data:
            temperature = data['current']['temperature']
            wind_speed = data['current']['wind_speed']
            wind_dir = data['current']['wind_dir']
            uv_index = data['current']['uv_index']
            time = data['current']['observation_time']
            location = data['location']['name']
            description = data['current']['weather_descriptions'][0]

            lable_temp_val.configure(text=f"{temperature}°C")
            lable_wind_speed_val.configure(text=f"{wind_speed} km/h")
            lable_wind_dir_val.configure(text=wind_dir)
            lable_uv_index_val.configure(text=uv_index)
            lable_time_val.configure(text=time)
            lable_location_val.configure(text=location)
            lable_desc_val.configure(text=description)
        else:
            tkinter.messagebox.showinfo("Error", "Weather data not found")
    else:
        tkinter.messagebox.showinfo("Error", "Failed to fetch weather data")


Button(root, text="SUBMIT", width=15, font=("comic sans", 13), bg='maroon', fg='white', bd=9, command=getWeather).place(
    x=590, y=235)

mainloop()
