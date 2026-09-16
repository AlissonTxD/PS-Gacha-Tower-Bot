from time import sleep

from .base_model import BaseModel


class PegoModel(BaseModel):
    def __init__(self, general_config):
        super().__init__(general_config)

    def collect_crystals(self):
        self.gt.move_mouse_grau(0, 10, self.pixel_per_degree)
        self.open_inventory()
        self.ctype.move_mouse_absolute(*self.configs["player_inventory"]["drop_all"])
        self.ctype.left_click()
        self.ctype.move_mouse_absolute(*self.configs["dino_inventory"]["transfer_all"])
        self.ctype.left_click()
        self.ctype.press("escape")
        sleep(1)
        self.gt.move_mouse_grau(0, -10, self.pixel_per_degree)