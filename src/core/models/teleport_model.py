from src.core.ctypes_utils import CtypesUtils
from time import sleep

PIXELS_POR_GRAU = 4.57
COORD_SEARCH = (543, 1289)
COORD_FIRST_ON_LIST = (394, 294)
COORD_TELEPORT_BUTTON = (2143, 1271)

class TeleportModel:
    def __init__(self):
        self.ctype = CtypesUtils()

    def teleport(self, nome: str):
        self.ctype.move_mouse_grau(0, -87, PIXELS_POR_GRAU)
        sleep(0.5)
        self.ctype.press("e")
        sleep(1)
        self.ctype.move_mouse_absolute(*COORD_SEARCH)
        self.ctype.left_click()
        sleep(0.5)
        self.ctype.write_text(nome)
        sleep(0.5)
        self.ctype.move_mouse_absolute(*COORD_FIRST_ON_LIST)
        self.ctype.left_click()
        sleep(0.5)
        self.ctype.move_mouse_absolute(*COORD_TELEPORT_BUTTON)
        self.ctype.left_click()
        sleep(2)
        self.ctype.move_mouse_grau(0, 87, PIXELS_POR_GRAU)
        sleep(0.5)