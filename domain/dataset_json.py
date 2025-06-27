from domain.dataset import Dataset
import pandas as pd
import os, json, ast, warnings

class DatasetJSON(Dataset):
    def __init__(self, fuente):
        super().__init__(fuente)
            
    def es_posible_json(self, val):
        if not isinstance(val, str): return False
        return (val.startswith('{') and val.endswith('}')) or (val.startswith('[') and val.endswith(']'))

    def intentar_parsear(self, val):
        try:
            return ast.literal_eval(val)
        except:
            try:
                return json.loads(val)
            except:
                return val

    def intentar_convertir_fecha(self, val):
        try:
            with warnings.catch_warnings():
                warnings.simplefilter("ignore", category=UserWarning)
                if isinstance(val, dict) and '$date' in val:
                    fecha = pd.to_datetime(val['$date'], errors="coerce")
                    #print(f'1 {fecha}')
                else:
                    fecha = pd.to_datetime(val, errors="coerce")
                    #print(f'2 {fecha}')

            if pd.isna(fecha):
                return val  

            return fecha.isoformat()  

        except:
            return val


        
    def transformar_datos(self):
        print('Transformando JSON...')
        if self.datos is not None:
            try:
                self.datos.columns = self.datos.columns.str.strip().str.lower().str.replace(" ", "_")

                for col in self.datos.select_dtypes(include="object").columns:
                    if col == "_id":
                        continue
                    nueva_col = []
                    for val in self.datos[col]:
                        if isinstance(val, str):
                            val = val.strip()

                            if self.es_posible_json(val):
                                val = self.intentar_parsear(val)

                        val = self.intentar_convertir_fecha(val)

                        if isinstance(val, (list, dict)):
                            val = json.dumps(val, ensure_ascii=False)

                        nueva_col.append(val)

                    self.datos[col] = nueva_col

                print("Transformaciones aplicadas")
            except Exception as e:
                print(f"Error transformando: {e}")
                raise
        else:
            print("No hay datos para transformar")



    def validar_datos(self):
        print('Validando datos...')
        if self.datos is None or self.datos.empty:
            raise ValueError("Archivo vacío o no cargado correctamente")

        print(f"Tipos de datos detectados: {self.datos.dtypes}")

        try:
            nulos = self.datos.isnull().sum().sum()
            print(f"{nulos} valores nulos encontrados")
        except Exception as e:
            print(f"Error detectando nulos: {e}")

        datos_validos = self.datos.copy()
        for col in datos_validos.columns:
            if datos_validos[col].apply(lambda x: isinstance(x, (dict, list))).any():
                datos_validos[col] = datos_validos[col].astype(str)

        try:
            duplicados = datos_validos.duplicated().sum()
            if duplicados > 0:
                print(f"{duplicados} filas duplicadas encontradas")
        except Exception as e:
            print(f"Error detectando duplicados: {e}")

        try:
            columnas_vacias = [col for col in self.datos.columns if self.datos[col].isnull().all()]
            if columnas_vacias:
                print(f"Columnas vacías: {columnas_vacias}")
        except Exception as e:
            print(f"Error detectando columnas vacías: {e}")

        try:
            columnas_unicas = [col for col in datos_validos.columns if datos_validos[col].nunique() <= 1]
            if columnas_unicas:
                print(f"Columnas con un único valor: {columnas_unicas}")
        except Exception as e:
            print(f"Error detectando columnas únicas: {e}")

        print('Validación finalizada')
        return True

    def cargar_datos(self):
        print(f"Intentando leer el archivo: {self.fuente}")
        print(f"Existe: {os.path.exists(self.fuente)}")
        print(f"Ruta absoluta: {os.path.abspath(self.fuente)}")

        print(f'Cargando datos desde .json...')        
        try:
            df = pd.read_json(self.fuente, lines=True)
            self.datos = df 
            print("JSON cargado")

            if self.validar_datos():
                print("Datos JSON validados")
                self.transformar_datos()
            else:
                print('Error en validacion')
        
        except Exception as e:
            return(f"Error cargando JSON: {e}")
