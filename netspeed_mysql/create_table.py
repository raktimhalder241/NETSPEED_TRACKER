import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="12345678",
  database="netspeed",
  auth_plugin='mysql_native_password'
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE netspeed_data (download DECIMAL(6,2), upload DECIMAL(6,2), ping DECIMAL(6,2), time VARCHAR(255))")
