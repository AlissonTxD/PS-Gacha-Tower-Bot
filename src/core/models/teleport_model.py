from .base_model import BaseModel


class TeleportModel(BaseModel):
    def __init__(self, general_config, stop_event):
        super().__init__(general_config, stop_event)

    def teleport(self, tp_name: str):
        self.log(f"Teleporting to {tp_name}...")
        if self.stop_event.is_set():
            return
        self.gt.move_mouse_grau(0, -87, self.pixel_per_degree)
        if self.stop_event.is_set():
            return
        self.ctype.press("e")
        if self.stop_event.is_set():
            return
        if not self.validator.wait_open(
            self.configs["validation"]["teleport"], key="e"
        ):
            return
        self.log("teleport HUD open successful")
        if not self.wait(1):
            return
        self.ctype.move_mouse_absolute(*self.configs["teleport"]["search_map"])
        if self.stop_event.is_set():
            return
        self.ctype.left_click()
        if self.stop_event.is_set():
            return
        self.ctype.write_text(tp_name)
        if not self.wait(0.1):
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
        if not self.wait(1):
            return
        self.gt.move_mouse_grau(0, 80, self.pixel_per_degree)
        self.log(f"Teleport to {tp_name} complete")
