import time
from datetime import datetime

class Time:
    def __init__(self):
        times = self.get_target()
        self.target_hour = times[0]
        self.target_minute = times[1]
        
    def calc_remaining(self):
        complete = False
        while not complete:
                time.sleep(1)
                self.current_hour, self.current_minute, self.current_second = self.get_current_time()
                self.hour_remaining = self.target_hour - self.current_hour
                self.minute_remaining = self.target_minute - self.current_minute
                self.second_remaining = 60 - self.current_second
                print(f'{self.hour_remaining}:{self.minute_remaining}:{self.second_remaining}')
                complete = self.hour_remaining == 0 and self.minute_remaining == 0
                current_time = self.get_current_time()
                hour_remaining = target_hour - current_hour
                minute_remaining = target_minute - current_minute
                second_remaining = 60-current_second
        print('You have reached your goal time!')
        
     def get_current_time(self):
        
        
     def get_target(self):
        unit_of_time == False
        while not unit_of_time:
            unit_of_time == int(input(f'Input the target hour in minute (using the 24 hour clock, formated as HH:MM): '))
            if len(unit_of_time.split(':')) == 2:
                target_hour = unit_of_time[0]
                target_minute = unit_of_time[1]
            else:
                continue
            
            unit_of_time = target_hour >= 0 and target_hour <= 2 and target_minute >= 0 and target_minute <= 60
        return [target_hour, target_minute]
                    
     
def main():
    countdown = Time()
    
main()

    

