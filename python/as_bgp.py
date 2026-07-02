#!/usr/bin/env python3
# Script para determinar si un numero de AS BGP es publico o privado

def verificar_as(numero):
    if 64512 <= numero <= 65535:
        return "PRIVADO (rango 64512-65535)"
    elif 1 <= numero <= 64511:
        return "PUBLICO (rango 1-64511)"
    else:
        return "INVALIDO (debe estar entre 1 y 65535)"

def mostrar_info():
    print("\n=== INFORMACION DE AS BGP ===")
    print("AS PUBLICOS: 1 - 64511")
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
            entrada = input("\nIngrese numero de AS (o 's' para salir): ")
            if entrada.lower() == 's':
                print("Hasta luego!")
                break
            as_num = int(entrada)
            resultado = verificar_as(as_num)
            print(f"AS {as_num} es {resultado}")
        except ValueError:
            print("Error: Ingrese un numero valido")