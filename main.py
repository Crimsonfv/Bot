from AbrirEmulador import AbrirEmulador
from Posicion import DetectarEmulador
from Comparacion import Pixel


AbrirEmulador(1,3)
DetectarEmulador()
Pixel.BorrarCaptura()

while True:
    valor = input('preciona 1 para salir y 2 para tomar captura')
    if valor == "2":
        Pixel.PantallasoEmulador()
    if valor == '1':
        break