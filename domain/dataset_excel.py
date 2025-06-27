from domain.dataset import Dataset
import pandas as pd
import os

class DatasetExcel(Dataset):
    def __init__(self, fuente):
        super().__init__(fuente)

    def cargar_datos(self):
        print(f"Intentando leer el archivo: {self.fuente}")
        print(f"Existe: {os.path.exists(self.fuente)}")
        print(f"Ruta absoluta: {os.path.abspath(self.fuente)}")

        print(f'Cargando datos desde .{os.path.splitext(self.fuente)[0].lower()}...') 
        try:
            df = pd.read_excel(self.fuente, na_values=[".."])
            self.datos = df
            print("Excel cargado")

            if self.validar_datos():
                print("Datos excel validados")
                self.transformar_datos()
        
        except Exception as e:
            return(f"Error cargando Excel: {e}")