from .base_model import BaseModel


class GachaModel(BaseModel):

    def __init__(self, general_config, stop_event):
        super().__init__(general_config, stop_event)

    def feed_gacha_pair_trap(self):
        if self.stop_event.is_set():
            return
        self.gt.move_mouse_grau(
            40, 0, self.pixel_per_degree
        )
        if self.stop_event.is_set():
            return
        self.__feed_gacha_trap()
        if self.stop_event.is_set():
            return
        self.gt.move_mouse_grau(
            -80, 0, self.pixel_per_degree
        )
        if self.stop_event.is_set():
            return
        self.__feed_gacha_trap()
        if self.stop_event.is_set():
            return
        self.gt.move_mouse_grau(
            40, 0, self.pixel_per_degree
        )

    def test_gachas(self):
        # not working yet
        pass

    def __feed_gacha_trap(self):
        if self.stop_event.is_set():
            return
        self.open_inventory()
        if self.stop_event.is_set():
            return
        self.ctype.move_mouse_absolute(
            *self.configs["player_inventory"]["transfer_all"]
        )
        if self.stop_event.is_set():
            return
        self.ctype.left_click()
        if self.stop_event.is_set():
            return
        self.ctype.press("escape")
        if not self.wait(1):
            return