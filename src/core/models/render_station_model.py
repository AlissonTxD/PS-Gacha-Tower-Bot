from src.core.ctypes_utils import CtypesUtils
from time import sleep


PITCH_BASE = 0
PIXELS_POR_GRAU = 4.57
COORD_LAY_DOWN = (1503, 578)


class render_station_model:
    def __init__(self):
        self.ctype = CtypesUtils()
        self.yaw_base = self.ctype.yaw_dict["yaw_meio"]


    def leave_bed_start(self):
        self.ctype.press("e")
        sleep(2)
        self.ctype.centralize(self.yaw_base, PITCH_BASE, PIXELS_POR_GRAU)
        sleep(1)
        

    def join_bed_end(self):
        self.ctype.centralize(self.yaw_base, PITCH_BASE, PIXELS_POR_GRAU)
        sleep(0.5)
        self.ctype.key_down("e")
        sleep(1)
        self.ctype.move_mouse_absolute(*COORD_LAY_DOWN)
        self.ctype.left_click()
        sleep(1)
        self.ctype.key_up("e")
        sleep(1)