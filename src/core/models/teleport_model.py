from time import sleep

from .base_model import BaseModel


class TeleportModel(BaseModel):
    def __init__(self, general_config):
        super().__init__(general_config)

    def teleport(self, tp_name: str):
        self.gt.move_mouse_grau(0, -87, self.pixel_per_degree)
        self.ctype.press("e")
        self.validator.wait_open(self.configs["validation"]["teleport"], key="e")
        sleep(1)
        self.ctype.move_mouse_absolute(*self.configs["teleport"]["search_map"])
        self.ctype.left_click()
        self.ctype.write_text(tp_name)
        sleep(0.1)
        self.ctype.move_mouse_absolute(*self.configs["teleport"]["first_on_list"])
        self.ctype.left_click()
        self.ctype.move_mouse_absolute(*self.configs["teleport"]["teleport_button"])
        self.ctype.left_click()
        sleep(2)
        self.gt.move_mouse_grau(0, 80, self.pixel_per_degree)
