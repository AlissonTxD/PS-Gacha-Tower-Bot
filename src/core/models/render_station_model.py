from time import sleep

from src.core.config.config import config
from src.core.services.ctypes_services import CtypesServices
from src.core.services.validation_services import ValidationUtils


class render_station_model:
    def __init__(self):
        self.ctype = CtypesServices()
        self.validator = ValidationUtils()
        self.yaw_base = config["yaw"]


    def leave_bed_start(self):
        self.ctype.press(key= "e", hold = 3)
        sleep(1)
        self.ctype.centralize(self.yaw_base, 0, config["pixel_per_grau"])
        

    def join_bed_end(self):
        self.ctype.centralize(self.yaw_base, 0, config["pixel_per_grau"])
        self.ctype.key_down("e")
        self.validator.wait_open(*config["validation"]["tek_bed_radial_validation"],key="e")
        self.ctype.move_mouse_absolute(*config["misc"]["lay_on"])
        self.ctype.left_click()
        self.ctype.key_up("e")
        self.validator.wait_open(*config["validation"]["inventory_validation"],key="v")
        self.ctype.move_mouse_absolute(*config["player_inventory"]["drop_all"])
        self.ctype.left_click()
        self.ctype.press("escape")
        sleep(1)
