#!/usr/bin/env python3
# Script para gestion de usuarios con contraseñas hasheadas y SQLite

import sqlite3
import hashlib
from flask import Flask, request, render_template_string

DB_NAME = "usuarios.db"
PUERTO = 7500
USUARIOS = ["Alonzo-Uzieda", "Cristian-Loyola"]

def crear_base_datos():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL UNIQUE,
            password_hash TEXT NOT NULL
        )
    ''')
    
    conn.commit()
    conn.close()
    print("Base de datos creada/verificada")

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def agregar_usuario(nombre, password):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    password_hash = hash_password(password)
    
    try:
        cursor.execute(
            "INSERT INTO usuarios (nombre, password_hash) VALUES (?, ?)",
            (nombre, password_hash)
        )
        conn.commit()
        print(f"Usuario '{nombre}' agregado correctamente")
        return True
    except sqlite3.IntegrityError:
        print(f"Usuario '{nombre}' ya existe")
        return False
    finally:
        conn.close()

def verificar_usuario(nombre, password):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    password_hash = hash_password(password)
    
    cursor.execute(
        "SELECT * FROM usuarios WHERE nombre = ? AND password_hash = ?",
        (nombre, password_hash)
    )
    
    resultado = cursor.fetchone()
    conn.close()
    return resultado is not None

def listar_usuarios():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute("SELECT id, nombre, password_hash FROM usuarios")
    usuarios = cursor.fetchall()
    
    conn.close()
    return usuarios

def inicializar_usuarios():
    crear_base_datos()
    
    passwords = {
        "Alonzo-Uzieda": "alonzo123",
        "Cristian-Loyola": "cristian456"
    }
    
    for nombre in USUARIOS:
        password = passwords.get(nombre, "password123")
        agregar_usuario(nombre, password)
    
    print("\nUsuarios cargados:")
    for usuario in listar_usuarios():
        print(f"   ID: {usuario[0]}, Nombre: {usuario[1]}, Hash: {usuario[2][:16]}...")

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Gestion de Usuarios - DRY7122</title>
    <style>
        body { font-family: Arial; margin: 40px; background: #f0f0f0; }
        .container { max-width: 600px; margin: auto; background: white; padding: 20px; border-radius: 10px; }
        h1 { color: #2c3e50; }
        .user { background: #ecf0f1; padding: 10px; margin: 10px 0; border-radius: 5px; }
        .hash { font-family: monospace; font-size: 12px; color: #7f8c8d; }
        .success { color: #27ae60; }
        .error { color: #e74c3c; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Gestion de Usuarios - DRY7122</h1>
        <p>Integrantes: Alonzo-Uzieda, Cristian-Loyola</p>
        <hr>
        <h2>Usuarios Registrados</h2>
        {% if usuarios %}
            {% for usuario in usuarios %}
            <div class="user">
                <strong>{{ usuario[1] }}</strong><br>
                <span class="hash">Hash: {{ usuario[2] }}</span>
            </div>
            {% endfor %}
        {% else %}
            <p>No hay usuarios registrados</p>
        {% endif %}
        <hr>
        <h2>Verificar Usuario</h2>
        <form method="POST">
            <input type="text" name="nombre" placeholder="Nombre de usuario" required>
            <input type="password" name="password" placeholder="Contrasena" required>
            <button type="submit">Verificar</button>
        </form>
        {% if resultado is not none %}
            <p class="{% if resultado %}success{% else %}error{% endif %}">
                {% if resultado %}Usuario verificado correctamente{% else %}Credenciales incorrectas{% endif %}
            </p>
        {% endif %}
        <hr>
        <p><small>Examen Transversal - DRY7122</small></p>
    </div>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        password = request.form.get('password')
        if nombre and password:
            resultado = verificar_usuario(nombre, password)
    
    usuarios = listar_usuarios()
    return render_template_string(HTML_TEMPLATE, usuarios=usuarios, resultado=resultado)

def iniciar_servidor():
    print(f"Iniciando servidor web en puerto {PUERTO}")
    print(f"Accede a: http://localhost:{PUERTO}")
    print("Presiona Ctrl+C para detener")
    app.run(host='0.0.0.0', port=PUERTO, debug=False)

def main():
    print("\n" + "=" * 60)
    print("GESTION DE USUARIOS - DRY7122")
    print("Integrantes: Alonzo-Uzieda, Cristian-Loyola")
    print("=" * 60)
    
    inicializar_usuarios()
    
    print("\n" + "=" * 60)
    print("Usuarios en base de datos:")
    print("=" * 60)
    for usuario in listar_usuarios():
        print(f"ID: {usuario[0]} | Nombre: {usuario[1]} | Hash: {usuario[2]}")
    
    print("\n" + "=" * 60)
    print("Credenciales de prueba:")
    print("   Alonzo-Uzieda / alonzo123")
    print("   Cristian-Loyola / cristian456")
    print("=" * 60)
    
    iniciar_servidor()

if __name__ == "__main__":
    main()