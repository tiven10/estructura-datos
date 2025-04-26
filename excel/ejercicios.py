import pandas as pd

class Hospital:
    def __init__(self, nombre: str, nit: int, sede: str, municipio: str):
        self.nombre = nombre
        self.nit = nit
        self.sede = sede
        self.municipio = municipio

    def __str__(self):
        return f"Hospital(nombre={self.nombre}, nit={self.nit}, sede={self.sede}, municipio={self.municipio})"

class Nodo: 
    def __init__(self, hospital):
        self.hospital = hospital
        self.izquieda= None
        self.derecha = None

#cargar el archivo csv
hospitales = pd.read_csv('/workspaces/estructura-datos/excel/directorio.csv')
#print(hospitales.head())
hospitales.rename(columns={
    'Razón Social Organización': 'Nombre',
    'Nombre Sede': 'Sede',
    'Nombre Municipio': 'Municipio',
    'Número NIT': 'NIT',

}, inplace=True)


hospitales['NIT'] = hospitales['NIT'].str.replace(',', '',)
hospitales['NIT'] = hospitales['NIT'].astype(int)
print(hospitales.head())
print(hospitales.columns)
print(hospitales['NIT'])

for index, row in hospitales.iterrows():
    hospital = Hospital(
        nombre=row['Nombre'],
        nit=row['NIT'],
        sede=row['Sede'],
        municipio=row['Municipio'],
    )
    print(hospital)
