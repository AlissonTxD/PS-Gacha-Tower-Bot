from functools import partial

from src.core.services.ctypes_services import CtypesServices
from src.core.services.gt_services import GtServices
from src.core.services.validation_services import ValidationServices


class BaseModel:
    def __init__(self, general_config: dict, stop_event):
        self.ctype = CtypesServices()
        self.gt = GtServices()
        self.validator = ValidationServices()
        self.configs = general_config
        self.stop_event = stop_event
        self.pixel_per_degree = self.configs["calibration"]["pixel_per_degree"]
        self.centralization_parameters = [
            self.configs["calibration"]["yaw"],
            0,
            self.pixel_per_degree,
        ]

    def open_inventory(self, key: str = "f") -> None:
        self.ctype.press(key)
        self.validator.wait_open(
            self.configs["validation"]["inventory"], key)
