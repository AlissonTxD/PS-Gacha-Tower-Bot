from time import sleep

from .base_model import BaseModel


class CrystalCrackerModel(BaseModel):
    def __init__(self, general_config, stop_event):
        super().__init__(general_config, stop_event)

    def crack_crystals(self):
        self._open_crystal()
        self.gt.centralize(*self.centralization_parameters)
        self.gt.put_in_dedicated(self.pixel_per_degree)
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
            self.ctype.key_down(key)
        sleep(6)
        for key in key_list:
            self.ctype.key_up(key)
