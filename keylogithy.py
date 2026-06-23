import pynput

from pynput import keyboard

print("script doing its thing")

def on_press(key):
    print(f"Raw: {key}")
    print(f"Type: {type(key)}")
    print("---")

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()