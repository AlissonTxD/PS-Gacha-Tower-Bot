from src.core.ctypes_utils import CtypesUtils
from src.core.config import config
from src.core.validation_utils import ValidationUtils

from time import sleep

class TrapModel:
    def __init__(self):
        self.validator = ValidationUtils()
        self.ctype = CtypesUtils()
        self.yaw_base = config["yaw"]

    def get_trap(self):
        self.ctype.centralize(self.yaw_base, 0, config["pixel_per_grau"])
        self.__takeall()

    def __takeall(self):
        self.ctype.press("f")
        self.validator.wait_open(*config["validation"]["inventory_validation"],key="f")
        sleep(0.1)
        self.ctype.move_mouse_absolute(*config["dino_inventory"]["search"])
        self.ctype.left_click()
        self.ctype.write_text("trap")
        self.ctype.move_mouse_absolute(*config["dino_inventory"]["first_slot"])
        self.ctype.left_click()
        for _ in range(150):
            self.ctype.press("t")
        self.ctype.press("escape")
        sleep(1)
