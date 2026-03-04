from src.core.ctypes_utils import CtypesUtils
from src.core.config import config
from src.core.validation_utils import ValidationUtils

from time import sleep


class CrystalCracker:
    def __init__(self):
        self.validator = ValidationUtils()
        self.ctype = CtypesUtils()
        self.yaw = self.ctype.yaw_dict["yaw_meio"]

    def crack_crystals(self):
        self._open_crystal()
        self.ctype.centralize(self.yaw, 0, config["pixel_per_grau"])
        self._put_in_dedicated()
        self.ctype.centralize(self.yaw, 0, config["pixel_per_grau"])
        self.ctype.move_mouse_grau(90, 0, config["pixel_per_grau"])
        self._place_in_vault(["riot","cliff","tree","behe"])
        self.ctype.move_mouse_grau(-90, 0, config["pixel_per_grau"])
        self.ctype.move_mouse_grau(-90, 0, config["pixel_per_grau"])
        self._place_in_vault(["fabricated","shotgun","assault"])
        self.ctype.move_mouse_grau(-90, 0, config["pixel_per_grau"])
        self.__open_inventory()
        self.ctype.move_mouse_absolute(*config["player_inventory"]["transfer_all"])
        self.ctype.left_click()
        sleep(0.5)
        self.ctype.move_mouse_absolute(*config["misc"]["grind_all"])
        self.ctype.left_click()
        self.ctype.press("escape")
        sleep(1)
        self.ctype.centralize(self.yaw, 0, config["pixel_per_grau"])

    def grind_items(self):
        self.ctype.move_mouse_grau(-90, 0, config["pixel_per_grau"])
        self.__open_inventory()
        self.ctype.move_mouse_absolute(*config["dino_inventory"]["transfer_all"])
        self.ctype.left_click()
        self.ctype.press("escape")
        sleep(1)
        self.ctype.centralize(self.yaw, 0, config["pixel_per_grau"])
        self._put_in_dedicated()
        self.ctype.centralize(self.yaw, 0, config["pixel_per_grau"])
        self.ctype.press("v")
        self.validator.wait_open(*config["validation"]["inventory_validation"])
        self.ctype.move_mouse_absolute(*config["player_inventory"]["drop_all"])
        self.ctype.left_click()
        self.ctype.press("escape")
        sleep(1)


    def _open_crystal(self):
        for _ in range(60):
            key_list = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "zero"]
            for key in key_list:
                self.ctype.press(key)
                sleep(0.01)

    def _place_in_vault(self, list_of_items):
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
        self.ctype.move_mouse_grau(15,10, config["pixel_per_grau"])#dedicada direita cima
        self.ctype.press("e")
        self.ctype.move_mouse_grau(0, -30, config["pixel_per_grau"])#dedicada direita meio
        self.ctype.press("e")
        self.ctype.move_mouse_grau(0, -40, config["pixel_per_grau"])#dedicada direita baixo
        self.ctype.press("e")
        self.ctype.move_mouse_grau(-30, 0, config["pixel_per_grau"])#dedicada esquerda baixo
        self.ctype.press("e")
        self.ctype.move_mouse_grau(0, 40, config["pixel_per_grau"])#dedicada esquerda meio
        self.ctype.press("e")
        self.ctype.move_mouse_grau(0, 30, config["pixel_per_grau"])#dedicada esquerda cima
        self.ctype.press("e")

    def __open_inventory(self):
        self.ctype.press("f")
        self.validator.wait_open(*config["validation"]["inventory_validation"])