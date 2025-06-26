from domain.dataset import Dataset
import pandas as pd

class DatasetJSON(Dataset):
    def __init__(self, fuente):
        super().__init__(fuente)

    def cargar_datos(self):
        try:
            df = pd.read_json(self.fuente)
            self.datos = df
            print("JSON cargado")

            if self.validar_datos():
                print("Datos JSON validados")
                self.transformar_datos()
        
        except Exception as e:
            return(f"Error cargando JSON: {e}")