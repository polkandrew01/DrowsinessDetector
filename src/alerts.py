from threading import Thread
import playsound


def sound_alarm(path):
    playsound.playsound(path)

def alert_value(on_off):
    
    #print("in the function")
    while(on_off == True):
        t = Thread(target=sound_alarm,
                   args=("../assets/alarm.wav",))
        t.deamon = True
        t.start()
       # sound_alarm("../assets/alarm.wav")
        
        
    elif(on_off == False):
        return
