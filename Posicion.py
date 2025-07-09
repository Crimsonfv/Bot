import pygetwindow
import time
import json
import os

def DetectarEmulador():
    alto = 300
    ancho = 300
    
    # Crear carpeta si no existe
    if not os.path.exists("EmuladorPosicion"):
        os.makedirs("EmuladorPosicion")
    
    posiciones = []  # Lista para guardar las posiciones
    
    try:
        # Buscar todas las ventanas con el título 'PokemonRuby'
        emuladores = pygetwindow.getWindowsWithTitle('PokemonRuby')
        
        if not emuladores:
            print("No se encontraron ventanas de emuladores")
            return
        
        print(f"Se encontraron {len(emuladores)} emuladores")
        
        # Posicionar cada emulador
        for i, emulador in enumerate(emuladores):
            # Posicionar emuladores lado a lado
            x = i * 290  # 400 píxeles de separación horizontal
            y = 0
            
            emulador.moveTo(x, y)
            # rescalar emuladores
            emulador.resizeTo(alto,ancho)
            print(f"Emulador {i+1} posicionado en ({x}, {y})")
            print(f"Tamano del emulador alto: {alto} y de ancho: {ancho}")
            
            # Guardar posición con nombre del emulador
            posiciones.append({
                "nombre": f"emulador{i+1}",
                "x": x, 
                "y": y
            })
            
            # Pequeña pausa entre movimientos
            time.sleep(0.5)
        
        # Guardar posiciones en JSON
        with open("EmuladorPosicion/posiciones.json", "w") as f:
            json.dump(posiciones, f)
        print(f"Posiciones guardadas en EmuladorPosicion/posiciones.json")
            
    except IndexError:
        print("Error: No se pudieron encontrar las ventanas de los emuladores")
    except Exception as e:
        print(f"Error al posicionar emuladores: {e}")