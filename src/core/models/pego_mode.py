from src.core.ctypes_utils import CtypesUtils
from time import sleep


PIXELS_POR_GRAU = 4.57
COORD_TAKEALL_BUTTON = (1911, 265)

class PegoModel:
    def __init__(self):
        self.ctype = CtypesUtils()

    def collect_crystals(self):
        self.ctype.move_mouse_grau(0, 10, PIXELS_POR_GRAU)
        self.ctype.press("f")
        sleep(1)
        self.ctype.move_mouse_absolute(*COORD_TAKEALL_BUTTON)
        self.ctype.left_click()
        sleep(0.5)
        self.ctype.press("escape")
        sleep(1)
        self.ctype.move_mouse_grau(0, -10, PIXELS_POR_GRAU)
        sleep(0.5)