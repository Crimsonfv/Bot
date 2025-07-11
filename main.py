from AbrirEmulador import AbrirEmulador
from Posicion import DetectarEmulador
from Comparacion import Pixel
from Controles.Control import Press_A,Press_B,Press_Start,Press_Izquierda,SoftReset
from ObtenerColor import *
import os
import time

N_Emuladores = 0  # Variable global
contador_reseteos = 0  # Contador de reseteos
tiempo_inicio = 0  # Tiempo de inicio de la búsqueda

def formatear_tiempo(segundos):
    """Convierte segundos a formato legible (horas:minutos:segundos)"""
    horas = int(segundos // 3600)
    minutos = int((segundos % 3600) // 60)
    segs = int(segundos % 60)
    
    if horas > 0:
        return f"{horas:02d}:{minutos:02d}:{segs:02d}"
    else:
        return f"{minutos:02d}:{segs:02d}"

def obtener_tiempo_transcurrido():
    """Obtiene el tiempo transcurrido desde el inicio de la búsqueda"""
    return time.time() - tiempo_inicio

while True:
    valor = input('escoge una opcion del 1 - 2 - 3: ')
    print('selecciona una opcion')
    print('')
    
    if valor == '1':
        N_Emuladores = int(input('selecciona la cantidad de emuladores: '))
        print('')
        AbrirEmulador(N_Emuladores, 3)
        DetectarEmulador()
        os.system('cls')
        
    elif valor == '2':
        if N_Emuladores == 0:
            print("Primero debes abrir los emuladores (opción 1)")
            continue
            
        print('Se inicia la busqueda del pokemon seleccionado')
        print('')
        
        # Reiniciar contador de reseteos y tiempo al iniciar nueva búsqueda
        contador_reseteos = 0
        tiempo_inicio = time.time()  # Registrar tiempo de inicio
        
        # BUCLE PRINCIPAL - Se reinicia cuando se hace SoftReset
        while True:
            os.system('cls')  # Limpiar pantalla al inicio de cada ciclo
            tiempo_transcurrido = obtener_tiempo_transcurrido()
            
            print("\n" + "="*70)
            print("INICIANDO NUEVA BÚSQUEDA DE POKEMON SHINY")
            if contador_reseteos > 0:
                print(f"RESETEOS REALIZADOS: {contador_reseteos}")
                print(f"TIEMPO TRANSCURRIDO: {formatear_tiempo(tiempo_transcurrido)}")
            print("="*70)
            
            # FASE 1: Navegar desde título hacia partida guardada
            print("\nFASE 1: Navegando desde título hacia partida guardada...")
            while True:
                colores_partida = PartidaGuardada()
                color_partida_objetivo = (248, 248, 248)
                coincidencias_partida = colores_partida.count(color_partida_objetivo)
                
                print(f"Emuladores en partida guardada: {coincidencias_partida}/{N_Emuladores}")
                
                if coincidencias_partida == N_Emuladores:
                    print("¡Todos los emuladores están en partida guardada!")
                    Press_A()  # Presionar A para continuar
                    time.sleep(0.05) 
                    break
                else:
                    print("Navegando desde título...")
                    Press_Start()  # Presionar B para ir de título a partida guardada
                    time.sleep(0.05)    # Esperar un poco más para que cargue
            
            # FASE 2: Navegar hasta la elección de pokemon
            print("\nFASE 2: Navegando a la elección de pokemon...")
            while True:
                colores_eleccion = EleccionPokemonTreecko()
                color_eleccion_objetivo = (216, 168, 88)
                coincidencias_eleccion = colores_eleccion.count(color_eleccion_objetivo)
                
                print(f"En pantalla de elección: {coincidencias_eleccion}/{N_Emuladores}")
                
                if coincidencias_eleccion == N_Emuladores:
                    print("¡Todos están en la pantalla de elección!")
                    Press_Izquierda()
                    time.sleep(0.05) 
                    break
                else:
                    print("Navegando...")
                    Press_A()
                    time.sleep(0.05)

            # FASE 3: Verificar BatallaPregunta  
            print("\nFASE 3: Verificando BatallaPregunta...")
            while True:
                colores_pregunta = BatallaPregunta()
                color_pregunta_objetivo = (104, 160, 160)
                coincidencias_pregunta = colores_pregunta.count(color_pregunta_objetivo)
                
                print(f"En BatallaPregunta: {coincidencias_pregunta}/{N_Emuladores}")
                
                if coincidencias_pregunta == N_Emuladores:
                    print("¡Todos están en BatallaPregunta!")
                    break
                else:
                    print("Esperando BatallaPregunta...")
                    Press_A()
                    time.sleep(0.05)

            # FASE 4: Verificar BatallaMenu (si la necesitas, descomenta y completa)
            # print("\nFASE 4: Verificando BatallaMenu...")
            # while True:
            #     # Aquí va tu código para BatallaMenu
            #     break
            
            # FASE 5: Verificar BatallaInfo
            print("\nFASE 5: Verificando BatallaInfo...")
            while True:
                colores_info = BatallaInfo()
                color_info_objetivo = (248, 248, 216)
                coincidencias_info = colores_info.count(color_info_objetivo)
                
                print(f"En BatallaInfo: {coincidencias_info}/{N_Emuladores}")
                
                if coincidencias_info == N_Emuladores:
                    print("¡Todos están en BatallaInfo!")
                    break
                else:
                    print("Esperando BatallaInfo...")
                    Press_A()
                    time.sleep(0.05)
            
            # FASE 6: VERIFICAR SI HAY POKEMON SHINY
            tiempo_actual = obtener_tiempo_transcurrido()
            print(f"\nFASE 6: ¡VERIFICANDO POKEMON SHINY! (Reset #{contador_reseteos + 1})")
            print(f"Tiempo actual: {formatear_tiempo(tiempo_actual)}")
            print("="*50)
            
            colores_batalla = CalcularPixelTreecko()
            color_normal_treecko = (152, 208, 72)
            coincidencias_normal = colores_batalla.count(color_normal_treecko)
            
            print(f"Pokemon normales: {coincidencias_normal}/{N_Emuladores}")
            
            if coincidencias_normal < N_Emuladores:
                tiempo_total = obtener_tiempo_transcurrido()
                emuladores_shiny = N_Emuladores - coincidencias_normal
                
                print("\n" + "🌟"*25)
                print(f"¡¡¡POKEMON SHINY ENCONTRADO!!! En {emuladores_shiny} emulador(es)")
                print(f"TOTAL DE RESETEOS REALIZADOS: {contador_reseteos}")
                print(f"TIEMPO TOTAL TRANSCURRIDO: {formatear_tiempo(tiempo_total)}")
                if contador_reseteos > 0:
                    tiempo_promedio = tiempo_total / contador_reseteos
                    print(f"TIEMPO PROMEDIO POR RESET: {formatear_tiempo(tiempo_promedio)}")
                print("🌟"*25)
                
                # Mostrar qué emuladores tienen shiny
                for i, color in enumerate(colores_batalla):
                    if color != color_normal_treecko:
                        print(f"SHINY detectado en emulador {i+1} - Color: {color}")
                
                # SHINY ENCONTRADO - SALIR DEL BUCLE PRINCIPAL
                input("\nPresiona ENTER para continuar...")
                break  # Sale del bucle principal, termina la búsqueda
            else:
                contador_reseteos += 1  # Incrementar contador
                tiempo_actual = obtener_tiempo_transcurrido()
                
                print("Todos son pokemon normales, haciendo SoftReset...")
                print(f"RESET #{contador_reseteos} - Tiempo: {formatear_tiempo(tiempo_actual)}")
                print("Reiniciando desde FASE 1 en 3 segundos...")
                SoftReset()
                time.sleep(1.5)  # Aumenté a 3 segundos para dar tiempo a leer
                # El continue hace que vuelva al inicio del bucle principal (FASE 1)
                continue
                
    elif valor == '3':
        os.system('cls')
        break