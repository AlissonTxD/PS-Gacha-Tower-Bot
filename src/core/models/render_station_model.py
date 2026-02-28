from src.core.ctypes_utils import CtypesUtils
from time import sleep
import logging
yaw_base = 136.32 #gacha 1
yaw2 = 137.36 #gacha 2
yaw3 = 134.57 #meio
pitch_base = 0
PIXELS_POR_GRAU = 4.57


class render_station_model:
    def __init__(self):
        self.ctype = CtypesUtils()


    def leave_bed_start(self):
        self.ctype.press("e")
        sleep(2)
        self.ctype.centralize(yaw_base, pitch_base, PIXELS_POR_GRAU)
        sleep(1)
        

    def join_bed_end(self):
        sleep(2)
        self.ctype.centralize(yaw_base, pitch_base, PIXELS_POR_GRAU)
        sleep(0.5)
        self.ctype.key_down("e")
        sleep(0.5)
        self.ctype.move_mouse_relative(100, -75)
        self.ctype.key_up("e")