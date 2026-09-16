import logging
from time import sleep, time

from pyperclip import copy, paste

from src.core.services.ctypes_services import CtypesServices


class GtServices:
    def __init__(self):
        self.ctype = CtypesServices()

    def move_mouse_grau(
        self, diff_yaw: float, diff_pitch: float, pixels_per_degree: float
    ) -> None:
        """
        Move the mouse by the specified yaw and pitch differences
        Args:
            diff_yaw (float): difference in yaw
            diff_pitch (float): difference in pitch
            pixels_per_degree (float): pixels per degree
        """
        pixels_x = int(diff_yaw * pixels_per_degree)
        pixels_y = int(-diff_pitch * pixels_per_degree)
        self.ctype.move_mouse_relative(pixels_x, pixels_y)

    def centralize(
        self, yaw_base: float, pitch_base: float, pixels_per_degree: float
    ) -> None:
        """
        Centralize the mouse to the target yaw and pitch
        Args:
            yaw_base (float): target yaw
            pitch_base (float): target pitch
            pixels_per_degree (float): pixels per degree
        """
        self.__ccc()
        yaw_atual, pitch_atual = self.__take_yall_pitch_from_clipboard()
        diff_yaw = self.__calculate_best_path(yaw_base, yaw_atual)
        diff_pitch = pitch_base - pitch_atual
        pixels_x = int(diff_yaw * pixels_per_degree)
        pixels_y = int(-diff_pitch * pixels_per_degree)
        self.ctype.move_mouse_relative(pixels_x, pixels_y)

    def put_in_dedicated(self, pixel_per_degree: float) -> None:
        """
        Move trought the dedicates 2x4 and press "e" to deposit the resources
        Args:
            pixel_per_degree (float): pixel per degree config
        """
        self.move_mouse_grau(15, 60, pixel_per_degree)
        self.ctype.press("e")
        self.move_mouse_grau(0, -30, pixel_per_degree)
        self.ctype.press("e")
        for _ in range(2):
            self.move_mouse_grau(0, -40, pixel_per_degree)
            self.ctype.press("e")
        self.move_mouse_grau(-30, 0, pixel_per_degree)
        self.ctype.press("e")
        for _ in range(2):
            self.move_mouse_grau(0, 40, pixel_per_degree)
            self.ctype.press("e")
        self.move_mouse_grau(0, 30, pixel_per_degree)
        self.ctype.press("e")

    def __calculate_best_path(self, target: int, current: int) -> int:
        """
        Calculate the best path to move from current to target angle, considering the circular nature of angles.
        Args:
            target (int): target angle
            current (int): current angle
        Returns:
            int: the best path to move from current to target
        """
        return ((target - current + 180) % 360) - 180

    def __take_yall_pitch_from_clipboard(self) -> tuple[float, float]:
        """
        Take the yaw and pitch values from the clipboard.
        Returns:
            tuple[float, float]: yaw and pitch values
        """
        texto = paste()
        partes = texto.strip().split()

        if len(partes) < 5:
            raise ValueError("CCC inválido")

        yaw = float(partes[3])
        pitch = float(partes[4])
        return yaw, pitch

    def __ccc(self, max_tentativas: int = 3, timeout: float = 5.0) -> None:
        """
        Send the CCC command and wait for a valid response in the clipboard.
        Args:
            max_tentativas (int): maximum number of attempts
            timeout (float): timeout for each attempt
        Raises:
            TimeoutError: if no valid response is received after max_tentativas
        """
        for tentativa in range(1, max_tentativas + 1):
            logging.info(f"Tentativa CCC {tentativa}/{max_tentativas}")  # noqa: LOG015
            copy("")
            self.ctype.press("tab")
            sleep(0.3)
            self.ctype.write_text("CCC")
            sleep(0.3)
            self.ctype.press("enter")
            inicio = time()
            while time() - inicio < timeout:
                sleep(0.1)
                try:
                    yaw, pitch = self.__take_yall_pitch_from_clipboard()
                    if yaw is not None and pitch is not None:
                        return
                except Exception as e:  # noqa: BLE001
                    logging.warning(  # noqa: LOG015
                        f"Erro ao obter valores do CCC na tentativa {tentativa}: {e}"
                    )
                    continue
            logging.warning("Timeout ao esperar resposta do CCC.")  # noqa: LOG015
        raise TimeoutError("Falha ao obter resposta válida do CCC após 3 tentativas.")

    def record_replay(self):
        self.ctype.key_down("leftalt")
        sleep(0.5)
        self.ctype.key_down("f10")
        sleep(0.5)
        self.ctype.key_up("f10")
        self.ctype.key_up("leftalt")

if __name__ == "__main__":
    print("test")
