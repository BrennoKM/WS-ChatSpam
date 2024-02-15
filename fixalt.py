import threading
import ctypes
import time
from pynput import keyboard

VK_MENU = 0x12
VK_LEFT = 0x25
VK_Q = 0x51
VK_RETURN = 0x0D
VK_A = 0x41

target_process_name = "Warspear Online"
hwnd = ctypes.windll.user32.FindWindowW(None, target_process_name)

def press_keydown(key_code):
    lparam_down = (1 << 0) | (key_code << 16)
    # lparam_up = (1 << 0) | (key_code << 16) | (1 << 30) | (1 << 31)
    # while altPressed.is_set():
    print("downnn")
    if altPressed.is_set():
        ctypes.windll.user32.keybd_event(key_code, 0, 0, 0)  # press
    # ctypes.windll.user32.PostMessageW(hwnd, 0x100, key_code, lparam_down)  # WM_KEYDOWN
    # time.sleep(0.1)
        # ctypes.windll.user32.PostMessageW(hwnd, 0x101, key_code, lparam_up)  # WM_KEYUP

def press_keyup(key_code):
    # lparam_up = (1 << 0) | (key_code << 16) | (1 << 30) | (1 << 31)
    # while not altPressed.is_set():
    ctypes.windll.user32.keybd_event(key_code, 0, 2, 0)  # release
    # ctypes.windll.user32.PostMessageW(hwnd, 0x101, key_code, lparam_up)  # WM_KEYUP

def skill():
    ctypes.windll.user32.keybd_event(VK_MENU, 0, 0, 0)  # press
    time.sleep(0.1)
    ctypes.windll.user32.PostMessageW(hwnd, 0x100, VK_Q, 0)
    time.sleep(0.1)
    ctypes.windll.user32.keybd_event(VK_MENU, 0, 2, 0)  # release
    ctypes.windll.user32.PostMessageW(hwnd, 0x101, VK_Q, 0)

    # ctypes.windll.user32.PostMessageW(hwnd, 0x100, VK_MENU, 0)  # WM_KEYDOWN
    # time.sleep(0.1)
    # ctypes.windll.user32.PostMessageW(hwnd, 0x100, VK_Q, 0)  # WM_KEYDOWN
    # time.sleep(0.1)
    # ctypes.windll.user32.PostMessageW(hwnd, 0x101, VK_MENU, 0)  # WM_KEYUP
    # time.sleep(0.1)
    # ctypes.windll.user32.PostMessageW(hwnd, 0x101, VK_MENU, 0)  # WM_KEYUP

def on_release(key):
    if key == keyboard.Key.alt_gr:
        # modo_alt(altPressed)
        if not altPressed.is_set():
            print("down")
            altPressed.set()

            th_press = threading.Thread(target=lambda: press_keydown(VK_MENU))
            th_press.start()
            # press_keydown(VK_MENU)
            
        elif altPressed.is_set():
            print("up")
            altPressed.clear()
            press_keyup(VK_MENU)
    if key == keyboard.Key.caps_lock:
        print("skill")
        skill()

def listener():
    with keyboard.Listener(on_release=on_release) as listener:
        listener.join()

global altPressed
altPressed = threading.Event()
altPressed.clear()
# altPressed.set()

th_l = threading.Thread(target=listener)
th_l.start()
th_l.join()