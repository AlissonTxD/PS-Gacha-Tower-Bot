from src.core.ctypes_utils import CtypesUtils
from src.core.config import config

from time import sleep


class TeleportModel:
    def __init__(self):
        self.ctype = CtypesUtils()

    def teleport(self, tp_name: str):
        self.ctype.move_mouse_grau(0, -87, config["pixel_per_grau"])
        sleep(0.5)
        self.ctype.press("e")
        sleep(1)
        self.ctype.move_mouse_absolute(*config["coord_search_teleport_map"])
        self.ctype.left_click()
        sleep(0.5)
        self.ctype.write_text(tp_name)
        sleep(0.5)
        self.ctype.move_mouse_absolute(*config["coord_first_on_list"])
        self.ctype.left_click()
        sleep(0.5)
        self.ctype.move_mouse_absolute(*config["coord_teleport_button"])
        self.ctype.left_click()
        sleep(2)
        self.ctype.move_mouse_grau(0, 87, config["pixel_per_grau"])
        sleep(0.5)