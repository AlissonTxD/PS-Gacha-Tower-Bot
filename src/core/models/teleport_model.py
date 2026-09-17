from time import sleep

from .base_model import BaseModel


class TeleportModel(BaseModel):
    def __init__(self, general_config, stop_event):
        super().__init__(general_config, stop_event)

    def teleport(self, tp_name: str):
        if self.stop_event.is_set():
            return
        self.gt.move_mouse_grau(0, -87, self.pixel_per_degree)
        if self.stop_event.is_set():
            return
        self.ctype.press("e")
        if self.stop_event.is_set():
            return
        self.validator.wait_open(self.configs["validation"]["teleport"], key="e")
        sleep(1)
        if self.stop_event.is_set():
            return
        self.ctype.move_mouse_absolute(*self.configs["teleport"]["search_map"])
        if self.stop_event.is_set():
            return
        self.ctype.left_click()
        if self.stop_event.is_set():
            return
        self.ctype.write_text(tp_name)
        sleep(0.1)
        if self.stop_event.is_set():
            return
        self.ctype.move_mouse_absolute(*self.configs["teleport"]["first_on_list"])
        if self.stop_event.is_set():
            return
        self.ctype.left_click()
        if self.stop_event.is_set():
            return
        self.ctype.move_mouse_absolute(*self.configs["teleport"]["teleport_button"])
        if self.stop_event.is_set():
            return
        self.ctype.left_click()
        sleep(2)
        if self.stop_event.is_set():
            return
        self.gt.move_mouse_grau(0, 80, self.pixel_per_degree)
        if self.stop_event.is_set():
            return
