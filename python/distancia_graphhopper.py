#!/usr/bin/env python3
# Script para calcular distancia entre ciudades de Chile y Peru usando API Graphhopper

import requests

# Reemplazar con tu API key de Graphhopper
API_KEY = "72301ab5-4ce6-4c7a-ac0f-6b62b106089c"

CIUDADES_CHILE = {
    "santiago": {"lat": -33.4489, "lon": -70.6693},
    "valparaiso": {"lat": -33.0360, "lon": -71.6296},
    "concepcion": {"lat": -36.8270, "lon": -73.0503},
    "antofagasta": {"lat": -23.6509, "lon": -70.3975},
    "la serena": {"lat": -29.9027, "lon": -71.2520},
    "iquique": {"lat": -20.2141, "lon": -70.1525},
    "puerto montt": {"lat": -41.4694, "lon": -72.9424},
    "temuco": {"lat": -38.7359, "lon": -72.5904},
    "calama": {"lat": -22.4564, "lon": -68.9277},
    "coquimbo": {"lat": -29.9533, "lon": -71.3395}
}

CIUDADES_PERU = {
    "lima": {"lat": -12.0464, "lon": -77.0428},
    "arequipa": {"lat": -16.3988, "lon": -71.5369},
    "trujillo": {"lat": -8.1120, "lon": -79.0288},
    "cuzco": {"lat": -13.5319, "lon": -71.9675},
    "piura": {"lat": -5.1945, "lon": -80.6328},
    "chiclayo": {"lat": -6.7712, "lon": -79.8409},
    "ica": {"lat": -14.0680, "lon": -75.7257},
    "puno": {"lat": -15.8402, "lon": -70.0219},
    "tacna": {"lat": -18.0146, "lon": -70.2486}
}

def obtener_coordenadas(ciudad, pais):
    ciudad = ciudad.lower().strip()
    
    if pais.lower() == "chile":
        if ciudad in CIUDADES_CHILE:
            data = CIUDADES_CHILE[ciudad]
            return data["lat"], data["lon"]
    elif pais.lower() == "peru":
        if ciudad in CIUDADES_PERU:
            data = CIUDADES_PERU[ciudad]
            return data["lat"], data["lon"]
    
    print(f"Ciudad '{ciudad}' no encontrada en {pais}")
    return None, None

def calcular_distancia(origen, destino, transporte="car"):
    url = "https://graphhopper.com/api/1/route"
    
    transportes = {
        "auto": "car",
        "bicicleta": "bike",
        "pie": "foot",
        "moto": "scooter"
    }
    
    vehicle = transportes.get(transporte.lower(), "car")
    
    params = {
        "point": [f"{origen[0]},{origen[1]}", f"{destino[0]},{destino[1]}"],
        "vehicle": vehicle,
        "locale": "es",
        "key": API_KEY
    }
    
    try:
        response = requests.get(url, params=params)
        data = response.json()
        
        if "paths" in data and data["paths"]:
            path = data["paths"][0]
            distancia_metros = path["distance"]
            distancia_km = distancia_metros / 1000
            distancia_millas = distancia_km * 0.621371
            duracion_segundos = path["time"] / 1000
            
            horas = int(duracion_segundos // 3600)
            minutos = int((duracion_segundos % 3600) // 60)
            
            return {
                "km": round(distancia_km, 2),
                "millas": round(distancia_millas, 2),
                "duracion": f"{horas}h {minutos}min",
                "narrativa": "Viaje calculado exitosamente"
            }
        else:
            print("No se pudo calcular la ruta")
            return None
    except Exception as e:
        print(f"Error en API: {e}")
        return None

def mostrar_ciudades(pais):
    if pais.lower() == "chile":
        print("Ciudades en Chile:", ", ".join(sorted(CIUDADES_CHILE.keys())))
    else:
        print("Ciudades en Peru:", ", ".join(sorted(CIUDADES_PERU.keys())))

def main():
    print("\n" + "=" * 60)
    print("CALCULADORA DE DISTANCIA CHILE - PERU")
    print("Integrantes: Alonzo-Uzieda, Cristian-Loyola")
    print("=" * 60)
    
    print("\nOpciones de transporte: auto, bicicleta, pie, moto")
    print("(Presione 's' para salir)")
    
    while True:
        print("\n" + "-" * 40)
        
        origen = input("Ciudad de Origen (en Chile): ").strip()
        if origen.lower() == 's':
            print("Hasta luego!")
            break
        
        if origen.lower() not in CIUDADES_CHILE:
            print(f"Ciudad '{origen}' no encontrada en Chile")
            mostrar_ciudades("chile")
            continue
        
        destino = input("Ciudad de Destino (en Peru): ").strip()
        if destino.lower() == 's':
            print("Hasta luego!")
            break
        
        if destino.lower() not in CIUDADES_PERU:
            print(f"Ciudad '{destino}' no encontrada en Peru")
            mostrar_ciudades("peru")
            continue
        
        transporte = input("Tipo de transporte [auto]: ").strip() or "auto"
        
        lat1, lon1 = obtener_coordenadas(origen, "Chile")
        if lat1 is None:
            continue
            
        lat2, lon2 = obtener_coordenadas(destino, "Peru")
        if lat2 is None:
            continue
        
        print("Calculando distancia...")
        resultado = calcular_distancia((lat1, lon1), (lat2, lon2), transporte)
        
        if resultado:
            print("\n" + "=" * 40)
            print("RESULTADOS")
            print("=" * 40)
            print(f"Origen: {origen.title()}, Chile")
            print(f"Destino: {destino.title()}, Peru")
            print(f"Distancia: {resultado['km']} km ({resultado['millas']} millas)")
            print(f"Duracion estimada: {resultado['duracion']}")
            print(f"Narrativa: {resultado['narrativa']}")
            print(f"Transporte: {transporte}")
            print("=" * 40)
        else:
            print("No se pudo calcular la ruta")

if __name__ == "__main__":
    main()