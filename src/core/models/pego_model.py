from time import sleep

from src.core.services.ctypes_services import CtypesServices
from src.core.services.validation_services import ValidationServices


class PegoModel:
    def __init__(self):
        self.ctype = CtypesServices()
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