from os import path
from domain.dataset_csv import DatasetCSV
from domain.dataset_excel import DatasetExcel

csv_path = path.join(path.dirname(__file__), "files/w_mean_prod.csv")
excel_path = path.join(path.dirname(__file__), "files/ventas.xlsx")


csv = DatasetCSV(csv_path)
csv.cargar_datos()

excel = DatasetExcel(excel_path)
excel.cargar_datos()