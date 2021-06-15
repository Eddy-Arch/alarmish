#!/usr/bin/python3
import time
print("what is the alarm name?\nname: ", end="")
alarmname = input()
print("alarm name will be: " + alarmname)
print("how many hours until the alarm goes off?\ntime: ", end="")
alarmduration_hours = input()
alarmduration_hours = int(alarmduration_hours) * 3600
print("how many minutes until the alarm goes off?\ntime: ", end="")
alarmduration_mins = input()
alarmduration_mins = int(alarmduration_mins) * 60
print("how many seconds until the alarm goes off?\ntime: ", end="")
alarmduration_secs = input()
alarmduration_secs = int(alarmduration_secs)
totalwaittime = alarmduration_secs + alarmduration_mins + alarmduration_hours
print(f'alarm will sound in {totalwaittime} seconds') 
time.sleep(totalwaittime)
print("times up!")
