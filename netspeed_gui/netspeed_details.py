#!/usr/bin/env python3

import mysql.connector
from matplotlib import pyplot as plt
import numpy as np

hour, minute, download, upload = [], [], [], []

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
  
  hour.append(row[0])
  minute.append(row[1])
  download.append(row[2])
  upload.append(row[3] * -1)

mydb.close()

############### MATPLOTLIB SECTION ##############

plt.style.use("fivethirtyeight")

fig = plt.figure(figsize=(20, 8))
fig.canvas.set_window_title('Netspeed Details')
plt.xticks(np.arange(min(hour), max(hour)+1, 1.0))

width = 0.5

plt.bar(hour, download, color="blue", width=width, label="Download")
plt.bar(hour, upload, color="red", width=width, label="Upload")

plt.legend()

plt.title("Internet Speed Analysis")
plt.xlabel("Time (hour)")
plt.ylabel("Internet speed (Mbps)")

plt.tight_layout()

plt.show()