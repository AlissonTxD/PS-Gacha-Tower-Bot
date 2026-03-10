from src.core.ctypes_utils import CtypesUtils
from src.core.validation_utils import ValidationUtils
from src.core.config import config
from time import sleep



class render_station_model:
    def __init__(self):
        self.ctype = CtypesUtils()
        self.validator = ValidationUtils()
        self.yaw_base = self.ctype.yaw_dict["yaw_meio"]


    def leave_bed_start(self):
        self.ctype.press(key= "e", hold = 3)
        self.validator.wait_close(*config["validation"]["tek_bed_buff_validation"])
        self.ctype.centralize(self.yaw_base, 0, config["pixel_per_grau"])
        

    def join_bed_end(self):
        self.ctype.centralize(self.yaw_base, 0, config["pixel_per_grau"])
        self.ctype.key_down("e")
        self.validator.wait_open(*config["validation"]["tek_bed_radial_validation"],key="e")
        self.ctype.move_mouse_absolute(*config["misc"]["lay_on"])
        self.ctype.left_click()
        self.ctype.key_up("e")
