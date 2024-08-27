
    #     vk_code = key.vk  # Obtém o VK code
    #     print(f'Tecla pressionada: {key.char}, VK code: {vk_code}')
    # except AttributeError:
    #     print

import ctypes

def get_vk_code(char):
    # Obter o código virtual (VK code) do caractere
    vk_code = ctypes.windll.user32.VkKeyScanW(ord(char))
    return vk_code & 0xff  # Retornar apenas o código virtual (os 8 bits menos significativos)

# Exemplo de uso
char = '_'
vk_code = get_vk_code(char)
print(f"O VK code do caractere '{char}' é: {vk_code}")