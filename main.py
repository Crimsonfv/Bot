from AbrirEmulador import AbrirEmulador
from Posicion import DetectarEmulador
from Comparacion import Pixel


N_Emuladores = int(input('Seleciona el numero de emuladores: '))


AbrirEmulador(N_Emuladores,3)
DetectarEmulador()
Pixel.BorrarCaptura()

while True:
    valor = input('preciona 1 para salir y 2 para tomar captura, 3 obtener pixel: ')
    if valor == "2":
        Pixel.PantallasoEmulador()
    if valor == '1':
        break
