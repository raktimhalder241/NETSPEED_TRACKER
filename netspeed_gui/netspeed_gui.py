#!/usr/bin/env python3

import tkinter as tk
import requests
import os
import sys
import time
from datetime import datetime

#####################   FRAME SETUP   ####################

HEIGHT = 900
WIDTH = 1500

root = tk.Tk()
root.title('Netspeed Home Page')

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

# background details
background_image = tk.PhotoImage(file='./netspeed_gui/netspeed.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

#####################   HEADER SETUP   ####################

header = tk.Frame(root, bg='#BDC3C7', bd=5)
header.place(relx=0.5, rely=0.05, relwidth=0.8, relheight=0.15, anchor='n')

def tick():
    time_string = time.strftime('%H:%M:%S')
    clock.config(text=time_string)
    clock.after(1000, tick)

clock = tk.Label(header, font=('times', 20, 'bold'), bg='#BDC3C7')
clock.grid(row=0, column=1)
clock.place(relx=0.2, rely=0.25, relwidth=0.3, relheight=0.5, anchor='n')
tick()

app_name = tk.Label(header, text="NETSPEED TRACKER", font=('times', 20, 'bold'), bg='#909497')
app_name.place(relx=0.5, rely=0.25, relwidth=0.3, relheight=0.5, anchor='n')

def todate():
    date_string = time.strftime('%d-%m-%Y')
    calender.config(text=date_string)
    calender.after(1000, todate)

calender = tk.Label(header, font=('times', 20, 'bold'), bg='#BDC3C7')
calender.grid(row=0, column=1)
calender.place(relx=0.8, rely=0.25, relwidth=0.3, relheight=0.5, anchor='n')
todate()

#####################   BUTTON CONTAINER SETUP   ####################

button_container = tk.Frame(root, bg='#80c1ff', bd=10)
button_container.place(relx=0.25, rely=0.25, relwidth=0.4, relheight=0.5, anchor='n')

def speedtest() :
    os.system("speedtest-cli --simple > temp.txt")
    with open("temp.txt") as file:
        data = file.read()
        label_result['text'] = data
    os.system("rm temp.txt")


button_speedtest = tk.Button(button_container, text="Speed Test", font=40, command=speedtest)
button_speedtest.place(relx=0.25, rely=0.1, relheight=0.2, relwidth=0.5)

def netspeed() :
    os.system("python3 ./netspeed_gui/netspeed_details.py")

button_netspeed = tk.Button(button_container, text="Internet Speed", font=40, command=netspeed)
button_netspeed.place(relx=0.25, rely=0.4, relheight=0.2, relwidth=0.5)

def bandwidth() :
    os.system("python3 ./netspeed_gui/bandwidth_details.py")

button_bandwidth = tk.Button(button_container, text="Bandwidth", font=40, command=bandwidth)
button_bandwidth.place(relx=0.25, rely=0.7, relheight=0.2, relwidth=0.5)

#####################   RESULT SETUP   ####################

result = tk.Frame(root, bg='#80c1ff', bd=10)
result.place(relx=0.75, rely=0.25, relwidth=0.4, relheight=0.5, anchor='n')

label_result = tk.Label(result, font=('times', 15, 'bold'), bg='#BDC3C7')
label_result.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
label_result['text'] = "Speed Test may take upto a minute.\nIn the mean time the App might seem to freeze.\nDon't Panic."

#####################   FOOTER SETUP   ####################

footer = tk.Frame(root, bg='#BDC3C7', bd=5)
footer.place(relx=0.5, rely=0.8, relwidth=0.8, relheight=0.15, anchor='n')

sponsor = tk.Label(footer, text="NA", font=('times', 15, 'bold'), bg='#BDC3C7')
sponsor.place(relx=0.25, rely=0.2, relwidth=0.4, relheight=0.3, anchor='n')

ip_address = tk.Label(footer, text="NA", font=('times', 15, 'bold'), bg='#BDC3C7')
ip_address.place(relx=0.75, rely=0.2, relwidth=0.4, relheight=0.3, anchor='n')

server = tk.Label(footer, text="NA", font=('times', 15, 'bold'), bg='#BDC3C7')
server.place(relx=0.25, rely=0.6, relwidth=0.4, relheight=0.3, anchor='n')

server_id = tk.Label(footer, text="NA", font=('times', 15, 'bold'), bg='#BDC3C7')
server_id.place(relx=0.75, rely=0.6, relwidth=0.4, relheight=0.3, anchor='n')

os.system("speedtest-cli --csv > temp.txt")
with open("temp.txt") as file:
    data = file.read()
    output = [str(s) for s in data[:-1].split(',')]
    sponsor["text"] = "Sponsor : "+output[1]
    server["text"] = "Server : "+output[2]
    ip_address["text"] = "IP Address : "+output[-1]
    server_id["text"] = "Server ID : "+output[0]
os.system("rm temp.txt")

#####################   FINALLY   ####################

root.mainloop()
