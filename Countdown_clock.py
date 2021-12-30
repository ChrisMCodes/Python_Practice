import time
from datetime import datetime

class Time:
    def __init__(self):
        times = self.get_target()
        self.target_hour = times[0]
        self.target_minute = times[1]
        self.calc_remaining()
        
    def calc_remaining(self):
        complete = False
        while not complete:
                time.sleep(1)
                self.get_current_time()
                self.hour_remaining = self.target_hour - self.current_hour
                self.minute_remaining = self.target_minute - self.current_minute
                self.second_remaining = 60 - self.current_second
                hour_remaining = self.target_hour - self.current_hour
                print()
                print()
                minute_remaining = self.target_minute - self.current_minute
                second_remaining = 60 - self.current_second
                print(f'{hour_remaining:02d}:{minute_remaining:02d}:{second_remaining:02d}')
                complete = self.hour_remaining == 0 and self.minute_remaining == 0
        print('You have reached your goal time!')
        
    def get_current_time(self):
         self.current_hour = datetime.now().hour
         self.current_minute = datetime.now().minute
         self.current_second = datetime.now().second
        
        
    def get_target(self, keep_going=False):
        unit_of_time = False
        while not keep_going:
            unit_of_time = input(f'Input the target hour and minute (using the 24 hour clock, formated as HH:MM): ')
            try:
                unit_of_time = unit_of_time.split(':')
            except Exception:
                print("Please enter a valid time")
            if len(unit_of_time) == 2:
                print(unit_of_time)
                target_hour = int(unit_of_time[0])
                target_minute = int(unit_of_time[1])
                keep_going = True
            else:
                continue
            
            unit_of_time = target_hour >= 0 and target_hour <= 2 and target_minute >= 0 and target_minute <= 60
        return [target_hour, target_minute]
                    
     
def main():
    countdown = Time()
    
main()

    

