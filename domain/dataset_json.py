from domain.dataset import Dataset
import pandas as pd
import os

class DatasetJSON(Dataset):
    def __init__(self, fuente):
        super().__init__(fuente)

    def cargar_datos(self):
        print(f"Intentando leer el archivo: {self.fuente}")
        print(f"Existe: {os.path.exists(self.fuente)}")
        print(f"Ruta absoluta: {os.path.abspath(self.fuente)}")

        print(f'Cargando datos JSON...')        
        try:
            df = pd.read_json(self.fuente)
            self.datos = df 
            print("JSON cargado")

            if self.validar_datos():
                print("Datos JSON validados")
                self.transformar_datos()
        
        except Exception as e:
            return(f"Error cargando JSON: {e}")