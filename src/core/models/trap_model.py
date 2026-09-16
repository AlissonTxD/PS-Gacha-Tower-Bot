from time import sleep

from .base_model import BaseModel


class TrapModel(BaseModel):
    def __init__(self, general_config):
        super().__init__(general_config)

    def get_trap(self):
        self.gt.centralize(*self.centralization_parameters)
        self.__take__traps()

    def __take__traps(self):
        self.ctype.press("f")
        self.validator.wait_open(self.configs["validation"]["inventory"], key="f")
        sleep(0.1)
        self.ctype.move_mouse_absolute(*self.configs["dino_inventory"]["search"])
        self.ctype.left_click()
        self.ctype.write_text("trap")
        self.ctype.move_mouse_absolute(*self.configs["dino_inventory"]["first_slot"])
        self.ctype.left_click()
        for _ in range(150):
            self.ctype.press("t")
        self.ctype.press("escape")
        sleep(1)
