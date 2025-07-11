import pyautogui as py
import json
import time


def SaberPosicion():
    while True:
        x,y =py.position()
        r,g,b = py.pixel(x,y)
        print(f'x: {x}, y = {y} RGB = {r,g,b}')
        time.sleep(1)

with open('EmuladorPosicion/posiciones.json', 'r', encoding='utf-8') as file:
    datos = json.load(file)


def CalcularPixelTreecko():
    # 152,208,72
    ColorPixelTreecko = []
    for dato in datos:
        a = 92
        b = 170
        datox = dato['x']
        datoy = dato['y']
        time.sleep(0.05)
        a = datox + a
        b = datoy + b
        color = py.pixel(a,b)
        ColorPixelTreecko.append(color)
    return ColorPixelTreecko

def EleccionPokemonTreecko():
    #216, 168, 88
    ColoresEleccionPokemonTreecko = []
    for dato in datos:
        a = 125
        b = 98
        datox = dato['x']
        datoy = dato['y']
        time.sleep(0.05)
        a = datox + a
        b = datoy + b
        color = py.pixel(a,b)
        ColoresEleccionPokemonTreecko.append(color)
    
    return ColoresEleccionPokemonTreecko


def PartidaGuardada():
    #248, 248, 248
    ColoresPartidaGuardada = []
    for dato in datos:
        a = 212
        b = 96
        datox = dato['x']
        datoy = dato['y']
        time.sleep(0.05)
        a = datox + a
        b = datoy + b
        color = py.pixel(a,b)
        ColoresPartidaGuardada.append(color)
    
    return ColoresPartidaGuardada


def BatallaMenu():
    #248, 248, 248
    ColoresBatallaMenu = []
    for dato in datos:
        a = 265
        b = 245
        datox = dato['x']
        datoy = dato['y']
        time.sleep(0.05)
        a = datox + a
        b = datoy + b
        color = py.pixel(a,b)
        ColoresBatallaMenu.append(color)
    
    return ColoresBatallaMenu

def BatallaPregunta():
    #104, 160, 160
    ColoresBatallaPregunta = []
    for dato in datos:
        a = 130
        b = 228
        datox = dato['x']
        datoy = dato['y']
        time.sleep(0.05)
        a = datox + a
        b = datoy + b
        color = py.pixel(a,b)
        ColoresBatallaPregunta.append(color)
    
    return ColoresBatallaPregunta

def BatallaInfo():
    #248, 248, 216
    ColoresBatallaInfo = []
    for dato in datos:
        a = 183
        b = 194
        datox = dato['x']
        datoy = dato['y']
        time.sleep(0.05)
        a = datox + a
        b = datoy + b
        color = py.pixel(a,b)
        ColoresBatallaInfo.append(color)
    
    return ColoresBatallaInfo

#print(BatallaMenu())

# colores = CalcularPixelTreecko()
# color_buscado = (152,208,72)

# coincidencias = colores.count(color_buscado)
# print(f'Se encontraron {coincidencias} colores iguales')

# if coincidencias > 0:
#     print('Al menos un color coincide')

