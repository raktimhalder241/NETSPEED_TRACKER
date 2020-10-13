# NETSPEED_TRACKER

Description:
------------
1. Build an app which will run speed test on the internet connection and will present results.
2. Figure out the speeds at different times of the day to figure out which is the optimum time for user to browse.
3. Do multiple tests to figure the average and notify user if the expected latency/speed drops (If possible).
4. Basically check if the promised bandwidth/speed is provided and notify if not.

Reference:
----------
https://support.ookla.com/hc/en-us/articles/115002187768-Speedtest-Intelligence-Data-Extracts-API

Structure :
---------
3 Major sections -
1. Data generation : https://github.com/raktimhalder241/NETSPEED_TRACKER/tree/main/netspeed_generator
2. GUI : https://github.com/raktimhalder241/NETSPEED_TRACKER/tree/main/netspeed_gui
3. Monitoring : https://github.com/raktimhalder241/NETSPEED_TRACKER/blob/main/start_netspeed_monitoring.sh

Instruction :
------------

1. Clone the Repo.
2. Open terminal in the NETSPEED_TRACKER/ directory
3. Complete MySQL setup as shown in https://github.com/raktimhalder241/NETSPEED_TRACKER/tree/main/netspeed_mysql
4. Run command "$ bash start_netspeed_generator.sh" to generate data. This takes data every 15 minutes at 00, 15, 30, 45 each hour.
5. Run command "$ bash start_netspeed_gui.sh" to open GUI to test internet speed.
6. Complete Grafana setup as shown in https://github.com/raktimhalder241/NETSPEED_TRACKER/tree/main/netspeed_grafana
7. Run command "$ bash start_netspeed_monitoring.sh" to start Grafana on Firefox browser.
8. Run command "$ bash stop_netspeed_monitoring.sh" to stop Grafana service.
