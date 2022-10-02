# Pronounce This Grafana Lib

## Overview

To log data we use the standard output of our pros program, which logs to the usb, to tube data to the computer, which while piping data from the pros terminal will send that information to grafana.

## Logger formatting

To add data to grafana we will use a command formatted as followed with the {name} filled with the name of the variable that you want to log, alphanumeric with no spaces, and the {data} filled with the integer, double, or string that you want to record.

```
{name}: {data}
```

## Running the logger

To run the logger you have to have a grafana server open on port 3000 with live streaming enabled. To run the logger you have to have the robot or controller plugged in to get logger data back from the robot. Then you will pipe the data from the terminal result to the main.py file.

Example command:

```bash
pros terminal | python3 main.py
```

## Helping out

If you want to help out please open an issue or a pull request and we will review it. The code is not written well as I was coming from C++ and just needed a script in python that could tube the data and get the job done. In the future I hope to rewrite this in rust to make it faster as it might be limited by the speed. We also hope to add recording features in the future that will make it so that you can review your past runs and learn from them. 
