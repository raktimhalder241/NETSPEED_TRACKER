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

############### MAPPLOTLIB SECTION ##############

plt.style.use("fivethirtyeight")

#x_indices = np.arange(len(hour))
width = 0.1

col = []
for val in bandwidth:
    if val < 40:
        col.append('red')
    elif val < 60:
        col.append('yellow')
    else:
        col.append('green')

plt.bar(hour, bandwidth, color=col, width=width)

#plt.legend()

plt.title("Bandwidth Analysis")
plt.xlabel("Time (s)")
plt.ylabel("Bandwidth (Mbps)")

plt.tight_layout()

#plt.canvas.set_window_title('Test')

plt.show()