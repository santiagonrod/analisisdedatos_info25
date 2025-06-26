from os import path
from domain.dataset_csv import DatasetCSV
from domain.dataset_excel import DatasetExcel
from domain.dataset_api import DatasetAPI
from data.data_saver import DataSaver

csv_path = path.join(path.dirname(__file__), "files/w_mean_prod.csv")
excel_path = path.join(path.dirname(__file__), "files/ventas.xlsx")


csv = DatasetCSV(csv_path)
csv.cargar_datos()
csv.mostrar_resumen()

excel = DatasetExcel(excel_path)
excel.cargar_datos()
excel.mostrar_resumen()

api = DatasetAPI("https://apis.datos.gob.ar/georef/api/provincias")
api.cargar_datos()
api.mostrar_resumen()

db = DataSaver()
db.guardar_dataframe(csv.datos, "w_mean_prod_csv")
db.guardar_dataframe(excel.datos, "ventas_csv")
# db.guardar_dataframe(api.datos, "provincia_api")