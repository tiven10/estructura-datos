import pandas as pd

def cargar_datos():
    try:
        df = pd.read_csv(
            "/workspaces/estructura-datos/excel/directorio.csv",
            encoding="utf-8-sig",
            sep=",",
            on_bad_lines="skip",
            low_memory=False
        )
    except FileNotFoundError:
        print("Error: El archivo CSV no fue encontrado. Usando datos de ejemplo.")
        df = pd.DataFrame({
            "Número NIT": [123456789, 987654321],
            "Razón Social Organización": ["Hospital A", "Hospital B"],
            "Nombre Sede": ["Sede A", "Sede B"],
            "Nombre Municipio": ["Municipio A", "Municipio B"]
        })
    except pd.errors.ParserError as e:
        print(f"Error al analizar el archivo CSV: {e}")
        exit()


    df.columns = df.columns.str.strip()
    df.rename(columns={
        "Cod. Aseguradora": "Número NIT",
        "NIT": "Número NIT",
        "Razón Social Organización": "Razón Social Organización",
        "Nombre Sede": "Nombre Sede",
        "Nombre Municipio": "Nombre Municipio"
    }, inplace=True)

    if "Número NIT" not in df.columns:
        print("Error: La columna 'Número NIT' no existe en el archivo CSV.")
        exit()

    df["Número NIT"] = (
        df["Número NIT"]
        .astype(str)
        .str.replace(",", "", regex=False)
        .str.replace('"', "", regex=False)
        .str.strip()
    )
    df = df[df["Número NIT"].str.isnumeric()]
    df["Número NIT"] = df["Número NIT"].astype(int)

    return df

class NodoHospital:

    def __init__(self, nit, razon_social, sede, municipio):
        self.nit = nit
        self.razon_social = razon_social
        self.sede = sede
        self.municipio = municipio
        self.izquierda = None
        self.derecha = None

class ArbolHospitales:
    def __init__(self):
        self.raiz = None

    def insertar(self, nodo, nit, razon_social, sede, municipio):

        if nodo is None:
            return NodoHospital(nit, razon_social, sede, municipio)
        if nit < nodo.nit:
            nodo.izquierda = self.insertar(nodo.izquierda, nit, razon_social, sede, municipio)
        else:
            nodo.derecha = self.insertar(nodo.derecha, nit, razon_social, sede, municipio)
        return nodo

    def recorrido_inorder(self, nodo):

        if nodo:
            self.recorrido_inorder(nodo.izquierda)
            print(f"NIT: {nodo.nit} | Organización: {nodo.razon_social} | "
                  f"Sede: {nodo.sede} | Municipio: {nodo.municipio}")
            self.recorrido_inorder(nodo.derecha)

    def buscar(self, nodo, nit_buscado):

        if nodo is None:
            return "Hospital no encontrado"
        if nodo.nit == nit_buscado:
            return (f"Organización: {nodo.razon_social}\n"
                    f"Sede: {nodo.sede}\n"
                    f"Municipio: {nodo.municipio}")
        elif nit_buscado < nodo.nit:
            return self.buscar(nodo.izquierda, nit_buscado)
        else:
            return self.buscar(nodo.derecha, nit_buscado)

def construir_arbol_hospitales(df):
    arbol_hospitales = ArbolHospitales()
    for _, row in df.iterrows():
        if pd.notnull(row["Número NIT"]) and pd.notnull(row["Razón Social Organización"]):
            arbol_hospitales.raiz = arbol_hospitales.insertar(
                arbol_hospitales.raiz,
                row["Número NIT"],
                row["Razón Social Organización"],
                row["Nombre Sede"],
                row["Nombre Municipio"]
            )
    return arbol_hospitales

def buscar_hospital(arbol, nit):
    return arbol.buscar(arbol.raiz, nit)

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, nodo, valor):

        if nodo is None:
            return Nodo(valor)
        if valor < nodo.valor:
            nodo.izquierda = self.insertar(nodo.izquierda, valor)
        else:
            nodo.derecha = self.insertar(nodo.derecha, valor)
        return nodo

    def preorden(self, nodo):

        if nodo:
            print(nodo.valor, end=" ")
            self.preorden(nodo.izquierda)
            self.preorden(nodo.derecha)
        else:
            print()  

valores = [20, 10, 30, 5, 15, 25, 35]
arbol_binario = ArbolBinario()
for valor in valores:
    arbol_binario.raiz = arbol_binario.insertar(arbol_binario.raiz, valor)


print("\nÁrbol en preorden:")
arbol_binario.preorden(arbol_binario.raiz)

class ArbolBinarioBusqueda(ArbolBinario):

    def buscar(self, nodo, valor):

        if nodo is None:
            return False
        if nodo.valor == valor:
            return True
        elif valor < nodo.valor:
            return self.buscar(nodo.izquierda, valor)
        else:
            return self.buscar(nodo.derecha, valor)


arbol_binario_busqueda = ArbolBinarioBusqueda()
for valor in valores:
    arbol_binario_busqueda.raiz = arbol_binario_busqueda.insertar(arbol_binario_busqueda.raiz, valor)

valor_a_buscar = 15
encontrado = arbol_binario_busqueda.buscar(arbol_binario_busqueda.raiz, valor_a_buscar)
print(f"\n¿El valor {valor_a_buscar} está en el árbol?")
print("Sí, el valor está en el árbol." if encontrado else "No, el valor no está en el árbol.")

def main():
    df = cargar_datos()

    arbol_hospitales = construir_arbol_hospitales(df)

    print("\nHospitales ordenados por NIT:")
    arbol_hospitales.recorrido_inorder(arbol_hospitales.raiz)

    nit_a_buscar = 123456789  
    print(f"\nBuscando hospital con NIT {nit_a_buscar}:")
    print(arbol_hospitales.buscar(arbol_hospitales.raiz, nit_a_buscar))

if __name__ == "__main__":
    main()