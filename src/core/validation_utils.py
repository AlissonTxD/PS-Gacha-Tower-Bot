from time import sleep
import time
import mss
import logging

from src.core.config import config
from src.core.ctypes_utils import CtypesUtils

class ValidationUtils:
    def __init__(self):
        self.ctype = CtypesUtils()

    def __nearby_colors(self, color, aim_color,  tolerance=1):
        return all(abs(c - a) <=  tolerance for c, a in zip(color, aim_color))


    def wait_open(self, x, y, aim_color, key, tolerance=3):
        max_try = 3
        timeout = 15.0

        with mss.mss() as sct:
            for each_try in range(1, max_try + 1):

                logging.info(f"verify open: {each_try}/{max_try}")

                start_time = time.time()

                while time.time() - start_time < timeout:
                    monitor = {
                        "top": y,
                        "left": x,
                        "width": 1,
                        "height": 1
                    }

                    img = sct.grab(monitor)
                    pixel = img.pixel(0, 0)

                    if self.__nearby_colors(pixel, aim_color, tolerance):
                        logging.info("Pixel detectado. Inventário aberto.")
                        return True

                    sleep(0.05)

                logging.warning("Timeout nessa tentativa.")
                if each_try < max_try:
                    logging.info(f"Reapertando tecla: {key}")
                    self.ctype.press(key)

        raise TimeoutError("Falha ao abrir após 3 tentativas.")
            

    def wait_close(self, x, y, aim_color, tolerance=1):
        with mss.mss() as sct:
            while True:
                monitor = {
                    "top": y,
                    "left": x,
                    "width": 1,
                    "height": 1
                }

                img = sct.grab(monitor)
                pixel = img.pixel(0, 0)
                print(pixel)

                if not self.__nearby_colors(pixel, aim_color, tolerance):
                    return True

                sleep(0.05)

    def is_pixel_color(self, x, y, aim_color, tolerance=1):
        with mss.mss() as sct:
            monitor = {
                "top": y,
                "left": x,
                "width": 1,
                "height": 1
            }

            img = sct.grab(monitor)
            pixel = img.pixel(0, 0)

            return self.__nearby_colors(pixel, aim_color, tolerance)
    
if __name__ == "__main__":
    pass