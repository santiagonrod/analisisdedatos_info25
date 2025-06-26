from domain.dataset import Dataset
import pandas as pd
import os
import chardet

class DatasetCSV(Dataset):
    def __init__(self, fuente):
        super().__init__(fuente)

    def cargar_datos(self):
        print(f"Intentando leer el archivo: {self.fuente}")
        print(f"Existe: {os.path.exists(self.fuente)}")
        print(f"Ruta absoluta: {os.path.abspath(self.fuente)}")

        print(f'Cargando datos csv...')        
        try:
            with open(self.fuente, 'rb') as f:
                result = chardet.detect(f.read())
                print("Encoding detectado:", result['encoding'])
            df = pd.read_csv(self.fuente, sep=",", encoding=result['encoding'])
            self.datos = df 
            print("CSV cargado")

            if self.validar_datos():
                print("Datos CSV validados")
                self.transformar_datos()
        
        except Exception as e:
            print(f"Error cargando CSV: {e}")
            raise