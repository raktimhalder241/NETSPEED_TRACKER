#!/usr/bin/env python3

# Python program to test 
# internet speed 

import speedtest

def test():
    s = speedtest.Speedtest()
    s.get_servers()
    s.get_best_server()
    s.download()
    s.upload()
    res = s.results.dict()
    return res["download"], res["upload"], res["ping"]

def generate_display_message(d, u, p):
    print('{:.2f}'.format(d / 1024))
    print('{:.2f}'.format(u / 1024))
    print('{:.2f}'.format(p))

def main():
    count = 1
    for i in range(count):
        d, u, p = test()
        d = round(d / (10**3), 2)
        u = round(u / (10**3), 2)
        generate_display_message(d, u, p)

if __name__ == '__main__':
    main()
