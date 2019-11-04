import time
from datetime import datetime


def countdown():
    current_hour = datetime.now().hour
    current_minute = datetime.now().minute
    current_second = datetime.now().second
    target_hour = int(input('Input the target HOUR using the 24 hour clock: '))
    target_minute = int(input('Input the target MINUTE: '))
    hour_remaining = target_hour - current_hour
    minute_remaining = target_minute - current_minute
    second_remaining = 60-current_second
    while hour_remaining >= 0:
        while minute_remaining >=0:
            print('{}:{}:{}'.format(hour_remaining, minute_remaining, second_remaining))
            time.sleep(1)
            current_hour = datetime.now().hour
            current_minute = datetime.now().minute
            current_second = datetime.now().second
            hour_remaining = target_hour - current_hour
            minute_remaining = target_minute - current_minute
            second_remaining = 60-current_second
    print('You have reached your goal time!')

countdown()

    

