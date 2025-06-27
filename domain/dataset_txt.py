from domain.dataset import Dataset
import pandas as pd

class DatasetTXT(Dataset):
    def __init__(self, fuente):
        super().__init__(fuente)

    def cargar_datos(self):
        print(f'Cargando datos desde .txt...')

        try:
            df = pd.read_csv(self.fuente, sep="\t")
            self.datos = df
            print("Txt cargado")

            if self.validar_datos():
                print("Datos txt validados")
                self.transformar_datos()
        
        except Exception as e:
            return(f"Error cargando txt: {e}")