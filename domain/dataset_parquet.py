from domain.dataset import Dataset
import pandas as pd

class DatasetExcel(Dataset):
    def __init__(self, fuente):
        super().__init__(fuente)

    def cargar_datos(self):
        try:
            df = pd.read_parquet(self.fuente)
            self.datos = df
            print("Parquet cargado")

            if self.validar_datos():
                print("Datos parquet validados")
                self.transformar_datos()
        
        except Exception as e:
            return(f"Error cargando parquet: {e}")