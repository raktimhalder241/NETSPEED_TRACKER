#!/usr/bin/env python3

import mysql.connector
import os

download, upload, ping, time, date = [], [], [], [], []

############### MYSQL SECTION ############## 
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="12345678",
  database="netspeed",
  auth_plugin='mysql_native_password'
)

mycursor = mydb.cursor()

sql = "select * from netspeed_data"
mycursor.execute(sql)
mycursor.fetchall()
rcount = int(mycursor.rowcount)

mycursor.execute(sql)
for r in range(rcount) :
  row = mycursor.fetchone()
  
  download.append(row[0])
  upload.append(row[1])
  ping.append(row[2])
  time.append(row[3])
  date.append(row[4])

mydb.close()

############### CSV SECTION ##############

os.system("echo \"download,upload,ping,time,date\" > netspeed_data.csv")
for i in range(len(download)) :
  entry = str(download[i]) +','+ str(upload[i]) +','+ str(ping[i]) +','+ time[i] +','+ date[i]
  os.system("echo \"" + entry + "\" >> netspeed_data.csv")