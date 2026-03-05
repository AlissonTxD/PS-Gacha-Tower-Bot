from src.core.ctypes_utils import CtypesUtils
from src.core.config import config
from src.core.validation_utils import ValidationUtils

from time import sleep


class TeleportModel:
    def __init__(self):
        self.ctype = CtypesUtils()
        self.validator = ValidationUtils()

    def teleport(self, tp_name: str):
        self.ctype.move_mouse_grau(0, -87, config["pixel_per_grau"])
        self.ctype.press("e")
        self.validator.wait_open(*config["validation"]["teleport_validation"],key="e")
        self.ctype.move_mouse_absolute(*config["teleport"]["search_map"])
        self.ctype.left_click()
        self.ctype.write_text(tp_name)
        self.ctype.move_mouse_absolute(*config["teleport"]["first_on_list"])
        self.ctype.left_click()
        self.ctype.move_mouse_absolute(*config["teleport"]["teleport_button"])
        self.ctype.left_click()
        sleep(2)
        self.ctype.move_mouse_grau(0, 87, config["pixel_per_grau"])

    def fast_teleport(self):
        pass