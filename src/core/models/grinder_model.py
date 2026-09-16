from time import sleep

from .base_model import BaseModel


class GrinderModel(BaseModel):
    def __init__(self, general_config):
        super().__init__(general_config)

    def grind_items(self):
        self.gt.move_mouse_grau(90, 0, self.pixel_per_degree)
        self.__place_in_vault(["gate"])
        self.gt.move_mouse_grau(-180, 0, self.pixel_per_degree)
        self.open_inventory()
        self.ctype.move_mouse_absolute(*self.configs["player_inventory"]["transfer_all"])
        self.ctype.left_click()
        sleep(0.5)
        self.ctype.move_mouse_absolute(*self.configs["misc"]["grind_all"])
        self.ctype.left_click()
        self.ctype.move_mouse_absolute(*self.configs["dino_inventory"]["transfer_all"])
        self.ctype.left_click()
        self.ctype.press("escape")
        sleep(1)
        self.gt.centralize(*self.centralization_parameters)
        self.gt.put_in_dedicated(self.pixel_per_degree)
        self.gt.centralize(*self.centralization_parameters)

    def __place_in_vault(self, list_of_items):
        self.open_inventory()
        sleep(1)
        if not self.validator.is_pixel_color(self.configs["validation"]["vault_full"]):
            for item in list_of_items:
                self.ctype.move_mouse_absolute(*self.configs["player_inventory"]["search"])
                self.ctype.left_click()
                self.ctype.write_text(item)
                self.ctype.move_mouse_absolute(*self.configs["player_inventory"]["transfer_all"])
                self.ctype.left_click()
        self.ctype.press("escape")
        sleep(1)