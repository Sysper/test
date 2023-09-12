import pandas as pd

def primeros_5_registros(ruta):
    try:
        
        df = pd.read_csv(ruta)

        print(df.head(5))
    except FileNotFoundError:
        print("El archivo no se encontró.")


ruta = r'C:\Users\Sysper\Prueba tecnica\Employee.csv'

primeros_5_registros(ruta)

