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

class GachaModel:
    def __init__(self):
        self.ctype = CtypesUtils()
        self.yaw_left = self.ctype.yaw_dict["yaw_left"]
        self.yaw_right = self.ctype.yaw_dict["yaw_right"]

    def feed_gacha(self, yaw: str, side: str):

        if yaw == "right":
            actual_yaw = self.yaw_right
        else:
            actual_yaw = self.yaw_left

        if side == "right":
            first_move = 40
            last_move = -40
        else:
            first_move = -40
            last_move = 40

        self.ctype.centralize(actual_yaw, 0, PIXELS_POR_GRAU)
        self.ctype.move_mouse_grau(first_move, 0, PIXELS_POR_GRAU)

        self.ctype.press("f")
        sleep(2)

        self.ctype.move_mouse_absolute(*COORD_PESQUISA_DINO)
        self.ctype.left_click()
        self.ctype.write_text("owl")
        sleep(1)

        self.ctype.move_mouse_absolute(*COORD_TRANSFER_ALL_DINO)
        self.ctype.left_click()
        sleep(1)

        self.ctype.move_mouse_absolute(*COORD_PESQUISA_DINO)
        self.ctype.left_click()
        self.ctype.write_text("owl")
        sleep(1)

        self.ctype.move_mouse_absolute(*COORD_DROP_ALL_DINO)
        self.ctype.left_click()
        sleep(1)

        for _ in range(2):
            self.ctype.move_mouse_absolute(*COORD_TRANSFER_ALL_DINO)
            self.ctype.left_click()

        sleep(1)

        self.ctype.move_mouse_absolute(*COORD_PESQUISA)
        self.ctype.left_click()
        self.ctype.write_text("owl")
        sleep(1)

        self.ctype.move_mouse_absolute(*COORD_FIRST_SLOT_PLAYER)
        self.ctype.left_click()

        for _ in range(15):
            self.ctype.press("t")
            sleep(0.5)

        sleep(1)

        self.ctype.move_mouse_absolute(*COORD_PESQUISA)
        self.ctype.left_click()

        for _ in range(5):
            self.ctype.press("backspace")

        self.ctype.write_text("seed")
        sleep(1)

        self.ctype.move_mouse_absolute(*COORD_TRANSFER_ALL)
        self.ctype.left_click()

        self.ctype.press("escape")
        sleep(1)

        self.ctype.move_mouse_grau(last_move, 0, PIXELS_POR_GRAU)


