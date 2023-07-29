import psutil
from win11toast import ToastNotification
from win11toast import toast
import time

def check_battery_status():
    battery = psutil.sensors_battery()
    
    if battery and battery.power_plugged and battery.percent == 100:
        toaster = ToastNotification()
        toaster.show_toast("Battery Full",
                           "Your battery is fully charged. Unplug your charger to preserve battery health.",
                           duration=10)
    else:
        toast('you still have battery left')
        
        

        

def main():
    while True:
        check_battery_status()
        time.sleep(300)  

if __name__ == "__main__":
    main()

        
    

