import pyautogui
import json
import os

RutaPantalla = 'C:\\Users\\guill\\WorkSpace\\Bot\\Capturas\\Ecenas\\PantallaDeTitulo.png'
RutaSeleccion = 'C:\\Users\\guill\\WorkSpace\\Bot\\Capturas\\Ecenas\\SeleccionarPokemon.png'
RutaVerPokemon = 'C:\\Users\\guill\\WorkSpace\\Bot\\Capturas\\Ecenas\\PantallaVerPokemon.png'
RutaEnBatalla = 'C:\\Users\\guill\\WorkSpace\\Bot\\Capturas\\Ecenas\\PokemonBatalla.png'
RutaPokemonEspecifico = 'C:\\Users\\guill\\WorkSpace\\Bot\\Capturas\\Pokemon\\PokemonSeleccionado.png'

def _cargar_emuladores():
    """Función auxiliar para cargar las posiciones de los emuladores"""
    try:
        with open("EmuladorPosicion/posiciones.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print("❌ Error: No se encontró el archivo posiciones.json")
        return []
    except Exception as e:
        print(f"❌ Error al leer JSON: {e}")
        return []

def _buscar_imagen_en_region(ruta_imagen, region, min_confidence=0.5):
    """Función auxiliar para buscar una imagen en una región específica"""
    confianzas_a_probar = [0.9, 0.8, 0.7, 0.6, 0.5]
    
    for conf in confianzas_a_probar:
        if conf < min_confidence:
            break
            
        try:
            resultado = pyautogui.locateOnScreen(ruta_imagen, confidence=conf, region=region)
            if resultado:
                return resultado, conf
        except:
            continue
    
    return None, None

def BuscarPantallaTitulo(min_confidence=0.7):
    """Busca la pantalla de título en TODOS los emuladores"""
    print("🔍 Buscando Pantalla de Título en todos los emuladores...")
    
    emuladores = _cargar_emuladores()
    if not emuladores:
        return []
    
    resultados = []
    ancho = 300
    alto = 300
    
    for emulador in emuladores:
        nombre = emulador["nombre"]
        x = emulador["x"]
        y = emulador["y"]
        region = (x, y, ancho, alto)
        
        print(f"  🎮 Buscando en {nombre}...")
        resultado, confianza = _buscar_imagen_en_region(RutaPantalla, region, min_confidence)
        
        if resultado:
            print(f"  ✅ {nombre}: ¡Pantalla de Título encontrada! (Confianza: {confianza})")
            resultados.append({
                "emulador": nombre,
                "coordenadas": resultado,
                "confianza": confianza,
                "region": region
            })
        else:
            print(f"  ❌ {nombre}: No encontrada")
    
    print(f"📊 Resultado: {len(resultados)}/{len(emuladores)} emuladores con Pantalla de Título")
    return resultados

def BuscarSeleccionPokemon(min_confidence=0.5):
    """Busca la pantalla de selección de Pokemon en TODOS los emuladores"""
    print("🔍 Buscando Selección de Pokemon en todos los emuladores...")
    
    emuladores = _cargar_emuladores()
    if not emuladores:
        return []
    
    resultados = []
    ancho = 300
    alto = 300
    
    for emulador in emuladores:
        nombre = emulador["nombre"]
        x = emulador["x"]
        y = emulador["y"]
        region = (x, y, ancho, alto)
        
        print(f"  🎮 Buscando en {nombre}...")
        resultado, confianza = _buscar_imagen_en_region(RutaSeleccion, region, min_confidence)
        
        if resultado:
            print(f"  ✅ {nombre}: ¡Selección de Pokemon encontrada! (Confianza: {confianza})")
            resultados.append({
                "emulador": nombre,
                "coordenadas": resultado,
                "confianza": confianza,
                "region": region
            })
        else:
            print(f"  ❌ {nombre}: No encontrada")
    
    print(f"📊 Resultado: {len(resultados)}/{len(emuladores)} emuladores con Selección de Pokemon")
    return resultados

def BuscarVerPokemon(min_confidence=0.5):
    """Busca la pantalla de ver Pokemon en TODOS los emuladores"""
    print("🔍 Buscando Pantalla Ver Pokemon en todos los emuladores...")
    
    emuladores = _cargar_emuladores()
    if not emuladores:
        return []
    
    resultados = []
    ancho = 300
    alto = 300
    
    for emulador in emuladores:
        nombre = emulador["nombre"]
        x = emulador["x"]
        y = emulador["y"]
        region = (x, y, ancho, alto)
        
        print(f"  🎮 Buscando en {nombre}...")
        resultado, confianza = _buscar_imagen_en_region(RutaVerPokemon, region, min_confidence)
        
        if resultado:
            print(f"  ✅ {nombre}: ¡Pantalla Ver Pokemon encontrada! (Confianza: {confianza})")
            resultados.append({
                "emulador": nombre,
                "coordenadas": resultado,
                "confianza": confianza,
                "region": region
            })
        else:
            print(f"  ❌ {nombre}: No encontrada")
    
    print(f"📊 Resultado: {len(resultados)}/{len(emuladores)} emuladores con Pantalla Ver Pokemon")
    return resultados

def BuscarEnBatalla(min_confidence=0.5):
    """Busca la pantalla de batalla en TODOS los emuladores"""
    print("🔍 Buscando Pokemon en Batalla en todos los emuladores...")
    
    emuladores = _cargar_emuladores()
    if not emuladores:
        return []
    
    resultados = []
    ancho = 300
    alto = 300
    
    for emulador in emuladores:
        nombre = emulador["nombre"]
        x = emulador["x"]
        y = emulador["y"]
        region = (x, y, ancho, alto)
        
        print(f"  🎮 Buscando en {nombre}...")
        resultado, confianza = _buscar_imagen_en_region(RutaEnBatalla, region, min_confidence)
        
        if resultado:
            print(f"  ✅ {nombre}: ¡Pokemon en Batalla encontrado! (Confianza: {confianza})")
            resultados.append({
                "emulador": nombre,
                "coordenadas": resultado,
                "confianza": confianza,
                "region": region
            })
        else:
            print(f"  ❌ {nombre}: No encontrado")
    
    print(f"📊 Resultado: {len(resultados)}/{len(emuladores)} emuladores con Pokemon en Batalla")
    return resultados

def BuscarPokemonEspecifico(min_confidence=0.5):
    """Busca un Pokemon específico en TODOS los emuladores"""
    print("🔍 Buscando Pokemon Específico en todos los emuladores...")
    
    emuladores = _cargar_emuladores()
    if not emuladores:
        return []
    
    resultados = []
    ancho = 300
    alto = 300
    
    for emulador in emuladores:
        nombre = emulador["nombre"]
        x = emulador["x"]
        y = emulador["y"]
        region = (x, y, ancho, alto)
        
        print(f"  🎮 Buscando en {nombre}...")
        resultado, confianza = _buscar_imagen_en_region(RutaPokemonEspecifico, region, min_confidence)
        
        if resultado:
            print(f"  ✅ {nombre}: ¡Pokemon Específico encontrado! (Confianza: {confianza})")
            resultados.append({
                "emulador": nombre,
                "coordenadas": resultado,
                "confianza": confianza,
                "region": region
            })
        else:
            print(f"  ❌ {nombre}: No encontrado")
    
    print(f"📊 Resultado: {len(resultados)}/{len(emuladores)} emuladores con Pokemon Específico")
    return resultados

def BuscarTodasLasEscenas():
    """Busca todas las escenas posibles en todos los emuladores y devuelve un resumen completo"""
    print("=" * 80)
    print("🎮 DETECTANDO TODAS LAS ESCENAS EN TODOS LOS EMULADORES")
    print("=" * 80)
    
    emuladores = _cargar_emuladores()
    if not emuladores:
        return {}
    
    # Definir todas las funciones de búsqueda
    funciones_busqueda = [
        ("Pantalla de Título", BuscarPantallaTitulo),
        ("Selección de Pokemon", BuscarSeleccionPokemon),
        ("Ver Pokemon", BuscarVerPokemon),
        ("En Batalla", BuscarEnBatalla),
        ("Pokemon Específico", BuscarPokemonEspecifico)
    ]
    
    resumen_completo = {}
    
    for nombre_escena, funcion in funciones_busqueda:
        print(f"\n{'='*20} {nombre_escena.upper()} {'='*20}")
        resultados = funcion()
        resumen_completo[nombre_escena] = resultados
    
    # Mostrar resumen final
    print("\n" + "=" * 80)
    print("📊 RESUMEN FINAL DE TODAS LAS ESCENAS")
    print("=" * 80)
    
    for escena, resultados in resumen_completo.items():
        if resultados:
            print(f"✅ {escena}: {len(resultados)} emulador(es) detectado(s)")
            for resultado in resultados:
                print(f"   - {resultado['emulador']} (Confianza: {resultado['confianza']})")
        else:
            print(f"❌ {escena}: No detectada en ningún emulador")
    
    return resumen_completo

# ===== CÓDIGO PRINCIPAL =====
if __name__ == "__main__":
    print("🎮 SISTEMA DE DETECCIÓN DE ESCENAS POKEMON")
    print("=" * 60)
    
    while True:
        print("\n📋 OPCIONES DISPONIBLES:")
        print("1️⃣  Buscar Pantalla de Título")
        print("2️⃣  Buscar Selección de Pokemon")
        print("3️⃣  Buscar Ver Pokemon")
        print("4️⃣  Buscar En Batalla")
        print("5️⃣  Buscar Pokemon Específico")
        print("6️⃣  Buscar TODAS las escenas")
        print("7️⃣  Salir")
        
        opcion = input("\n🎯 Selecciona una opción (1-7): ").strip()
        
        if opcion == "1":
            resultados = BuscarPantallaTitulo()
            
        elif opcion == "2":
            resultados = BuscarSeleccionPokemon()
            
        elif opcion == "3":
            resultados = BuscarVerPokemon()
            
        elif opcion == "4":
            resultados = BuscarEnBatalla()
            
        elif opcion == "5":
            resultados = BuscarPokemonEspecifico()
            
        elif opcion == "6":
            resumen = BuscarTodasLasEscenas()
            
        elif opcion == "7":
            print("👋 ¡Hasta luego!")
            break
            
        else:
            print("❌ Opción no válida. Intenta de nuevo.")
        
        input("\n⏸️  Presiona Enter para continuar...")