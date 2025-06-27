from domain.dataset import Dataset
import pandas as pd

class DatasetParquet(Dataset):
    def __init__(self, fuente):
        super().__init__(fuente)

    def cargar_datos(self):
        print(f'Cargando datos desde .parquet...')
        try:
            df = pd.read_parquet(self.fuente)
            self.datos = df
            print("Parquet cargado")

            if self.validar_datos():
                print("Datos parquet validados")
                self.transformar_datos()
        
        except Exception as e:
            return(f"Error cargando parquet: {e}")
        
    def transformar_datos(self):
        if self.datos is not None:
            self.__datos.columns = (self.datos.columns.str.strip().str.lower().str.replace(" ", "_"))
            self.__datos = self.datos.drop_duplicates().copy()
            for col in self.datos.select_dtypes(include="object").columns:
                self.__datos[col] = self.datos[col].astype(str).str.strip()
                        
            print("Transformaciones aplicadas")
        else: 
            print("No hay datos para transformar")