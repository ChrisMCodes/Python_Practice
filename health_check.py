#!/usr/bin/env python3

# This simple program can be called in the command line and used to check a computer's disk space and CPU usage.
# I've made it here so that it can be run locally, but for scalability purposes, the functions return boolean values
# So that you can simply delete the print statements and everything below the functions and import this into whatever custom script you need.
# Feedback is always welcome

# You will need to have psutil installed.
# If you are on Ubuntu, psutil will probably be installed but only track to the python variable (for Python 2)
# To use it in Python 3, you'll probably want to use:
# sudo apt install -y python3-psutil


import shutil
import psutil

def check_disk_usage(disk):
	'''Returns True if disk usage is under 80%'''
	du = shutil.disk_usage(disk)
	free = du.free / du.total * 100
	print("{:.2f}% of your disk is free".format(free))
	return free > 20

def check_cpu_usage():
	'''Returns True if CPU usage averages under 75% over three seconds'''
	print("Checking CPU usage...")
	usage = psutil.cpu_percent(3)
	print("Your CPU averaged {:.2f}% utilization over 3 seconds".format(usage))
	return usage < 75

if not check_disk_usage("/") or not check_cpu_usage():
	print("ERROR!")
else:
	print("Everything is ok")

print("Press any key to close program")
close_it = input()
