import time
import sys
import keyboard

def validate_number(user_input):
    try:
        n = int(user_input, base=10)
    except ValueError:
        print("Invalid entry.")
        return 0
    else:
        return n

def countdown(seconds, fps):
    fps = 1/fps
    last = time.time()
    printed = False
    
    while seconds > 0:
        if printed is False:
            seconds_format = time.strftime("%H:%M:%S", time.gmtime(seconds))
            print(seconds_format + "\t('q' to quit)", end="")
            print("\r", end="")
            printed = True
        
        if time.time() - last >= 1:
            printed = False
            last = time.time()
            seconds -= 1
                        
        if keyboard.is_pressed('q'):
            break
        
        time.sleep(fps)
        
    sys.stdout.write("Done!" + " " * 25)    

seconds = validate_number(input("Enter seconds: "))
if seconds != 0:
    countdown(seconds, 60)