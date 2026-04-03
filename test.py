from src.core.ctypes_utils import CtypesUtils
from src.core.validation_utils import ValidationUtils
from time import sleep
from src.core.config import config

validator = ValidationUtils()
ctype = CtypesUtils()

while True:
    validator.wait_open(*config["validation"]["inventory_validation"], key="v")
    ctype.move_mouse_absolute(*config["player_inventory"]["transfer_all"], deley=0)
    ctype.left_click()
    ctype.move_mouse_absolute(*config["player_inventory"]["search"], deley=0)
    ctype.left_click()
    ctype.write_text("t")
    sleep(0.1)
    ctype.move_mouse_absolute(*config["player_inventory"]["drop_all"], deley=0)
    ctype.left_click()
    ctype.press("escape")
    sleep(1)
