
from src.core.ctypes_utils import CtypesUtils
from time import sleep

YAW = 134.57 #meio
PIXELS_POR_GRAU = 4.57
COORD_PESQUISA = (360, 266)
COORD_TRANSFER_ALL = (552, 261)
COORD_GRIND_ALL = (1268, 1110)
COORD_TAKE_ALL = (1914, 262)
COORD_DROP_ALL = (617, 270)

class CrystalCracker:
    def __init__(self):
        self.ctype = CtypesUtils()

    def crack_crystals(self):
        sleep(2)
        self._open_crystal()
        self.ctype.centralize(YAW, 0, PIXELS_POR_GRAU)
        sleep(0.5)
        self._put_in_dedicated()
        self.ctype.centralize(YAW, 0, PIXELS_POR_GRAU)
        sleep(0.5)
        self.ctype.move_mouse_grau(90, 0, PIXELS_POR_GRAU)
        self._place_in_vault(["riot","cliff","tree","behe"])
        self.ctype.move_mouse_grau(-90, 0, PIXELS_POR_GRAU)
        sleep(0.5)
        self.ctype.move_mouse_grau(-90, 0, PIXELS_POR_GRAU)
        self._place_in_vault(["fabricated","pump","assault"])
        sleep(0.5)
        self.ctype.move_mouse_grau(-90, 0, PIXELS_POR_GRAU)
        self.ctype.press("f")
        sleep(0.5)
        self.ctype.move_mouse_absolute(*COORD_TRANSFER_ALL)
        self.ctype.left_click()
        sleep(1)
        self.ctype.move_mouse_absolute(*COORD_GRIND_ALL)
        self.ctype.left_click()
        self.ctype.press("escape")
        sleep(2)

    def grind_items(self):
        self.ctype.centralize(YAW, 0, PIXELS_POR_GRAU)
        sleep(0.5)
        self.ctype.move_mouse_grau(-90, 0, PIXELS_POR_GRAU)
        self.ctype.press("f")
        sleep(1)
        self.ctype.move_mouse_absolute(*COORD_TAKE_ALL)
        self.ctype.left_click()
        self.ctype.press("escape")
        sleep(2)
        self.ctype.centralize(YAW, 0, PIXELS_POR_GRAU)
        self._put_in_dedicated()
        self.ctype.press("v")
        sleep(1)
        self.ctype.move_mouse_absolute(*COORD_DROP_ALL)
        self.ctype.left_click()
        sleep(1)
        self.ctype.press("escape")
        sleep(2)


    def _open_crystal(self):
        for _ in range(30):
            key_list = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "zero"]
            for key in key_list:
                self.ctype.press(key)
                sleep(0.01)

    def _place_in_vault(self, list_of_items):
        sleep(1)
        self.ctype.press("f")
        sleep(3)
        for item in list_of_items:
            self.ctype.move_mouse_absolute(*COORD_PESQUISA)
            self.ctype.left_click()
            sleep(0.5)
            self.ctype.write_text(item)
            self.ctype.move_mouse_absolute(*COORD_TRANSFER_ALL)
            self.ctype.left_click()
            sleep(0.5)
        self.ctype.press("escape")
        sleep(3)

    def _put_in_dedicated(self):
        self.ctype.move_mouse_grau(15,10, PIXELS_POR_GRAU)#dedicada direita cima
        self.ctype.press("e")
        self.ctype.move_mouse_grau(0, -30, PIXELS_POR_GRAU)#dedicada direita meio
        self.ctype.press("e")
        self.ctype.move_mouse_grau(0, -40, PIXELS_POR_GRAU)#dedicada direita baixo
        self.ctype.press("e")
        self.ctype.move_mouse_grau(-30, 0, PIXELS_POR_GRAU)#dedicada esquerda baixo
        self.ctype.press("e")
        self.ctype.move_mouse_grau(0, 40, PIXELS_POR_GRAU)#dedicada esquerda meio
        self.ctype.press("e")
        self.ctype.move_mouse_grau(0, 30, PIXELS_POR_GRAU)#dedicada esquerda cima
        self.ctype.press("e")