from playsound import playsound
import time

CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"
HIDE_CURSOR = "\033[?25l"

def alarm(seconds):
    time_elapsed = 0
    print(CLEAR)
    
    while time_elapsed<seconds:
        time.sleep(1)
        time_elapsed+=1

        time_left = seconds - time_elapsed
        minutes_left = time_left//60
        seconds_left = time_left % 60
        print(HIDE_CURSOR)
        print(f"{CLEAR_AND_RETURN}{minutes_left:02d} : {seconds_left:02d}")

    playsound("C:/Users/user/Downloads/Python/Mini-projects/Alarm.mp3")

minutes = int(input("How many minutes to wait: "))
seconds = int(input("How many seconds to wait: "))
total_seconds = (minutes*60 + seconds)+1

alarm(total_seconds)

