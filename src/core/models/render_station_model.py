from .base_model import BaseModel


class RenderStationModel(BaseModel):

    def __init__(self, general_config, stop_event):
        super().__init__(general_config, stop_event)

    def leave_bed(self):
        if self.stop_event.is_set():
            return
        self.ctype.press(key="e", hold=3)
        if not self.wait(1):
            return
        if self.stop_event.is_set():
            return
        self.gt.centralize(
            *self.centralization_parameters
        )
        if self.stop_event.is_set():
            return
        self.ctype.scroll_mouse("up", 3)
        self.log("Player left the bed successfully.")

    def join_bed(self):
        if self.stop_event.is_set():
            return
        self.gt.centralize(
            *self.centralization_parameters
        )
        if self.stop_event.is_set():
            return
        self.ctype.key_down("e")
        if not self.validator.wait_open(
            self.configs["validation"]["tek_bed_radial"],
            key="e"
        ):
            return
        if self.stop_event.is_set():
            return
        self.ctype.move_mouse_absolute(
            *self.configs["misc"]["lay_on"]
        )
        if self.stop_event.is_set():
            return
        self.ctype.left_click()
        self.log("Player joined the bed successfully.")
        if self.stop_event.is_set():
            return
        self.ctype.key_up("e")
        if self.stop_event.is_set():
            return
        self.ctype.press("v")
        if not self.validator.wait_open(
            self.configs["validation"]["inventory"],
            key="v"
        ):
            return
        self.log("Player inventory opened successfully.")
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
        self.ctype.press("escape")
        self.log("Player inventory droped and closed successfully.")
        if not self.wait(5):
            return