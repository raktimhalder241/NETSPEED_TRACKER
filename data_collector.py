# Python program to test 
# internet speed 

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
    # write to csv
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    argument_string = ""
    argument_string = argument_string + str('{:.2f}'.format(d / 1024)) + " "
    argument_string = argument_string + str('{:.2f}'.format(u / 1024)) + " "
    argument_string = argument_string + str('{:.2f}'.format(p)) + " "
    argument_string = argument_string + current_time
    os.system("python3 insert_data.py " + argument_string)

def generate_display_message(d, u, p):
    # simply print in needed format if you want to use pipe-style: python script.py > file
    print('Results from Test')
    print('Download: {:.2f} Mbps'.format(d / 1024))
    print('Upload: {:.2f} Mbps'.format(u / 1024))
    print('Ping: {:.2f}'.format(p))

def main():
    count = 1
    for i in range(count):
        d, u, p = test()
        d = round(d / (10**3), 2)
        u = round(u / (10**3), 2)
        trigger_data_insertion(d, u, p)
        generate_display_message(d, u, p)

if __name__ == '__main__':
    main()