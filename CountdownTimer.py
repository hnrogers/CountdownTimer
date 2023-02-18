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

def countdown(seconds):
    while seconds > 0:
        seconds_format = time.strftime("%H:%M:%S", time.gmtime(seconds))
        print(seconds_format + "\t('q' to quit)", end="")
        print("\r", end="")
        seconds -= 1        
        
        if keyboard.is_pressed('q'):
            break
        
        time.sleep(1)
    
    sys.stdout.write("Done!" + " " * 25)    

seconds = validate_number(input("Enter seconds: "))

if seconds != 0:
    countdown(seconds)