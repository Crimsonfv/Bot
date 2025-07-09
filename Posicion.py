import pygetwindow
import time
import json
import os

def DetectarEmulador():
    alto = 300
    ancho = 300
    
    # Configuración de la grilla
    emuladores_por_fila = 4  # Puedes cambiar este número según tus necesidades
    separacion_x = 290  # Separación horizontal entre emuladores
    separacion_y = 310  # Separación vertical entre filas
    
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
        print(f"Organizando en grilla de {emuladores_por_fila} emuladores por fila")
        
        # Posicionar cada emulador en grilla
        for i, emulador in enumerate(emuladores):
            # Calcular fila y columna
            fila = i // emuladores_por_fila  # División entera para obtener la fila
            columna = i % emuladores_por_fila  # Módulo para obtener la columna
            
            # Calcular coordenadas X e Y
            x = columna * separacion_x
            y = fila * separacion_y
            
            # Posicionar y redimensionar emulador
            emulador.moveTo(x, y)
            emulador.resizeTo(alto, ancho)
            
            print(f"Emulador {i+1} posicionado en fila {fila+1}, columna {columna+1} - Coordenadas: ({x}, {y})")
            print(f"Tamaño del emulador alto: {alto} y de ancho: {ancho}")
            
            # Guardar posición con nombre del emulador
            posiciones.append({
                "nombre": f"emulador{i+1}",
                "x": x, 
                "y": y,
                "fila": fila + 1,
                "columna": columna + 1
            })
            
            # Pequeña pausa entre movimientos
            time.sleep(0.5)
        
        # Mostrar resumen de la organización
        total_filas = (len(emuladores) - 1) // emuladores_por_fila + 1
        print(f"\nResumen: {len(emuladores)} emuladores organizados en {total_filas} filas")
        
        # Guardar posiciones en JSON
        with open("EmuladorPosicion/posiciones.json", "w") as f:
            json.dump(posiciones, f, indent=2)
        print(f"Posiciones guardadas en EmuladorPosicion/posiciones.json")
            
    except IndexError:
        print("Error: No se pudieron encontrar las ventanas de los emuladores")
    except Exception as e:
        print(f"Error al posicionar emuladores: {e}")