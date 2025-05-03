import pandas as pd

hospitales = pd.read_csv('/workspaces/estructura-datos/excel/hospital.csv')
print(hospitales.head())
print(hospitales.dtypes)
hospitales['AÑO'] = hospitales['AÑO'].str.replace(',', '',)
print(hospitales.head())
print(hospitales.dtypes)
hospitales['AÑO'] = hospitales['AÑO'].astype(int)
print(hospitales.head())
print(hospitales.dtypes)