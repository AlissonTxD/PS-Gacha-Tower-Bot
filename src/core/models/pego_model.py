from .base_model import BaseModel


class PegoModel(BaseModel):

    def __init__(self, general_config, stop_event):
        super().__init__(general_config, stop_event)

    def collect_crystals(self) -> None:
        if self.stop_event.is_set():
            return
        self.gt.move_mouse_grau(
            0, 10, self.pixel_per_degree
        )
        if self.stop_event.is_set():
            return
        self.open_inventory()
        if self.stop_event.is_set():
            return
        self.ctype.move_mouse_absolute(
            *self.configs["player_inventory"]["drop_all"]
        )
        if self.stop_event.is_set():
            return
        self.ctype.left_click()
        if self.stop_event.is_set():
            return
        self.ctype.move_mouse_absolute(
            *self.configs["dino_inventory"]["transfer_all"]
        )
        if self.stop_event.is_set():
            return
        self.ctype.left_click()
        if self.stop_event.is_set():
            return
        self.ctype.press("escape")
        if not self.wait(1):
            return
        if self.stop_event.is_set():
            return
        self.gt.move_mouse_grau(
            0, -10, self.pixel_per_degree
        )