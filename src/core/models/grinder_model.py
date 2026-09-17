from .base_model import BaseModel


class GrinderModel(BaseModel):

    def __init__(self, general_config, stop_event):
        super().__init__(general_config, stop_event)

    def grind_items(self):

        if self.stop_event.is_set():
            return

        self.gt.move_mouse_grau(
            90, 0, self.pixel_per_degree
        )

        if self.stop_event.is_set():
            return

        self.__place_in_vault(["gate"])

        if self.stop_event.is_set():
            return

        self.gt.move_mouse_grau(
            -180, 0, self.pixel_per_degree
        )

        if self.stop_event.is_set():
            return

        self.open_inventory()

        if self.stop_event.is_set():
            return

        self.ctype.move_mouse_absolute(
            *self.configs["player_inventory"]["transfer_all"]
        )

        if self.stop_event.is_set():
            return

        self.ctype.left_click()

        if not self.wait(0.5):
            return

        self.ctype.move_mouse_absolute(
            *self.configs["misc"]["grind_all"]
        )

        if self.stop_event.is_set():
            return

        self.ctype.left_click()

        if self.stop_event.is_set():
            return

        self.ctype.move_mouse_absolute(
            *self.configs["dino_inventory"]["transfer_all"]
        )

        if self.stop_event.is_set():
            return

        self.ctype.left_click()

        if self.stop_event.is_set():
            return

        self.ctype.press("escape")

        if not self.wait(1):
            return

        self.gt.centralize(
            *self.centralization_parameters
        )

        if self.stop_event.is_set():
            return

        self.gt.put_in_dedicated(
            self.pixel_per_degree
        )

        if self.stop_event.is_set():
            return

        self.gt.centralize(
            *self.centralization_parameters
        )

    def __place_in_vault(self, list_of_items):

        if self.stop_event.is_set():
            return

        self.open_inventory()

        if self.stop_event.is_set():
            return

        if not self.wait(1):
            return

        if self.stop_event.is_set():
            return

        if not self.validator.is_pixel_color(
            self.configs["validation"]["vault_full"]
        ):
            for item in list_of_items:

                if self.stop_event.is_set():
                    return

                self.ctype.move_mouse_absolute(
                    *self.configs["player_inventory"]["search"]
                )

                if self.stop_event.is_set():
                    return

                self.ctype.left_click()

                if self.stop_event.is_set():
                    return

                self.ctype.write_text(item)

                if self.stop_event.is_set():
                    return

                self.ctype.move_mouse_absolute(
                    *self.configs["player_inventory"]["transfer_all"]
                )

                if self.stop_event.is_set():
                    return

                self.ctype.left_click()

        if self.stop_event.is_set():
            return

        self.ctype.press("escape")

        if not self.wait(1):
            return