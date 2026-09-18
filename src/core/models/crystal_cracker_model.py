from .base_model import BaseModel


class CrystalCrackerModel(BaseModel):
    def __init__(self, general_config, stop_event):
        super().__init__(general_config, stop_event)

    def crack_crystals(self):
        if self.stop_event.is_set():
            return
        self._open_crystal()
        if self.stop_event.is_set():
            return
        self.gt.centralize(*self.centralization_parameters)
        if self.stop_event.is_set():
            return
        self.gt.put_in_dedicated(self.pixel_per_degree)
        if self.stop_event.is_set():
            return
        self.gt.centralize(*self.centralization_parameters)

    def _open_crystal(self):
        key_list = [
            "one",
            "two",
            "three",
            "four",
            "five",
            "six",
            "seven",
            "eight",
            "nine",
            "zero",
        ]
        for key in key_list:
            if self.stop_event.is_set():
                return
            self.ctype.key_down(key)
        if not self.wait(6):
            return
        for key in key_list:
            if self.stop_event.is_set():
                return
            self.ctype.key_up(key)
        self.log("Crystals opened successfully.")
