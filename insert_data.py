import sys
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="12345678",
  database="netspeed",
  auth_plugin='mysql_native_password'
)

mycursor = mydb.cursor()

sql = "INSERT INTO netspeed_data (download, upload, ping, time, date) VALUES (%s, %s, %s, %s, %s)"
val = (sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
mycursor.execute(sql, val)

mydb.commit()
