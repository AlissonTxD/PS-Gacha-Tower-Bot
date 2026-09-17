from time import sleep

from .base_model import BaseModel


class RenderStationModel(BaseModel):
    def __init__(self, general_config, stop_event):
        super().__init__(general_config, stop_event)

    def leave_bed(self):
        self.ctype.press(key="e", hold=3)
        sleep(1)
        self.gt.centralize(*self.centralization_parameters)
        self.ctype.scroll_mouse("up", 3)

    def join_bed(self):
        self.gt.centralize(*self.centralization_parameters)
        self.ctype.key_down("e")
        if not self.validator.wait_open(self.configs["validation"]["tek_bed_radial"], key="e"): return
        self.ctype.move_mouse_absolute(*self.configs["misc"]["lay_on"])
        self.ctype.left_click()
        self.ctype.key_up("e")
        self.ctype.press("v")
        if not self.validator.wait_open(self.configs["validation"]["inventory"], key="v"):return
        self.ctype.move_mouse_absolute(*self.configs["player_inventory"]["drop_all"])
        self.ctype.left_click()
        self.ctype.press("escape")
        sleep(5)
