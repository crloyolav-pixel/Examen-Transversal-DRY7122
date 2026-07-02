#!/usr/bin/env python3
"""
Script para determinar si un número de AS BGP es público o privado
Integrantes: Alonzo-Uzieda, Cristian-Loyola
"""

def verificar_as(numero):
    """
    Verifica si un número de AS es público o privado
    AS Privados: 64512 - 65535
    AS Públicos: 1 - 64511
    """
    if 64512 <= numero <= 65535:
        return "PRIVADO (rango 64512-65535)"
    elif 1 <= numero <= 64511:
        return "PÚBLICO (rango 1-64511)"
    else:
        return "INVÁLIDO (debe estar entre 1 y 65535)"

def mostrar_info():
    """Muestra información sobre rangos de AS"""
    print("\n=== INFORMACIÓN DE AS BGP ===")
    print("AS PÚBLICOS: 1 - 64511")
    print("AS PRIVADOS: 64512 - 65535")
    print("=" * 40)

if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("VERIFICADOR DE AS BGP - DRY7122")
    print("Integrantes: Alonzo-Uzieda, Cristian-Loyola")
    print("=" * 50)
    
    mostrar_info()
    
    while True:
        try:
            entrada = input("\nIngrese número de AS (o 's' para salir): ")
            if entrada.lower() == 's':
                print("¡Hasta luego!")
                break
            as_num = int(entrada)
            resultado = verificar_as(as_num)
            print(f"▶ AS {as_num} es {resultado}")
        except ValueError:
            print("❌ Error: Ingrese un número válido")

