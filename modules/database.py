import json
import os

FILE_DATA = "data/pelanggan.json"

def load_data():

    if not os.path.exists(FILE_DATA):
        return []

    with open(FILE_DATA, "r") as file:
        return json.load(file)


def simpan_data(data):

    with open(FILE_DATA, "w") as file:
        json.dump(data, file, indent=4)