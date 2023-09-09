
#João Lopes------------------------------
#Copyright-------------------------------
import psutil
from win11toast import ToastNotification
from win11toast import toast
# from utils.constants import USER
import time
import os
import threading

USER = os.getlogin()
def check_by_10_thread():
    while True:
        battery = psutil.sensors_battery()
        bateria = battery.percent
        if bateria % 10 == 0:
            toast(f'{USER} You have {bateria}%  of battery ')
        time.sleep(180)  


def check_battery_status():
    battery = psutil.sensors_battery()
    
    if battery and battery.power_plugged and battery.percent == 100:
        toaster = ToastNotification()
        toaster.show_toast(f'{USER} Your battery is fully charged. Unplug your charger to preserve battery health.',
                           duration=10)
    else:
        toast('you still have battery left')
        
def main():
    threading.Thread(target=check_by_10_thread).start()
    while True:
        check_battery_status()
        
        time.sleep(300) 
      

if __name__ == "__main__":
    main()

        
    

