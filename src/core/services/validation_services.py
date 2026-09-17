import logging
import time

import mss

from src.core.services.ctypes_services import CtypesServices


class ValidationServices:
    def __init__(self, stop_event):
        self.stop_event = stop_event
        self.ctype = CtypesServices()

    def wait_open(self, validation: dict, key, tolerance=3):

        x, y = validation["position"]
        aim_color = validation["color"]

        max_try = 3
        timeout = 15.0

        with mss.mss() as sct:
            for each_try in range(1, max_try + 1):
                if self.stop_event.is_set():
                    return False

                logging.info(f"verify open: {each_try}/{max_try}")  # noqa: LOG015

                start_time = time.time()

                while time.time() - start_time < timeout:
                    if self.stop_event.is_set():
                        return False

                    monitor = {"top": y, "left": x, "width": 1, "height": 1}

                    img = sct.grab(monitor)
                    pixel = img.pixel(0, 0)

                    if self.__nearby_colors(pixel, aim_color, tolerance):
                        logging.info("Pixel detectado. Inventário aberto.")  # noqa: LOG015
                        return True

                    # Espera cancelável
                    if self.stop_event.wait(0.05):
                        return False

                logging.warning("Timeout nessa tentativa.")  # noqa: LOG015

                if self.stop_event.is_set():
                    return False

                if each_try < max_try:
                    logging.info(f"Reapertando tecla: {key}")  # noqa: LOG015

                    self.ctype.press(key)

        raise TimeoutError("Falha ao abrir após 3 tentativas.")

    def is_pixel_color(self, validation: dict, tolerance=1):

        if self.stop_event.is_set():
            return False

        x, y = validation["position"]
        aim_color = validation["color"]

        with mss.mss() as sct:
            monitor = {"top": y, "left": x, "width": 1, "height": 1}

            img = sct.grab(monitor)
            pixel = img.pixel(0, 0)

            return self.__nearby_colors(pixel, aim_color, tolerance)

    def __nearby_colors(self, color, aim_color, tolerance=1):
        return all(abs(c - a) <= tolerance for c, a in zip(color, aim_color))
