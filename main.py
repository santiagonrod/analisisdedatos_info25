from os import path
from domain.dataset_csv import DatasetCSV

csv_path = path.join(path.dirname(__file__), "files/w_mean_prod.csv")


csv = DatasetCSV(csv_path)
csv.cargar_datos()