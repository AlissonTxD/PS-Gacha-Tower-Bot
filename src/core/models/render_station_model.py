from time import sleep

from .base_model import BaseModel


class RenderStationModel(BaseModel):
    def __init__(self, general_config):
        super().__init__(general_config)

    def leave_bed_start(self):
        self.ctype.press(key="e", hold=3)
        sleep(1)
        self.gt.centralize(self.centralization_parameters)

    def join_bed_end(self):
        self.gt.centralize(self.centralization_parameters)
        self.ctype.key_down("e")
        self.validator.wait_open(
            *self.configs["validation"]["tek_bed_radial_validation"], key="e"
        )
        self.ctype.move_mouse_absolute(*self.configs["misc"]["lay_on"])
        self.ctype.left_click()
        self.ctype.key_up("e")
        self.ctype.press("v")
        self.validator.wait_open(
            *self.configs["validation"]["inventory_validation"], key="v"
        )
        self.ctype.move_mouse_absolute(*self.configs["player_inventory"]["drop_all"])
        self.ctype.left_click()
        self.ctype.press("escape")
        sleep(1)
