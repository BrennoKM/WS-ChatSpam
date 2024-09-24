import threading
import ctypes
import time
from pynput import keyboard

VK_MENU = 0x12
VK_CTRL_R = 0xA3
VK_LEFT = 0x25
VK_Q = 0x51
VK_E = 0x45
VK_R = 0x52
VK_RETURN = 0x0D
VK_A = 0x41

target_process_name = "Warspear Online"

hwnd = ctypes.windll.user32.FindWindowW(None, target_process_name)
if not hwnd:
    raise Exception(f"Janela '{target_process_name}' não encontrada")
print(f"Janela '{target_process_name}' encontrada")
# print(hwnd)


def press_keydown(key_code):
    while altPressed.is_set():
        ctypes.windll.user32.keybd_event(key_code, 0, 0, 0)  # press
        time.sleep(0.3)
        press_keyup(key_code)
    # lparam_down = (1 << 0) | (key_code << 16)
    # while altPressed.is_set():
    #     ctypes.windll.user32.PostMessageW(hwnd, 0x100, key_code, lparam_down)  # WM_KEYDOWN
    #     time.sleep(0.1)
def press_keyup(key_code):
    ctypes.windll.user32.keybd_event(key_code, 0, 2, 0)  # release
    # lparam_up = (1 << 0) | (key_code << 16) | (1 << 30) | (1 << 31)
    # ctypes.windll.user32.PostMessageW(hwnd, 0x101, key_code, lparam_up)  # WM_KEYUP


def skill(VK_CODE):
    press_keydown(VK_MENU)
    time.sleep(0.1)
    press_keydown(VK_CODE)
    time.sleep(0.1)
    press_keyup(VK_CODE)
    press_keyup(VK_MENU)

def colored(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"

def on_release(key):
    if key == keyboard.Key.ctrl_r:
        # modo_alt(altPressed)
        if not altPressed.is_set():
            print(colored("FixAlt On", 32))
            altPressed.set()

            th_press = threading.Thread(target=lambda: press_keydown(VK_MENU))
            th_press.start()
            # press_keydown(VK_MENU)
            
        elif altPressed.is_set():
            altPressed.clear()
            print(colored("FixAlt Off", 31))
            press_keyup(VK_MENU)
    if key == keyboard.Key.caps_lock:
        # skill(VK_R)
        # skill(VK_E)
        pass


def listener():
    with keyboard.Listener(on_release=on_release) as listener:
        listener.join()

global altPressed
altPressed = threading.Event()
# altPressed.set()
altPressed.clear()

print("Programa iniciado. Pressione Ctrl_right para ativar/desativar o modo FixAlt")

th_l = threading.Thread(target=listener)
th_l.start()
th_l.join()
