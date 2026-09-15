from time import sleep

from src.core.services.ctypes_services import CtypesServices
from src.core.services.gt_services import GtServices
from src.core.services.validation_services import ValidationServices


class CrystalCracker:
    def __init__(self, general_config: dict):
        self.validator = ValidationServices()
        self.ctype = CtypesServices()
        self.gt = GtServices()
        self.configs = general_config

    def crack_crystals(self):
        self._open_crystal()
        self.gt.centralize(self.configs["calibration"]["yaw"], 0, self.configs["calibration"]["pixel_per_degree"])
        self._put_in_dedicated()
        self.gt.centralize(self.configs["calibration"]["yaw"], 0, self.configs["calibration"]["pixel_per_degree"])

    def grind_items(self):
        self.ctype.move_mouse_grau(90, 0, config["pixel_per_grau"])
        self.__place_in_vault(["gate"])
        self.ctype.move_mouse_grau(-180, 0, config["pixel_per_grau"])
        self.__open_inventory()
        self.ctype.move_mouse_absolute(*config["player_inventory"]["transfer_all"])
        self.ctype.left_click()
        sleep(0.5)
        self.ctype.move_mouse_absolute(*config["misc"]["grind_all"])
        self.ctype.left_click()
        self.ctype.move_mouse_absolute(*config["dino_inventory"]["transfer_all"])
        self.ctype.left_click()
        self.ctype.press("escape")
        sleep(1)
        self.ctype.centralize(self.yaw, 0, config["pixel_per_grau"])
        self._put_in_dedicated()
        self.ctype.centralize(self.yaw, 0, config["pixel_per_grau"])


    def _open_crystal(self):
        key_list = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "zero"]
        for key in key_list:
            self.ctype.key_down(key)
        sleep(6)
        for key in key_list:
            self.ctype.key_up(key)

    def __place_in_vault(self, list_of_items):
        self.__open_inventory()
        sleep(1)
        if not self.validator.is_pixel_color(*config["validation"]["vault_full_validation"]):
            for item in list_of_items:
                self.ctype.move_mouse_absolute(*config["player_inventory"]["search"])
                self.ctype.left_click()
                self.ctype.write_text(item)
                self.ctype.move_mouse_absolute(*config["player_inventory"]["transfer_all"])
                self.ctype.left_click()
        else:
            print("vault full, skipando carai")
        self.ctype.press("escape")
        sleep(1)

    def _put_in_dedicated(self):
        self.ctype.move_mouse_grau(15, 60, config["pixel_per_grau"])
        self.ctype.press("e")
        self.ctype.move_mouse_grau(0, -30, config["pixel_per_grau"])
        self.ctype.press("e")
        self.ctype.move_mouse_grau(0, -40, config["pixel_per_grau"])
        self.ctype.press("e")
        self.ctype.move_mouse_grau(0, -40, config["pixel_per_grau"])
        self.ctype.press("e")


        self.ctype.move_mouse_grau(-30, 0, config["pixel_per_grau"])
        self.ctype.press("e")
        self.ctype.move_mouse_grau(0, 40, config["pixel_per_grau"])
        self.ctype.press("e")
        self.ctype.move_mouse_grau(0, 40, config["pixel_per_grau"])
        self.ctype.press("e")
        self.ctype.move_mouse_grau(0, 30, config["pixel_per_grau"])
        self.ctype.press("e")

    def __open_inventory(self):
        self.ctype.press("f")
        self.validator.wait_open(*config["validation"]["inventory_validation"],key="f")