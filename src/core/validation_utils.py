from time import sleep
import mss

from src.core.config import config
from src.core.ctypes_utils import CtypesUtils

class ValidationUtils:

    def __nearby_colors(self, color, aim_color,  tolerance=1):
        return all(abs(c - a) <=  tolerance for c, a in zip(color, aim_color))


    def wait_open(self, x, y, aim_color, tolerance=1):
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

                if self.__nearby_colors(pixel, aim_color,  tolerance):
                    return True
                sleep(0.05)

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