from abc import ABC, abstractmethod

class Dataset(ABC):
    def __init__(self, fuente):
        self.__fuente = fuente
        self.__datos = None
    
    @property
    def datos(self):
        return self.__datos
    
    @datos.setter
    def datos(self, value):
        self.__datos = value

    @property
    def fuente(self):
        return self.__fuente
    
    
    @abstractmethod
    def cargar_datos(self):
        pass

    def validar_datos(self):
        print('Validando datos...')
        if self.datos is None or self.datos.empty:
            raise ValueError("Archivo vacío o no cargado correctamente")

        print(f"Tipos de datos detectados: {self.datos.dtypes}")

        nulos = self.datos.isnull().sum().sum()
        if nulos > 0:
            print(f"{nulos} valores nulos encontrados")

        duplicados = self.datos.duplicated().sum()
        if duplicados > 0:
            print(f"{duplicados} filas duplicadas encontradas")

        columnas_vacias = [col for col in self.datos.columns if self.datos[col].isnull().all()]
        if columnas_vacias:
            print(f"Columnas vacías: {columnas_vacias}")

        columnas_unicas = [col for col in self.datos.columns if self.datos[col].nunique() <= 1]
        if columnas_unicas:
            print(f"Columnas con un único valor: {columnas_unicas}")

        return True

        

    def transformar_datos(self):
        if self.datos is not None:
            self.__datos.columns = (self.datos.columns.str.strip().str.lower().str.replace(" ", "_"))
            self.__datos = self.datos.drop_duplicates().copy()
            for col in self.datos.select_dtypes(include="object").columns:
                self.__datos[col] = self.datos[col].astype(str).str.strip()
                        
            print("Transformaciones aplicadas")
        else: 
            print("No hay datos para transformar")
     
    def mostrar_resumen(self):
        return print(self.datos.describe(include='all') if self.datos is not None else "No hay datos")
        
