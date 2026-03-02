from src.core.ctypes_utils import CtypesUtils
from time import sleep

PIXELS_POR_GRAU = 4.57
COORD_PESQUISA = (360, 266)
COORD_TRANSFER_ALL = (552, 261)
COORD_PESQUISA_DINO = (1719, 260)
COORD_TRANSFER_ALL_DINO = (1913, 263)
COORD_DROP_ALL = (617, 270)
COORD_FIRST_SLOT_DINO = (1659, 373)
COORD_FIRST_SLOT_PLAYER = (296, 369)
COORD_DROP_ALL_DINO = (1980, 262)

class BerrysModel:
    def __init__(self):
        self.ctype = CtypesUtils()
        self.yaw_base = self.ctype.yaw_dict["yaw_meio"]

    def get_berrys(self):
        self.ctype.centralize(self.yaw_base, 0, PIXELS_POR_GRAU)
        self.__takeall()
        self.ctype.move_mouse_grau(0,-30, PIXELS_POR_GRAU)
        self.__takeall()

    def __takeall(self):
        self.ctype.press("f")
        sleep(1)
        self.ctype.move_mouse_absolute(*COORD_TRANSFER_ALL_DINO)
        self.ctype.left_click()
        sleep(1)
        self.ctype.press("escape")
        sleep(2)
