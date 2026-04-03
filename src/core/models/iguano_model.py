from src.core.ctypes_utils import CtypesUtils
from src.core.config import config
from src.core.validation_utils import ValidationUtils

from time import sleep

class IguanoModel:
    def __init__(self):
        self.ctype = CtypesUtils()
        self.validator = ValidationUtils()
        self.yaw_base = config["yaw"]

    def get_seeds_w_berry(self):
        self.ctype.centralize(self.yaw_base, 0, config["pixel_per_grau"])
        self.__open_inventory()
        self.ctype.move_mouse_absolute(*config["player_inventory"]["search"])
        self.ctype.left_click()
        self.ctype.write_text("mejoberry")
        self.ctype.move_mouse_absolute(*config["player_inventory"]["transfer_all"])
        self.ctype.left_click()
        sleep(0.5)
        self.ctype.move_mouse_absolute(*config["player_inventory"]["drop_all"])
        self.ctype.left_click()
        self.ctype.press("escape")
        sleep(1)
        self.ctype.press("e")
        sleep(2)
        self.__open_inventory()
        self.ctype.move_mouse_absolute(*config["dino_inventory"]["search"])
        self.ctype.left_click()
        self.ctype.write_text("seed")
        self.ctype.move_mouse_absolute(*config["dino_inventory"]["transfer_all"])
        self.ctype.left_click()
        self.ctype.press("escape")
        sleep(1)
        
    def get_seeds_w_no_berrys(self):
        self.__open_inventory()
        self.ctype.move_mouse_absolute(*config["dino_inventory"]["first_slot"])
        self.ctype.left_click()
        for _ in range(5):
            self.ctype.press("t")
            sleep(0.4)
        self.ctype.move_mouse_absolute(*config["player_inventory"]["search"])
        self.ctype.left_click()
        self.ctype.write_text("mejoberry")
        self.ctype.move_mouse_absolute(*config["player_inventory"]["transfer_all"])
        self.ctype.left_click()
        sleep(0.5)
        self.ctype.move_mouse_absolute(*config["player_inventory"]["drop_all"])
        self.ctype.left_click()
        self.ctype.press("escape")
        sleep(1)
        self.ctype.press("e")
        sleep(1)
        self.__open_inventory()
        self.ctype.move_mouse_absolute(*config["dino_inventory"]["search"])
        self.ctype.left_click()
        self.ctype.write_text("seed")
        self.ctype.move_mouse_absolute(*config["dino_inventory"]["transfer_all"])
        self.ctype.left_click()
        self.ctype.press("escape")
        sleep(1)
        
    def __open_inventory(self):
        self.ctype.press("f")
        self.validator.wait_open(*config["validation"]["inventory_validation"], key="f")