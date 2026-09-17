from .base_model import BaseModel


class TrapModel(BaseModel):

    def __init__(self, general_config, stop_event):
        super().__init__(general_config, stop_event)

    def get_trap(self):
        if self.stop_event.is_set():
            return
        self.gt.centralize(
            *self.centralization_parameters
        )
        if self.stop_event.is_set():
            return
        self.__take__traps()

    def __take__traps(self):
        if self.stop_event.is_set():
            return
        self.ctype.press("f")
        if not self.validator.wait_open(
            self.configs["validation"]["inventory"],
            key="f"
        ):
            return
        if self.stop_event.is_set():
            return
        if not self.wait(0.1):
            return
        self.ctype.move_mouse_absolute(
            *self.configs["dino_inventory"]["search"]
        )
        if self.stop_event.is_set():
            return
        self.ctype.left_click()
        if self.stop_event.is_set():
            return
        self.ctype.write_text("trap")
        if self.stop_event.is_set():
            return
        self.ctype.move_mouse_absolute(
            *self.configs["dino_inventory"]["first_slot"]
        )
        if self.stop_event.is_set():
            return
        self.ctype.left_click()
        if self.stop_event.is_set():
            return

        for _ in range(150):
            if self.stop_event.is_set():
                return
            self.ctype.press("t")
        if self.stop_event.is_set():
            return
        self.ctype.press("escape")
        if not self.wait(1):
            return