import pyautogui as pg
from pynput import keyboard
import threading

def listener():
    with keyboard.Listener(on_release=on_release) as listener:
        listener.join()

def on_release(key):
    try:
        # if key.char == "k":
        #     spam(string)
        # if key.char == "l":
        #     print("L")
        if key == keyboard.Key.alt_gr:
            if not myEvent.is_set():
                myEvent.set()
                th_spam = threading.Thread(target=spam)
                th_spam.start()
                print("Ligado")
            else:
                myEvent.clear()
                print("Desligado")
        # if key == keyboard.key.right_ctrl:
        #     myEvent.clear()
    except AttributeError:
                pass

def spam():
    while myEvent.is_set():
        pg.typewrite(string, interval=0.01)
        pg.press('enter')
        pg.sleep(60)

global string
string = "gId 100k por 10 brazucas :)"


global myEvent
myEvent = threading.Event()
myEvent.clear()

th_l = threading.Thread(target=listener)
th_l.start()
th_l.join()
