from src.core.ctypes_utils import CtypesUtils
from src.core.validation_utils import ValidationUtils
from src.core.config import config

from time import sleep

class PegoModel:
    def __init__(self):
        self.ctype = CtypesUtils()
        self.validator = ValidationUtils()

    def collect_crystals(self):
        self.ctype.move_mouse_grau(0, 10, config["pixel_per_grau"])
        self.ctype.press("f")
        self.validator.wait_open(*config["validation"]["inventory_validation"],key="f")
        self.ctype.move_mouse_absolute(*config["player_inventory"]["drop_all"])
        self.ctype.left_click()
        self.ctype.move_mouse_absolute(*config["dino_inventory"]["transfer_all"])
        self.ctype.left_click()
        self.ctype.press("escape")
        sleep(1)
        self.ctype.move_mouse_grau(0, -10, config["pixel_per_grau"])