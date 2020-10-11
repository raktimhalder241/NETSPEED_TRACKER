#!/usr/bin/env python3

import tkinter as tk
import requests
import os
import sys
from datetime import datetime

HEIGHT = 900
WIDTH = 1500

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
current_date = now.strftime("%Y-%m-%d")

# background details
background_image = tk.PhotoImage(file='netspeed.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

header = tk.Frame(root, bg='#80c1ff', bd=5)
header.place(relx=0.5, rely=0.1, relwidth=0.8, relheight=0.1, anchor='n')

button_container = tk.Frame(root, bg='#80c1ff', bd=10)
button_container.place(relx=0.25, rely=0.25, relwidth=0.4, relheight=0.4, anchor='n')

# button details
def button_action() :
    os.system("python3 check_current_state.py > temp.txt")
    with open("temp.txt") as file:
        #data = file.read()
        download = file.readline().strip()
        upload = file.readline().strip()
        ping = file.readline().strip() 
    os.system("rm temp.txt")
    label['text'] = "{}\n{}\n{}".format(download, upload, ping)

button = tk.Button(button_container, text="Speed Test", font=40, command=button_action)
button.place(relx=0.3, rely=0.1, relheight=0.2, relwidth=0.5)

# button details
def button_action2() :
    os.system("python3 netspeed_details.py")

button2 = tk.Button(button_container, text="Internet Speed", font=40, command=button_action2)
button2.place(relx=0.3, rely=0.4, relheight=0.2, relwidth=0.5)

# button details
def button_action3() :
    os.system("python3 bandwidth_details.py")

button3 = tk.Button(button_container, text="Bandwidth", font=40, command=button_action3)
button3.place(relx=0.3, rely=0.7, relheight=0.2, relwidth=0.5)

result = tk.Frame(root, bg='#80c1ff', bd=10)
result.place(relx=0.75, rely=0.25, relwidth=0.4, relheight=0.4, anchor='n')

label = tk.Label(result)
label.place(relx=0.5, relwidth=0.2, relheight=0.5)

footer = tk.Frame(root, bg='#80c1ff', bd=5)
footer.place(relx=0.5, rely=0.8, relwidth=0.8, relheight=0.1, anchor='n')

root.mainloop()