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
db = DataSaver()

archivos = [f for f in os.listdir(FILES_DIR) if os.path.isfile(os.path.join(FILES_DIR, f))]

print(archivos)


def procesar_archivos():
    resultados = []

    print(f'Se detectó {len(archivos)} archivo(s) en la carpeta {FILES_DIR}')

    for i, archivo in enumerate(archivos, start=1):
        print("\n" + "=" * 80)
        print(f"{f'Procesando archivo {i}/{len(archivos)} : {archivo}':^80}")
        print("=" * 80)

        ruta = os.path.join(FILES_DIR, archivo)
        nombre =  os.path.splitext(archivo)[0].lower()
        extension = os.path.splitext(archivo)[1].lower()

        clase_dataset = EXTENSIONES.get(extension)

        #print(f'{ruta}, {nombre}, {extension}, {clase_dataset}')

        if clase_dataset:
            dataset = clase_dataset(ruta)
            try:
                dataset.cargar_datos()
                #dataset.mostrar_resumen()
                db.guardar_dataframe(dataset.datos, nombre+f'{os.path.splitext(archivo)[1].lower().replace('.', '_')}')
                
                resultados.append(f"{archivo}: cargado con éxito.")
            except Exception as e:
                resultados.append(f"{archivo}: error - {e}")
        else:
            resultados.append(f"{archivo}: extensión no soportada.")

    return resultados

procesar_archivos()