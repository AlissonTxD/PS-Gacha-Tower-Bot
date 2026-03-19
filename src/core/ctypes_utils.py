import ctypes
import logging
import time
import pyperclip
from typing import Dict


PUL = ctypes.POINTER(ctypes.c_ulong)


class MOUSEINPUT(ctypes.Structure):
    _fields_ = [
        ("dx", ctypes.c_long),
        ("dy", ctypes.c_long),
        ("mouseData", ctypes.c_ulong),
        ("dwFlags", ctypes.c_ulong),
        ("time", ctypes.c_ulong),
        ("dwExtraInfo", PUL),
    ]


class KEYBDINPUT(ctypes.Structure):
    _fields_ = [
        ("wVk", ctypes.c_ushort),
        ("wScan", ctypes.c_ushort),
        ("dwFlags", ctypes.c_ulong),
        ("time", ctypes.c_ulong),
        ("dwExtraInfo", PUL),
    ]


class INPUTUNION(ctypes.Union):
    _fields_ = [
        ("mi", MOUSEINPUT),
        ("ki", KEYBDINPUT),
    ]


class INPUT(ctypes.Structure):
    _fields_ = [
        ("type", ctypes.c_ulong),
        ("union", INPUTUNION),
    ]


class CtypesUtils:
    INPUT_MOUSE = 0
    INPUT_KEYBOARD = 1

    MOUSEEVENTF_MOVE = 0x0001
    MOUSEEVENTF_LEFTDOWN = 0x0002
    MOUSEEVENTF_LEFTUP = 0x0004
    MOUSEEVENTF_RIGHTDOWN = 0x0008
    MOUSEEVENTF_RIGHTUP = 0x0010
    MOUSEEVENTF_ABSOLUTE = 0x8000

    KEYEVENTF_KEYUP = 0x0002

    SM_CXSCREEN = 0
    SM_CYSCREEN = 1

    DEFAULT_KEYMAP: Dict[str, int] = {
        "tab": 0x09,
        "escape": 0x1B,
        "return": 0x0D,
        "enter": 0x0D,
        "leftcontrol": 0xA2,
        "leftshift": 0xA0,
        "leftalt": 0xA4,
        "rightalt": 0xA5,
        "spacebar": 0x20,
        "hyphen": 0xBD,
        "tilde": 0xC0,
        "backspace": 0x08,
        "zero": 0x30,
        "one": 0x31,
        "two": 0x32,
        "three": 0x33,
        "four": 0x34,
        "five": 0x35,
        "six": 0x36,
        "seven": 0x37,
        "eight": 0x38,
        "nine": 0x39,
        "thumbmousebutton": 0x05,
        "thumbmousebutton2": 0x06,
        "a": 0x41,
        "b": 0x42,
        "c": 0x43,
        "d": 0x44,
        "e": 0x45,
        "f": 0x46,
        "g": 0x47,
        "h": 0x48,
        "i": 0x49,
        "j": 0x4A,
        "k": 0x4B,
        "l": 0x4C,
        "m": 0x4D,
        "n": 0x4E,
        "o": 0x4F,
        "p": 0x50,
        "q": 0x51,
        "r": 0x52,
        "s": 0x53,
        "t": 0x54,
        "u": 0x55,
        "v": 0x56,
        "w": 0x57,
        "x": 0x58,
        "y": 0x59,
        "z": 0x5A,
        "f1": 0x70,
        "f2": 0x71,
        "f3": 0x72,
        "f4": 0x73,
        "f5": 0x74,
        "f6": 0x75,
        "f7": 0x76,
        "f8": 0x77,
        "f9": 0x78,
        "f10": 0x79,
        "f11": 0x7A,
        "f12": 0x7B,
    }

    def __init__(self, keymap: Dict[str, int] | None = None) -> None:
        self.yaw_dict = {
            "yaw_left": 136.32,
            "yaw_right": 137.36,
            "yaw_meio": 134.57
        }
        self.user32 = ctypes.windll.user32
        self.keymap = dict(self.DEFAULT_KEYMAP)
        if keymap:
            self.keymap.update({k.lower(): v for k, v in keymap.items()})

    def add_key(self, name: str, vk_code: int) -> None:
        self.keymap[name.lower()] = vk_code

    def _send_input(self, inp: INPUT) -> None:
        self.user32.SendInput(1, ctypes.byref(inp), ctypes.sizeof(INPUT))

    def _send_key_vk(self, vk: int, keyup: bool = False) -> None:
        extra = ctypes.c_ulong(0)
        flags = self.KEYEVENTF_KEYUP if keyup else 0
        inp = INPUT(
            type=self.INPUT_KEYBOARD,
            union=INPUTUNION(
                ki=KEYBDINPUT(vk, 0, flags, 0, ctypes.pointer(extra))
            ),
        )
        self._send_input(inp)

    def _send_mouse(self, dx: int, dy: int, flags: int) -> None:
        extra = ctypes.c_ulong(0)
        inp = INPUT(
            type=self.INPUT_MOUSE,
            union=INPUTUNION(
                mi=MOUSEINPUT(dx, dy, 0, flags, 0, ctypes.pointer(extra))
            ),
        )
        self._send_input(inp)

    def key_down(self, key: str) -> None:
        vk = self.keymap[key.lower()]
        self._send_key_vk(vk, keyup=False)

    def key_up(self, key: str) -> None:
        vk = self.keymap[key.lower()]
        self._send_key_vk(vk, keyup=True)

    def press(self, key: str, hold: float = 0.02) -> None:
        self.key_down(key)
        time.sleep(hold)
        self.key_up(key)

    def combo(self, *keys: str, hold: float = 0.02) -> None:
        if not keys:
            return
        for key in keys:
            self.key_down(key)
        time.sleep(hold)
        for key in reversed(keys):
            self.key_up(key)

    def write_text(self, text: str, interval: float = 0.02) -> None:
        digit_names = [
            "zero",
            "one",
            "two",
            "three",
            "four",
            "five",
            "six",
            "seven",
            "eight",
            "nine",
        ]

        for ch in text:
            if ch == " ":
                self.press("spacebar")
            elif ch.isdigit():
                self.press(digit_names[int(ch)])
            elif ch.isalpha():
                self.press(ch.lower())
            elif ch == "-":
                self.press("hyphen")
            elif ch == "~":
                self.press("tilde")
            time.sleep(interval)

    def move_mouse_relative(self, dx: int, dy: int) -> None:
        self._send_mouse(dx, dy, self.MOUSEEVENTF_MOVE)
        time.sleep(0.5)

    def move_mouse_absolute(self, x: int, y: int, deley: float = 0.5) -> None:
        screen_w = self.user32.GetSystemMetrics(self.SM_CXSCREEN) - 1
        screen_h = self.user32.GetSystemMetrics(self.SM_CYSCREEN) - 1

        abs_x = int(x * 65535 / max(screen_w, 1))
        abs_y = int(y * 65535 / max(screen_h, 1))

        self._send_mouse(abs_x, abs_y, self.MOUSEEVENTF_MOVE | self.MOUSEEVENTF_ABSOLUTE)
        time.sleep(deley)

    def set_cursor_pos(self, x: int, y: int) -> None:
        self.user32.SetCursorPos(int(x), int(y))

    def left_click(self) -> None:
        self._send_mouse(0, 0, self.MOUSEEVENTF_LEFTDOWN)
        self._send_mouse(0, 0, self.MOUSEEVENTF_LEFTUP)
        time.sleep(0.1)

    def right_click(self) -> None:
        self._send_mouse(0, 0, self.MOUSEEVENTF_RIGHTDOWN)
        self._send_mouse(0, 0, self.MOUSEEVENTF_RIGHTUP)
        time.sleep(0.1)

    def calculate_best_path(self, target: int, current: int) -> int:
        return ((target - current + 180) % 360) - 180
    
    def take_yall_pitch_from_clipboard(self):
        texto = pyperclip.paste()
        partes = texto.strip().split()

        if len(partes) < 5:
            raise ValueError("CCC inválido")

        yaw = float(partes[3])
        pitch = float(partes[4])
        return yaw, pitch
    

    def ccc(self, max_tentativas: int = 3, timeout: float = 5.0) -> None:

        for tentativa in range(1, max_tentativas + 1):

            logging.info(f"Tentativa CCC {tentativa}/{max_tentativas}")
            pyperclip.copy("")
            self.press("tab")
            time.sleep(0.3)
            self.write_text("CCC")
            time.sleep(0.3)
            self.press("enter")
            inicio = time.time()
            while time.time() - inicio < timeout:

                time.sleep(0.5)
                try:

                    yaw, pitch = self.take_yall_pitch_from_clipboard()
                    return
                except Exception:

                    continue
            logging.warning("Timeout ao esperar resposta do CCC.")
        raise TimeoutError("Falha ao obter resposta válida do CCC após 3 tentativas.")

    def centralize(self, yaw_base: float, pitch_base: float, pixels_per_degree: float) -> None:

        self.ccc()
        time.sleep(1)
        yaw_atual, pitch_atual = self.take_yall_pitch_from_clipboard()
        diff_yaw = self.calculate_best_path(yaw_base, yaw_atual)
        diff_pitch = pitch_base - pitch_atual
        pixels_x = int(diff_yaw * pixels_per_degree)
        pixels_y = int(-diff_pitch * pixels_per_degree)
        self.move_mouse_relative(pixels_x, pixels_y)
    
    def move_mouse_grau(self, diff_yaw: float, diff_pitch: float, pixels_per_degree: float) -> None:
        pixels_x = int(diff_yaw * pixels_per_degree)
        pixels_y = int(-diff_pitch * pixels_per_degree)
        self.move_mouse_relative(pixels_x, pixels_y)
        time.sleep(0.5)