import json
import pyautogui

def obtener_coordenada_absoluta(nombre_emulador, offset_x, offset_y):
    """
    Calcula la coordenada absoluta de un píxel específico dentro de un emulador
    
    Args:
        nombre_emulador (str): Nombre del emulador (ej: "emulador1", "emulador2")
        offset_x (int): Coordenada X relativa dentro del emulador
        offset_y (int): Coordenada Y relativa dentro del emulador
    
    Returns:
        tuple: (x_absoluta, y_absoluta) coordenadas en pantalla
    """
    try:
        # Leer archivo JSON con posiciones
        with open("EmuladorPosicion/posiciones.json", "r") as f:
            emuladores = json.load(f)
        
        # Buscar el emulador específico
        for emulador in emuladores:
            if emulador["nombre"] == nombre_emulador:
                # Calcular coordenadas absolutas
                x_absoluta = emulador["x"] + offset_x
                y_absoluta = emulador["y"] + offset_y
                
                return x_absoluta, y_absoluta
        
        print(f"Error: No se encontró el emulador '{nombre_emulador}'")
        return None, None
        
    except FileNotFoundError:
        print("Error: No se encontró el archivo posiciones.json")
        return None, None
    except Exception as e:
        print(f"Error: {e}")
        return None, None

def obtener_coordenada_y_color(nombre_emulador, offset_x, offset_y):
    """
    Obtiene las coordenadas absolutas Y el color del píxel en esas coordenadas
    
    Args:
        nombre_emulador (str): Nombre del emulador
        offset_x (int): Coordenada X relativa dentro del emulador
        offset_y (int): Coordenada Y relativa dentro del emulador
    
    Returns:
        tuple: (x_absoluta, y_absoluta, color_rgb)
    """
    # Obtener coordenadas
    x, y = obtener_coordenada_absoluta(nombre_emulador, offset_x, offset_y)
    
    if x is not None and y is not None:
        # Obtener color del píxel
        color = pyautogui.pixel(x, y)
        return x, y, color
    
    return None, None, None

# Ejemplo de uso:
if __name__ == "__main__":
    # Ejemplo 1: Solo obtener coordenadas
    x, y = obtener_coordenada_absoluta("emulador1", 50, 100)
    print(f"Coordenadas: ({x}, {y})")
    
    # Obtener color por separado
    if x is not None and y is not None:
        color = pyautogui.pixel(x, y)
        print(f"Color RGB: {color}")
    
    print("-" * 40)
    
    # Ejemplo 2: Obtener coordenadas Y color de una vez
    x, y, color = obtener_coordenada_y_color("emulador1", 50, 100)
    if x is not None:
        print(f"Coordenadas: ({x}, {y})")
        print(f"Color RGB: {color}")
        print(f"Rojo: {color[0]}, Verde: {color[1]}, Azul: {color[2]}")
    
    print("-" * 40)
    
    # Ejemplo 3: Comparar color para detectar pantalla
    x, y, color_actual = obtener_coordenada_y_color("emulador1", 50, 100)
    
    # Color esperado para pantalla de selección (ejemplo)
    color_pantalla_seleccion = (120, 150, 200)
    
    if color_actual == color_pantalla_seleccion:
        print("¡Estamos en la pantalla de selección!")
    else:
        print("No estamos en la pantalla correcta")
        print(f"Color esperado: {color_pantalla_seleccion}")
        print(f"Color actual: {color_actual}")


obtener_coordenada_absoluta()