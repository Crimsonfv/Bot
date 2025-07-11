import time
import pyautogui

print('Vamos a testear el control y verificar que las teclas precionadas interacutan con el emulador')


def Press_A():
    pyautogui.keyDown('l')
    time.sleep(0.2)
    pyautogui.keyUp('l')

def Press_B():
    pyautogui.keyDown('k')
    time.sleep(0.2)
    pyautogui.keyUp('k')

def Press_Start():
    pyautogui.keyDown('e')
    time.sleep(0.2)
    pyautogui.keyUp('e')

def Press_Select():
    pyautogui.keyDown('r')
    time.sleep(0.2)
    pyautogui.keyUp('r')

def Press_Arriba():
    pyautogui.keyDown('w')
    time.sleep(0.2)
    pyautogui.keyUp('w')

def Press_Abajo():
    pyautogui.keyDown('s')
    time.sleep(0.2)
    pyautogui.keyUp('s')

def Press_Izquierda():
    pyautogui.keyDown('a')
    time.sleep(0.2)
    pyautogui.keyUp('a')

def Press_Derecha():
    pyautogui.keyDown('d')
    time.sleep(0.2)
    pyautogui.keyUp('d')


def SoftReset():
    print("Ejecutando Soft Reset (A + B + Start + Select)...")
    
    pyautogui.keyDown('l')  
    pyautogui.keyDown('k')  
    pyautogui.keyDown('e')  
    pyautogui.keyDown('r')  
    
    time.sleep(0.2)  # 200ms suele ser suficiente
    
    # Soltar todas las teclas
    pyautogui.keyUp('r')  
    pyautogui.keyUp('e')  
    pyautogui.keyUp('k')  
    pyautogui.keyUp('l')  
    
    print("Soft Reset completado!")