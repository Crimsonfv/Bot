import subprocess
import os
import time
import Posicion


Emulador = 'E:\\Emulador\\visualboyadvance-m.exe' # cambiar dependiendo del pc
Rom = 'E:\\Emulador\\rom\\PokemonRuby.gba' # cambiar dependiendo del pc

# Verificamos si la ruta donde se encuentra el emulador es correcta o no
def verificarRutas(Emulador, Rom):
    if os.path.exists(Emulador) and os.path.exists(Rom):
        print('Emulador encontrado y Rom encontrada')
    else:
        print('Emulador y Rom no encontrado')

#abrimos el emulador 
def AbrirEmulador(NumeroEmuladores, TiempoEntreEmulador):
    i = 0
    verificarRutas(Emulador, Rom)
    time.sleep(TiempoEntreEmulador)
    print(f'total de emuladores a abrir {NumeroEmuladores}')

    for i in range(NumeroEmuladores):
        i = i + 1
        subprocess.Popen(f'{Emulador} {Rom}')
        time.sleep(1)
        print(f'Numero de emuladores abierto {i}')
        time.sleep(TiempoEntreEmulador)


