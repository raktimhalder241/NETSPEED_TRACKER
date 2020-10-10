# Python program to test 
# internet speed 

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
    current_time = now.strftime("%H:%M:%S")
    current_date = now.strftime("%Y-%m-%d")
    argument_string = ""
    argument_string = argument_string + str('{:.2f}'.format(d / 1024)) + " "
    argument_string = argument_string + str('{:.2f}'.format(u / 1024)) + " "
    argument_string = argument_string + str('{:.2f}'.format(p)) + " "
    argument_string = argument_string + current_time + " "
    argument_string = argument_string + current_date
    print(argument_string)
    os.system("python3 testing_insert.py " + argument_string)

def generate_display_message(d, u, p):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    current_date = now.strftime("%Y-%m-%d")
    print('Results from Test')
    print('Date : ' + current_date)
    print('Time : ' + current_time)
    print('Download: {:.2f} Mbps'.format(d / 1024))
    print('Upload: {:.2f} Mbps'.format(u / 1024))
    print('Ping: {:.2f}'.format(p))

def main():
    count = 1
    for i in range(count):
        d, u, p = test()
        d = round(d / (10**3), 2)
        u = round(u / (10**3), 2)
        generate_display_message(d, u, p)

if __name__ == '__main__':
    main()