from time import sleep

from .base_model import BaseModel


class GachaModel(BaseModel):
    def __init__(self, general_config):
        super().__init__(general_config)

    def feed_gacha_pair_trap(self):
        self.gt.move_mouse_grau(40, 0, self.pixel_per_degree)
        self.__feed_gacha_trap()
        self.gt.move_mouse_grau(-80, 0, self.pixel_per_degree)
        self.__feed_gacha_trap()
        self.gt.move_mouse_grau(40, 0, self.pixel_per_degree)

    def test_gachas(self):
        #self.gt.centralize(*self.calibration)
        self.gt.move_mouse_grau(40, 0, self.pixel_per_degree)
        self.open_inventory()
        self.ctype.press("escape")
        sleep(1)
        self.gt.move_mouse_grau(-80, 0, self.pixel_per_degree)
        self.open_inventory()
        self.ctype.press("escape")
        sleep(1)

    def __feed_gacha_trap(self):
        self.open_inventory()
        self.ctype.move_mouse_absolute(
            *self.configs["player_inventory"]["transfer_all"]
        )
        self.ctype.left_click()
        self.ctype.press("escape")
        sleep(1)
