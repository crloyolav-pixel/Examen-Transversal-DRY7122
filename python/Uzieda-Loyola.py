#!/usr/bin/env python3
# Script para mostrar nombres y apellidos de los integrantes del grupo

integrantes = [
    "Alonzo-Uzieda",
    "Cristian-Loyola"
]

print("=== INTEGRANTES DEL GRUPO ===")
print("Examen Transversal - Programación y Redes Virtualizadas - DRY7122")
print("-" * 50)
for i, integrante in enumerate(integrantes, 1):
    print(f"{i}. {integrante}")
print("-" * 50)
print(f"Total de integrantes: {len(integrantes)}")

# Subir a GitHub
# git add integrantes.py
# git commit -m "Agregar script de integrantes - Alonzo y Loyola"
# git push origin main