import os

BASE_DIR = os.path.dirname(os.path.relpath(__file__))


class BaseConfig:
    STAMINA_PER_ROUND = 1
    DEBUG = True
    DATA_DIR = os.path.join(os.path.dirname(BASE_DIR), 'data/equipment.json')