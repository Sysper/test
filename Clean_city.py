import pandas as pd

def clean_columna_city(dataframe):
   
    dataframe['City'].fillna('sin dato', inplace=True)

    dataframe['City'] = dataframe['City'].str.replace('[^a-zA-Z\s]', '', regex=True)
    dataframe['City'] = dataframe['City'].str.replace('\s+', ' ', regex=True)

    
    dataframe['City'] = dataframe['City'].str.title()

ruta = r'C:\Users\Sysper\Prueba tecnica\Employee.csv'
df = pd.read_csv(ruta)

clean_columna_city(df)

print(df.head(15))

ruta_csv_limpiado = r'C:\Users\Sysper\Prueba tecnica\Employee_limpiado.csv'
df.to_csv(ruta_csv_limpiado, index=False)

print("El conjunto de datos con la columna 'City' limpia ha sido exportado a CSV.")
