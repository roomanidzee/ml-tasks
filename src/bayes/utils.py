import csv

from typing import Tuple, List
from src.commons.types import Float

CSV_DATA = Tuple[List[List[Float]], List[List[Float]]]


def load_data(
        csv_path: str
) -> CSV_DATA:

    with open(csv_path, 'r') as csv_file:
        data_reader = csv.reader(csv_file)
        csv_rows = [row for row in data_reader]

    symptoms = [list(map(float, elem)) for elem in csv_rows]
    diseases = []
    columns_count = len(csv_rows[0])

    for i in range(columns_count):
        diseases.append([float(item[i]) for item in csv_rows])

    return symptoms, diseases
