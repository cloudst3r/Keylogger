from pynput.keyboard import Listener

def show(key):
    print("GOT KEY:", key)

with Listener(on_press=show) as listener:
    listener.join()