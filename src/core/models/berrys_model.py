from src.core.ctypes_utils import CtypesUtils
from src.core.config import config
from src.core.validation_utils import ValidationUtils

from time import sleep

class BerrysModel:
    def __init__(self):
        self.validator = ValidationUtils()
        self.ctype = CtypesUtils()
        self.yaw_base = config["yaw"]

    def get_berrys(self):
        self.ctype.centralize(self.yaw_base, 0, config["pixel_per_grau"])
        self.__takeall()
        self.ctype.move_mouse_grau(0,-40, config["pixel_per_grau"])
        self.__takeall()

    def __takeall(self):
        self.ctype.press("f")
        self.validator.wait_open(*config["validation"]["inventory_validation"],key="f")
        self.ctype.move_mouse_absolute(*config["dino_inventory"]["transfer_all"])
        self.ctype.left_click()
        self.ctype.press("escape")
        sleep(1)
