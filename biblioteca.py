class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.historial_lecturas = []

    def agregar_lectura(self, titulo):
        self.historial_lecturas.append(titulo)

    def ver_historial(self):
        if self.historial_lecturas:
            print(f"Historial de lecturas de {self.nombre}:")
            for libro in self.historial_lecturas:
                print(f"- {libro}")
        else:
            print(f"No hay historial de lecturas disponible para {self.nombre}.")

class Biblioteca:
    def __init__(self):
        self.libros = {}
        self.usuarios = {}

    def agregar_usuario(self, nombre):
        if nombre not in self.usuarios:
            self.usuarios[nombre] = Usuario(nombre)
            print(f"Usuario '{nombre}' registrado con éxito.")
        else:
            print(f"El usuario '{nombre}' ya está registrado.")

    def obtener_usuario(self, nombre):
        return self.usuarios.get(nombre, None)

    def prestar_libro(self, titulo, nombre_usuario):
        usuario = self.obtener_usuario(nombre_usuario)
        if not usuario:
            print(f"El usuario '{nombre_usuario}' no está registrado.")
            return

        if titulo in self.libros and self.libros[titulo]['cantidad'] > 0:
            self.libros[titulo]['cantidad'] -= 1
            usuario.agregar_lectura(titulo)
            print(f"Libro '{titulo}' prestado a {nombre_usuario}.")
        else:
            print(f"El libro '{titulo}' no está disponible.")

    def agregar_libro(self, titulo, autor, cantidad):
        if titulo in self.libros:
            self.libros[titulo]['cantidad'] += cantidad
        else:
            self.libros[titulo] = {'autor': autor, 'cantidad': cantidad}
        print(f"Libro '{titulo}' agregado con éxito.")

    def devolver_libro(self, titulo):
        if titulo in self.libros:
            self.libros[titulo]['cantidad'] += 1
            print(f"Libro '{titulo}' devuelto con éxito.")
        else:
            print(f"El libro '{titulo}' no pertenece a esta biblioteca.")

    def consultar_disponibilidad(self):
        if titulo in self.libros and self.libros[titulo]['cantidad'] > 0:
            print(f"El libro '{titulo}' está disponible.")
            return True
        else:
            print(f"El libro '{titulo}' no está disponible.")
            return False

    def sugerir_libro(self, nombre_usuario):
        usuario = self.obtener_usuario(nombre_usuario)
        if not usuario:
            print(f"El usuario '{nombre_usuario}' no está registrado.")
            return None

        if usuario.historial_lecturas:
            ultimo_libro = usuario.historial_lecturas[-1]
            autor = self.libros[ultimo_libro]['autor']
            sugerencias = [titulo for titulo, datos in self.libros.items() if datos['autor'] == autor and titulo != ultimo_libro]
            if sugerencias:
                print(f"Sugerencia para {nombre_usuario}: {sugerencias[0]}")
                return sugerencias[0]
        print(f"No hay sugerencias disponibles para {nombre_usuario}.")
        return None

    def libros_mas_prestados(self):
        prestados = {}
        for usuario in self.usuarios.values():
            for libro in usuario.historial_lecturas:
                prestados[libro] = prestados.get(libro, 0) + 1
        mas_prestados = sorted(prestados.items(), key=lambda x: x[1], reverse=True)
        print("Libros más prestados:")
        for titulo, cantidad in mas_prestados:
            print(f"{titulo}: {cantidad} veces")
        return mas_prestados

# Ejemplo de uso con menú interactivo

biblioteca = Biblioteca()
while True:
    print("\n--- Menú Biblioteca ---")
    print("1. Agregar libro")
    print("2. Prestar libro")
    print("3. Devolver libro")
    print("4. Consultar disponibilidad")
    print("5. Sugerir libro")
    print("6. Mostrar libros más prestados")
    print("7. Registrar usuario")
    print("8. Ver historial de lecturas de un usuario")
    print("9. Salir")

    opcion = input("Elige una opción: ")
    
    if opcion == "1":
        titulo = input("Introduce el título del libro: ")
        autor = input("Introduce el autor del libro: ")
        while True:
            try:
                cantidad = int(input("Introduce la cantidad de ejemplares: "))
                if cantidad < 0:
                    print("La cantidad no puede ser negativa. Inténtalo de nuevo.")
                    continue
                break
            except ValueError:
                print("Por favor, introduce un número válido.")
        biblioteca.agregar_libro(titulo, autor, cantidad)
    elif opcion == "2":
        titulo = input("Introduce el título del libro que deseas prestar: ")
        usuario = input("Introduce el nombre del usuario: ")
        biblioteca.prestar_libro(titulo, usuario)
    elif opcion == "3":
        titulo = input("Introduce el título del libro que deseas devolver: ")
        biblioteca.devolver_libro(titulo)
    elif opcion == "4":
        titulo = input("Introduce el título del libro que deseas consultar: ")
        biblioteca.consultar_disponibilidad()
    elif opcion == "5":
        usuario = input("Introduce el nombre del usuario: ")
        biblioteca.sugerir_libro(usuario)
    elif opcion == "6":
        biblioteca.libros_mas_prestados()
    elif opcion == "7":
        nombre = input("Introduce el nombre del usuario: ")
        biblioteca.agregar_usuario(nombre)
    elif opcion == "8":
        nombre = input("Introduce el nombre del usuario: ")
        usuario = biblioteca.obtener_usuario(nombre)
        if usuario:
            usuario.ver_historial()
        else:
            print(f"El usuario '{nombre}' no está registrado.")
    elif opcion == "9":
        print("Saliendo del programa. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, elige una opción del menú.")