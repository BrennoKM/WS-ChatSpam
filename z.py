import ctypes
import time

# Definir algumas constantes
INPUT_KEYBOARD = 1
KEYEVENTF_UNICODE = 0x0004
KEYEVENTF_KEYUP = 0x0002

# Definir a estrutura KEYBDINPUT
class KEYBDINPUT(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", ctypes.POINTER(ctypes.c_ulong))]

# Definir a estrutura INPUT
class INPUT(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ki", KEYBDINPUT)]

# Função para simular a pressão de uma tecla
def press_key(key):
    input_struct = INPUT(INPUT_KEYBOARD, KEYBDINPUT(key, 0, KEYEVENTF_UNICODE, 0, None))
    ctypes.windll.user32.SendInput(1, ctypes.pointer(input_struct), ctypes.sizeof(INPUT))

# Função para simular a liberação de uma tecla
def release_key(key):
    input_struct = INPUT(INPUT_KEYBOARD, KEYBDINPUT(key, 0, KEYEVENTF_UNICODE | KEYEVENTF_KEYUP, 0, None))
    ctypes.windll.user32.SendInput(1, ctypes.pointer(input_struct), ctypes.sizeof(INPUT))

# Aguarde um momento antes de começar a digitar (opcional)
time.sleep(2)

# Digite o texto "Hello, World!"
for char in "Hello, World!":
    press_key(ord(char))
    release_key(ord(char))
    time.sleep(0.1)  # Ajuste conforme necessário
