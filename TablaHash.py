class Contacto:
    def __init__(self, key, telefono):
        self.key = key  # La llave es el nombre de la persona
        self.telefono = telefono  # El teléfono es el valor asociado a la llave

    def __repr__(self):
        return f"Contacto(nombre={self.key}, telefono={self.telefono})"


class TablaHash:
    def __init__(self, tamaño=10):
        self.tamaño = tamaño  # Tamaño de la tabla
        self.tabla = [None] * tamaño  # Inicializamos la tabla con valores nulos

    def funcion_hash(self, key):
        # Calculamos el hash a partir del nombre (key)
        return sum(ord(c) for c in key) % self.tamaño

    def insertar(self, key, telefono):
        # Creamos un objeto Contacto
        contacto = Contacto(key, telefono)
        # Calculamos la posición en la tabla utilizando la función hash
        indice = self.funcion_hash(key)

        # Si la posición está vacía, almacenamos el contacto allí
        if self.tabla[indice] is None:
            self.tabla[indice] = [contacto]
        else:
            # Si ya hay una colisión, agregamos el contacto a la lista
            self.tabla[indice].append(contacto)

    def buscar(self, key):
        # Calculamos el índice de la llave (nombre)
        indice = self.funcion_hash(key)
        
        # Si hay contactos en esa posición, los buscamos
        if self.tabla[indice] is not None:
            for contacto in self.tabla[indice]:
                if contacto.key == key:
                    return contacto.telefono
        return None  # Si no se encuentra, devolvemos None

    def eliminar(self, key):
        # Calculamos el índice de la llave (nombre)
        indice = self.funcion_hash(key)
        
        # Si hay contactos en esa posición, los buscamos
        if self.tabla[indice] is not None:
            for i, contacto in enumerate(self.tabla[indice]):
                if contacto.key == key:
                    del self.tabla[indice][i]
                    return True
        return False  # Si no se encuentra, devolvemos False

    def listar(self):
        # Imprimimos todos los contactos de la tabla
        for i, bucket in enumerate(self.tabla):
            if bucket:
                print(f"Índice {i}:")
                for contacto in bucket:
                    print(f"  {contacto}")
                    
# Ejemplo de uso
tabla = TablaHash(tamaño=5)  # Creamos una tabla de tamaño 5

# Insertamos algunos contactos
tabla.insertar("Juan Pérez", "123-456-7890")
tabla.insertar("Ana Gómez", "987-654-3210")
tabla.insertar("Luis Torres", "555-666-7777")
tabla.insertar("Pedro Sánchez", "222-333-4444")

# Buscar un contacto
print("Buscar 'Ana Gómez':", tabla.buscar("Ana Gómez"))  # Debería devolver el teléfono

# Eliminar un contacto
tabla.eliminar("Juan Pérez")

# Listar todos los contactos
tabla.listar()

# Intentar buscar un contacto eliminado
print("Buscar 'Juan Pérez':", tabla.buscar("Juan Pérez"))  # Debería devolver None




