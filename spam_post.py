import pyautogui as pg
from pynput import keyboard
import threading
import ctypes
from ctypes import c_char
import time

target_process_name = "Warspear Online"
hwnd = ctypes.windll.user32.FindWindowW(None, target_process_name)


# https://learn.microsoft.com/pt-br/windows/win32/inputdev/virtual-key-codes

WM_KEYDOWN = 0x100
WM_KEYUP = 0x101
WM_MOUSEMOVE = 0X0200

MK_LBUTTON = 0X0001

VK_MENU = 0x12
VK_LEFT = 0x25
VK_RETURN = 0x0D
VK_LEFT = 0x25

VK_0 = 0x30	#   0 key
VK_1 = 0x31	#   1 key
VK_2 = 0x32	#   2 key
VK_3 = 0x33	#   3 key
VK_4 = 0x34 #	4 key
VK_5 = 0x35 #	5 key
VK_6 = 0x36 #	6 key
VK_7 = 0x37 #	7 key
VK_8 = 0x38 #	8 key
VK_9 = 0x39 #	9 key

VK_A = 0x41 #	A key
VK_B = 0x42 #	B key
VK_C = 0x43 #	C key
VK_D = 0x44 #	D key
VK_E = 0x45 #	E key
VK_F = 0x46 #	F key
VK_G = 0x47 #	G key
VK_H = 0x48 #	H key
VK_I = 0x49 #	I key
VK_J = 0x4A #	J key
VK_K = 0x4B #	K key
VK_L = 0x4C #	L key
VK_M = 0x4D #	M key
VK_N = 0x4E #	N key
VK_O = 0x4F #	O key
VK_P = 0x50 #	P key
VK_Q = 0x51 #	Q key
VK_R = 0x52 #	R key
VK_S = 0x53 #	S key
VK_T = 0x54 #	T key
VK_U = 0x55 #	U key
VK_V = 0x56 #	V key
VK_W = 0x57 #	W key
VK_X = 0x58 #	X key
VK_Y = 0x59 #	Y key
VK_Z = 0x5A #	Z key
VK_Ç = 0xBA #   Ç key

VK_OEM_1 = 0xBF # ;:
VK_OEM_3 = 0xDE # ~^
VK_SPACE = 0x20 # espaço
VK_SHIFT = 0x10  # Shift
VK_OEM_COMMA = 0xBC # ,<


def spam(char):
    ctypes.windll.user32.PostMessageW(hwnd, WM_KEYDOWN, char, 0)  # WM_KEYDOWN
    time.sleep(0.1)
    ctypes.windll.user32.PostMessageW(hwnd, WM_KEYUP, char, 0)  # WM_KEYUP
    print("apertou")

def digitar(string):
    for char in string:
        if myEvent.is_set():
            char_upper = char.upper()
            if 'A' <= char_upper <= 'Z':
                vk_code = globals()[f'VK_{char_upper}']
                if char == char_upper:
                    spam_scan(vk_code, True)
                else:
                    spam_scan(vk_code, False)
            elif '0' <= char <= '9':
                vk_code = globals()[f'VK_{char}']
                spam_scan(vk_code)
            elif ' ' == char:
                spam_scan(VK_SPACE)
            elif ':' == char:
                spam_scan(VK_OEM_1, True)
            elif 'ç' == char:
                spam_scan(VK_Ç) 
            elif ',' == char:
                spam_scan(VK_OEM_COMMA)
            elif 'ã' == char:
                spam_scan(VK_OEM_3)
                spam_scan(VK_A)
            elif 'ô' == char:
                spam_scan(VK_OEM_3, True)
                time.sleep(0.09)
                spam_scan(VK_O)
            else:
                # Handle other characters as needed
                pass
            time.sleep(0.02)
    if myEvent.is_set():
        spam_scan(VK_RETURN)
        time.sleep(2)


def spam_scan(scan_code, shift = False):
    lparam_down = (1 << 0) | (scan_code << 16)
    lparam_up = (1 << 0) | (scan_code << 16) | (1 << 30) | (1 << 31)
    
    if shift:
        ctypes.windll.user32.keybd_event(VK_SHIFT, 0, 0, 0)  # press Shift
        time.sleep(0.03)
    ctypes.windll.user32.PostMessageW(hwnd, 0x100, scan_code, lparam_down)  # WM_KEYDOWN
    time.sleep(0.03)
    ctypes.windll.user32.PostMessageW(hwnd, 0x101, scan_code, lparam_up)  # WM_KEYUP

    if shift:
        ctypes.windll.user32.keybd_event(VK_SHIFT, 0, 2, 0)  # release Shift

def move_to(x, y):
     x = int(x)
     y = int(y)
     lParam = (y << 16) | x
     ctypes.windll.user32.PostMessageW(hwnd, WM_MOUSEMOVE, MK_LBUTTON, lParam)

def click():
    pass


def listener():
    with keyboard.Listener(on_release=on_release) as listener:
        listener.join()

def on_release(key):
    # try:
    #     vk_code = key.vk  # Obtém o VK code
    #     print(f'Tecla pressionada: {key.char}, VK code: {vk_code}')
    # except AttributeError:
    #     print(f'Tecla especial pressionada: {key}, VK code: {key.vk}')
    try:
        # if key.char == "k":
        #     spam(string)
        # if key.char == "l":
        #     move_to(100,100)
        if key == keyboard.Key.alt_gr:
            if not myEvent.is_set():
                myEvent.set()
                th_spam = threading.Thread(target=spamar)
                th_spam.start()
                print("Ligado")
            else:
                myEvent.clear()
                print("Desligado")
        # if key == keyboard.Key.esc:
        #     myEvent.clear()
    except AttributeError:
                pass

def spamar():
    while myEvent.is_set():
        digitar(string1)
        digitar(string2)
        digitar(string3)
        time.sleep(40)

global string1, string2, string3
string1 = "Alô, me chama no zap 85 08130 2220 :flowergrinch::kissing:"
string2 = "Faço craft Corpo a Corpo, Longo alcance e Tecido :parrot4:"
string3 = "Mão de obra por 50k com coins e licença incluso :gift:"
# print(string)

global myEvent
myEvent = threading.Event()
myEvent.clear()

th_l = threading.Thread(target=listener)
th_l.start()
th_l.join()
