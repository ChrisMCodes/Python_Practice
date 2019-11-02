import time
from datetime import datetime

now = datetime.now()
current_time = int(now.strftime('%H%M%S'))
target = 000000

#This needs cleanup
while True:
    if target < current_time: 
        target = int(input('Input a target time before midnight today in the format "HHMMSS" (please do not use quotes and use the standard 24-hour clock): '))
    else:
        break
#Needs to adjust to subtract from 60

print('The current time is: ', current_time)
print('Now counting down to the time you entered:')
while target > current_time:
    print(target - current_time)
    time.sleep(1)
    now = datetime.now()
    current_time = int(now.strftime('%H%M%S'))
    

