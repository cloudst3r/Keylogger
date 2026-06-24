from pynput import keyboard

def on_press(key):
    print(f"got: {key}", flush=True)

with keyboard.Listener(on_press=on_press) as listener:
    print("listener started", flush=True)
    listener.join()