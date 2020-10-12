import os
from datetime import datetime

old_time = ""
current_time = ""

while(1) :
  now = datetime.now()
  current_time = now.strftime("%M")
  if current_time != old_time :
    if int(current_time) % 15 == 0 :
      os.system("python3 ./netspeed_generator/data_generator.py")
      old_time = current_time
