import pyautogui
import json
import os
from datetime import datetime

RutaJson = 'C:\\Users\\guill\\WorkSpace\\Bot\\EmuladorPosicion\\posiciones.json' # cambiar dependiendo del pc
RutaCapturas = 'C:\\Users\\guill\\WorkSpace\\Bot\\Capturas\\CapturasEmulador' # cambiar dependiendo del pc

def PantallasoEmulador():
    # Verificar si existe el archivo JSON
    if not os.path.exists(RutaJson):
        print(f'Error: No se encontró el archivo {RutaJson}')
        return
    
    print('JSON encontrado')
    
    try:
        # Leer el archivo JSON
        with open(RutaJson, 'r', encoding='utf-8') as archivo:
            emuladores = json.load(archivo)
        
        print(f'Se encontraron {len(emuladores)} emuladores')
        
        # Crear carpeta para las capturas si no existe
        if not os.path.exists(RutaCapturas):
            os.makedirs(RutaCapturas)
            print(f'Carpeta creada: {RutaCapturas}')
        
        # Tomar captura de cada emulador
        for emulador in emuladores:
            nombre = emulador['nombre']
            x = emulador['x']
            y = emulador['y']
            
            print(f'Tomando captura de {nombre} en posición ({x}, {y})')
            
            # Tomar captura en la posición especificada
            # Puedes ajustar el tamaño (300x300) según tus necesidades
            img = pyautogui.screenshot(region=(x, y, 300, 300))
            
            # Nombre del archivo sin timestamp - solo el nombre del emulador
            nombre_archivo = f'{RutaCapturas}\\{nombre}.png'
            
            # Guardar la imagen
            img.save(nombre_archivo)
            print(f'Captura guardada: {nombre_archivo}')
        
        print('¡Todas las capturas completadas!')
        
    except json.JSONDecodeError:
        print('Error: El archivo JSON no tiene un formato válido')
    except Exception as e:
        print(f'Error inesperado: {e}')

def BorrarCaptura():
    """
    Elimina todas las capturas de la carpeta CapturasEmulador
    """
    if not os.path.exists(RutaCapturas):
        print(f'La carpeta {RutaCapturas} no existe')
        return
    
    try:
        # Obtener todos los archivos en la carpeta
        archivos = os.listdir(RutaCapturas)
        
        # Filtrar solo archivos de imagen
        archivos_imagen = [archivo for archivo in archivos if archivo.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif'))]
        
        if not archivos_imagen:
            print('No hay capturas para borrar')
            return
        
        print(f'Borrando {len(archivos_imagen)} capturas...')
        
        archivos_borrados = 0
        for archivo in archivos_imagen:
            ruta_archivo = os.path.join(RutaCapturas, archivo)
            try:
                os.remove(ruta_archivo)
                print(f'Borrado: {archivo}')
                archivos_borrados += 1
            except Exception as e:
                print(f'Error al borrar {archivo}: {e}')
        
        print(f'¡Se borraron {archivos_borrados} capturas exitosamente!')
            
    except Exception as e:
        print(f'Error al acceder a la carpeta: {e}')