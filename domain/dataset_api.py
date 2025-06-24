import requests
import pandas as pd
from domain.dataset import Dataset


class DatasetAPI(Dataset):
    def __init__(self, fuente):
        super().__init__(fuente)


    def cargar_datos(self):
        try:
            response = requests.get(self.fuente)
            if response.status_code == 200:
                df = pd.json_normalize(response.json())

                def es_lista(x):
                    return isinstance(x, list)
                
                def lista_a_string(x):
                    if es_lista(x):
                        return ', '.join(map(str, x))
                
                for col in df.columns:
                    if df[col].apply(es_lista).any():
                        df[col] = df[col].apply(lista_a_string)

                self.datos = df
                print("API cargada")

                if self.validar_datos():
                    self.transformar_datos()
            else:
                print("Error en respuesta desde API")

        except Exception as e:
            print(f"Error APÎ: {e}")