# Escritura en el archivo de texto
# Creamos o abrimos un archivo llamado 'my_notes.txt' en modo escritura ('w')
with open('my_notes.txt', 'w') as archivo:
    # Escribimos tres líneas de notas personales en el archivo
    archivo.write("Primera nota: Recordar estudiar para el examen de programación.\n")
    archivo.write("Segunda nota: Comprar materiales para el proyecto de Realidad Nacional.\n")
    archivo.write("Tercera nota: Leer el capítulo 4 del libro de Física.\n")

# Lectura del archivo de texto
# Abrimos el archivo en modo lectura ('r')
with open('my_notes.txt', 'r') as archivo:
    # Leemos el contenido línea por línea usando readline()
    print("Contenido del archivo my_notes.txt:\n")
    linea = archivo.readline()
    while linea:
        # Mostramos cada línea en la consola
        print(linea.strip())  # .strip() elimina saltos de línea adicionales
        linea = archivo.readline()

# El archivo se cierra automáticamente al usar 'with', no se necesita cerrar manualmente
