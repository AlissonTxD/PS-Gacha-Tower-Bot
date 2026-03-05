from src.core.ctypes_utils import CtypesUtils
from src.core.config import config
from src.core.validation_utils import ValidationUtils
from time import sleep

class GachaModel:
    def __init__(self):
        self.ctype = CtypesUtils()
        self.first_time = True
        self.validator = ValidationUtils()
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

        self.ctype.centralize(actual_yaw, 0, config["pixel_per_grau"])
        self.ctype.move_mouse_grau(first_move, 0, config["pixel_per_grau"])
        self.__open_inventory()
        if self.first_time:
            self.__first_row()
        else:
            self.__refeed_row()
        self.ctype.move_mouse_grau(last_move, 0, config["pixel_per_grau"])

    def __open_inventory(self):
        self.ctype.press("f")
        self.validator.wait_open(*config["validation"]["inventory_validation"], key="f")

    def __first_row(self):
        self.ctype.move_mouse_absolute(*config["dino_inventory"]["search"])
        self.ctype.left_click()
        self.ctype.write_text("owl")
        self.ctype.move_mouse_absolute(*config["dino_inventory"]["transfer_all"])
        self.ctype.left_click()
        self.ctype.move_mouse_absolute(*config["dino_inventory"]["search"])
        self.ctype.left_click()
        self.ctype.write_text("owl")
        self.ctype.move_mouse_absolute(*config["dino_inventory"]["drop_all"])
        self.ctype.left_click()
        self.ctype.move_mouse_absolute(*config["player_inventory"]["search"])
        self.ctype.left_click()
        self.ctype.write_text("owl")
        self.ctype.move_mouse_absolute(*config["player_inventory"]["first_slot"])
        self.ctype.left_click()
        for _ in range(15):
            self.ctype.press("t")
            sleep(0.35)
        self.ctype.move_mouse_absolute(*config["player_inventory"]["search"])
        self.ctype.left_click()
        for _ in range(5):
            self.ctype.press("backspace")
        self.ctype.write_text("seed")
        self.ctype.move_mouse_absolute(*config["player_inventory"]["transfer_all"])
        self.ctype.left_click()
        self.ctype.press("escape")
        sleep(1)

    def __refeed_row(self):
        self.ctype.move_mouse_absolute(*config["player_inventory"]["search"])
        self.ctype.left_click()
        self.ctype.write_text("seed")
        self.ctype.move_mouse_absolute(*config["player_inventory"]["transfer_all"])
        self.ctype.left_click()
        self.ctype.move_mouse_absolute(*config["dino_inventory"]["first_slot"])
        for _ in range(5):
            self.ctype.press("t")
            sleep(0.4)
        self.ctype.press("escape")
        sleep(1)

    