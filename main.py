import os
from os import path
from domain.dataset_csv import DatasetCSV
from domain.dataset_excel import DatasetExcel
from domain.dataset_json import DatasetJSON
from domain.dataset_parquet import DatasetParquet
from domain.dataset_txt import DatasetTXT
from data.data_saver import DataSaver

EXTENSIONES = {
    '.csv': DatasetCSV,
    '.xlsx': DatasetExcel,
    '.xls': DatasetExcel,
    '.parquet': DatasetParquet,
    '.json': DatasetJSON,
    '.txt': DatasetTXT,
}

FILES_DIR = 'files'

archivos = [f for f in os.listdir(FILES_DIR) if os.path.isfile(os.path.join(FILES_DIR, f))]

print(archivos)


def procesar_archivos():
    resultados = []

    print(f'Se detectaron {len(archivos)} archivos en la carpeta {FILES_DIR}')

    for archivo in archivos:
        print(f'{archivo}')
        ruta = os.path.join(FILES_DIR, archivo)
        extension = os.path.splitext(archivo)[1].lower()

        clase_dataset = EXTENSIONES.get(extension)

        print(f'{ruta}, {extension}, {clase_dataset}')

        if clase_dataset:
            dataset = clase_dataset(ruta)
            try:
                dataset.cargar_datos()
                dataset.mostrar_resumen()
                resultados.append(f"{archivo}: cargado con éxito.")
            except Exception as e:
                resultados.append(f"{archivo}: error - {e}")
        else:
            resultados.append(f"{archivo}: extensión no soportada.")

    return resultados

procesar_archivos()

# db = DataSaver()
# db.guardar_dataframe(csv.datos, "w_mean_prod_csv")
# db.guardar_dataframe(excel.datos, "ventas_csv")
# db.guardar_dataframe(api.datos, "provincia_api")