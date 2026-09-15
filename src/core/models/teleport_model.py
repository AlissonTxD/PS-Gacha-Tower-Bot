from time import sleep

from src.core.config.config import config
from src.core.services.ctypes_services import CtypesServices
from src.core.services.validation_services import ValidationUtils


class TeleportModel:
    def __init__(self):
        self.ctype = CtypesServices()
        self.validator = ValidationUtils()

    def teleport(self, tp_name: str):
        self.ctype.move_mouse_grau(0, -87, config["pixel_per_grau"])
        self.ctype.press("e")
        self.validator.wait_open(*config["validation"]["teleport_validation"],key="e")
        sleep(1)
        self.ctype.move_mouse_absolute(*config["teleport"]["search_map"])
        self.ctype.left_click()
        self.ctype.write_text(tp_name)
        sleep(0.1)
        self.ctype.move_mouse_absolute(*config["teleport"]["first_on_list"])
        self.ctype.left_click()
        self.ctype.move_mouse_absolute(*config["teleport"]["teleport_button"])
        self.ctype.left_click()
        sleep(2)
        self.ctype.move_mouse_grau(0, 87, config["pixel_per_grau"])

    def fast_teleport(self):
        pass