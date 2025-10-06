# ============================================
# Tarea: Trabajo con Archivos de Texto en Python
# Autor: Arturo Chalacan
# Descripción: Este programa crea, escribe y lee un archivo de texto.
# ============================================

# --- Escritura de Archivo de Texto ---
# Se crea (o sobreescribe si ya existe) el archivo llamado "my_notes.txt"
with open("my_notes.txt", "w", encoding="utf-8") as archivo:
    archivo.write("Primera nota: Aprender Python paso a paso.\n")
    archivo.write("Segunda nota: Practicar ejercicios todos los días.\n")
    archivo.write("Tercera nota: Subir mis tareas al repositorio de GitHub.\n")
# El archivo se cierra automáticamente al salir del bloque 'with'

print("✅ Archivo 'my_notes.txt' creado y se han escrito las notas.\n")

# --- Lectura de Archivo de Texto ---
# Se abre el archivo en modo lectura
with open("my_notes.txt", "r", encoding="utf-8") as archivo:
    print("📖 Contenido del archivo línea por línea:\n")
    # Se lee y muestra cada línea usando un bucle
    for linea in archivo:
        print(linea.strip())  # strip() elimina los saltos de línea extra

# No es necesario cerrar el archivo manualmente porque 'with' lo hace automáticamente

print("\n✅ Lectura completada y archivo cerrado correctamente.")
