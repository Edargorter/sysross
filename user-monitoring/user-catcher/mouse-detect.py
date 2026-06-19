from evdev import InputDevice, categorize, ecodes
import threading 
from multiprocessing import Process
from os import system, environ
from time import sleep
from datetime import datetime 
import sys 
import time 

lock_command = "loginctl lock-session"
# lock_command = "xdg-screensaver lock"

def record():
	# cap_cmd = "./capture-webcam.sh"
	cap_cmd = "./capture-evidence.sh"
	system(cap_cmd)

def detect(stop_event):
    mouse_event = environ['MOUSE_EVENT']
    disp = 'zenity --info --title "ALERT" --text "Tampering detected! Evidence Captured - let\'s hope you were smiling :)  \" &'
    dev = InputDevice(f"/dev/input/{mouse_event}")  # replace with your mouse event

    for event in dev.read_loop():
        if stop_event.is_set():
            return 
        if event.type == ecodes.EV_REL:  # relative motion
            ctime = datetime.now()
            print(f"Mouse moved: {ctime}")
            # your action here
            system(disp)
            p = Process(target=record)
            p.start()
            sleep(4)
            system(lock_command)
            break
        if time.time() - start_time > duration:
            break

if __name__ == "__main__":
    print("waiting...")
    stop_event = threading.Event()
    t_thread = threading.Thread(target=detect, args=(stop_event,))
    t_thread.start()

    duration = 15 * 60

    time.sleep(duration)
    stop_event.set()

    t_thread.join()
