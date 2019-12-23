import tkinter as tk
from tkinter import font
import requests
import PIL
from PIL import Image
def test_func(entry):
    print("Hello... this is ",entry)
#key
#f8c67af3c6564333f6f5cacdd6a71769
#api.openweathermap.org/data/2.5/forecast?q={city name},{country code}
def format_response(weather):
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']
        final_str = 'City : %s\nConditions : %s\nTemperature : %s C' % (name,desc,temp)
    except:
        final_str = "Error"
    return final_str


def get_weather(city):
    weather_key = 'f8c67af3c6564333f6f5cacdd6a71769'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID' : weather_key, 'q':city, 'units':'Metric'}
    response = requests.get(url, params=params)
    weather = response.json()
    print(weather)
    lower_label['text'] = format_response(weather)

root = tk.Tk()

canvas = tk.Canvas(root, height=500, width=400, bg="white")
canvas.pack()

'''
bg_image = tk.PhotoImage("weather_app_bg_img.jpg")
bg_label = tk.Label(root, image=bg_image)
bg_label.place(x=0,y=0,relheight=1,relwidth=1)
'''
frame = tk.Frame(root, bg="#99ceff",bd=5)
frame.place(relx=0.05, rely=0.1, relwidth = 0.9, relheight= 0.2)

label = tk.Label(frame, text= "Enter pin code or specified place", bg="#F2DC3D")
label.pack(side = 'top', fill='x')

entry = tk.Entry(frame, bg="white")
entry.place(relx= 0.1,rely=0.5, relheight=0.2, relwidth=0.6)

#here i used lambda
button = tk.Button(frame, text="Get Weather",command= lambda: get_weather(entry.get()), bg="#E5DCDB", fg="#2AB75C", activebackground="#B7B7B1", activeforeground = "red")
button.place(relx="0.7", rely="0.5", relheight="0.2", relwidth="0.2")


'''-------------------------------------------------'''
lower_frame = tk.Frame(root, bg="#99ceff",bd=5)
lower_frame.place(relx=0.05, rely=0.4, relwidth = 0.9, relheight= 0.5)

lower_label = tk.Label(lower_frame, text="", bg="white", font=('Modern',20))
lower_label.place(relheight=0.8, relwidth=0.9, relx=0.05, rely=0.1)


root.mainloop()
