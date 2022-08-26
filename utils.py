import json
from app.config import BaseConfig


def read_data_from_json() -> dict:
    """Reading data from json file"""
    with open(BaseConfig.DATA_DIR, encoding="UTF-8") as fp:
        data = json.load(fp)
    return data