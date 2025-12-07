from datetime import datetime

alarmtime=input("enter the time for alarm in HH MM SS (AM/PM):")
try:
    alarmhour,alarmminute,alarmsecond,alarmperiod=alarmtime.split()
    alarmhour=int(alarmhour)
    alarmminute=int(alarmminute)
    alarmsecond=int(alarmsecond)
    alarmperiod=alarmperiod.upper()
except ValueError:
        print("the format is wrong")
        exit(1)
if not(1<=alarmhour<=12,1<=alarmminute<=60,1<=alarmsecond<=60,alarmperiod in ["AM","PM"]):
    print("it is wrong format")
    exit(1)
print("Setting time...")
while True:
    now=datetime.now()
    currenthour=int(now.strftime("%I"))
    currentminute=int(now.strftime("%M"))
    currentsecond=int(now.strftime("%S"))
    currentperiod=now.strftime("%p").upper()
    if (alarmhour==currenthour and
                 alarmminute==currentminute and
                     alarmsecond==currentsecond and
                         alarmperiod==currentperiod):
                            print("Wake up")
                           
                            break
            

        
