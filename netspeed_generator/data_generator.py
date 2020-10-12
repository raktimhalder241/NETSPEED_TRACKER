import os
import speedtest
from datetime import datetime

def test():
    s = speedtest.Speedtest()
    s.get_servers()
    s.get_best_server()
    s.download()
    s.upload()
    res = s.results.dict()
    return res["download"], res["upload"], res["ping"]

def trigger_data_insertion(d, u, p):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    current_date = now.strftime("%Y-%m-%d")
    argument_string = ""
    argument_string = argument_string + str('{:.2f}'.format(d / 1024)) + " "
    argument_string = argument_string + str('{:.2f}'.format(u / 1024)) + " "
    argument_string = argument_string + str('{:.2f}'.format(p)) + " "
    argument_string = argument_string + current_time + " "
    argument_string = argument_string + current_date
    os.system("python3 ./netspeed_generator/insert_data.py " + argument_string)

def main():
    count = 1
    for i in range(count):
        d, u, p = test()
        d = round(d / (10**3), 2)
        u = round(u / (10**3), 2)
        trigger_data_insertion(d, u, p)

if __name__ == '__main__':
    main()
