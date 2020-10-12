#!/usr/bin/env python3

import mysql.connector
from matplotlib import pyplot as plt
import numpy as np

hour, minute, bandwidth = [], [], []

############### MYSQL SECTION ############## 
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="12345678",
  database="netspeed",
  auth_plugin='mysql_native_password'
)

mycursor = mydb.cursor()

sql = "select hour, minute, avg(download), avg(upload) from (select download, upload, hour(time) as hour, minute(time) as minute from netspeed_data) as main_table group by hour, minute order by hour, minute"
mycursor.execute(sql)
mycursor.fetchall()
rcount = int(mycursor.rowcount)

mycursor.execute(sql)
for r in range(rcount) :
  row = mycursor.fetchone()
  
  hour.append(row[0] + row[1]/60)
  bandwidth.append(row[2] + row[3])

mydb.close()

############### MATPLOTLIB SECTION ##############

plt.style.use("fivethirtyeight")

fig = plt.figure(figsize=(20, 8))
fig.canvas.set_window_title('Bandwidth Details')
plt.xticks(np.arange(min(hour), max(hour)+1, 1.0))

width = 0.1

col = []
for val in bandwidth:
    if val < 70:
        col.append('red')
    elif val < 90:
        col.append('yellow')
    else:
        col.append('green')

plt.bar(hour, bandwidth, color=col, width=width)

plt.title("Bandwidth Analysis")
plt.xlabel("Time (hour)")
plt.ylabel("Bandwidth (Mbps)")

plt.tight_layout()

plt.show()