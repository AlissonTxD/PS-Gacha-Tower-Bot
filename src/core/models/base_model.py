from src.core.services.ctypes_services import CtypesServices
from src.core.services.gt_services import GtServices
from src.core.services.validation_services import ValidationServices


class BaseModel:
    def __init__(self, general_config: dict):
        print("base model started")
        self.ctype = CtypesServices()
        self.gt = GtServices()
        self.validator = ValidationServices()
        self.configs = general_config
        self.pixel_per_degree = self.configs["calibration"]["pixel_per_degree"]
        self.calibration = [self.configs["calibration"]["yaw"], 0, self.pixel_per_degree]