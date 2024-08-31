import tkinter as tk
import requests
import requests
import settings
from tkinter import messagebox

# Weather API Settings
def get_weather(city):
    api_key = settings.API_KEY 
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    weather_data = response.json()

    if weather_data['cod'] == 200:
        city_label['text'] = weather_data['name']
        # country_label['text'] = weather_data['country']
        temp_label['text'] = f'Temperature: {weather_data["main"]["temp"]}°C'
        desc_label['text'] = f'Weather: {weather_data["weather"][0]["description"]}'
    else:
        city_label['text'] = 'City not found'
        temp_label['text'] = ''
        desc_label['text'] = ''


# Submit Method
def on_submit():
    try:
        city = city_entry.get()
        get_weather(city)
    except:
        messagebox.showerror("Network Error","Please Connect the Device to Internet")


# Create the main window
root = tk.Tk()
root.title('Weather App')
root.configure(bg="Light Blue")
root.minsize(width=settings.width, height=settings.height)
root.resizable(False, False)

# Create and pack widgets to the Window
tk.Label(root, text='Enter City:').pack()
city_entry = tk.Entry(root)
city_entry.pack()

submit_button = tk.Button(root, text='Submit', command=on_submit)
submit_button.pack()

city_label = tk.Label(root, text='', font=('Arial', 20))
city_label.pack()

# country_label = tk.Label(root, text='', font=('Arial', 20) )
# country_label.pack()

temp_label = tk.Label(root, text='')
temp_label.pack()

desc_label = tk.Label(root, text='')
desc_label.pack()

root.mainloop()
