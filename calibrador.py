import ctypes
import time
import pyperclip


# ============================================================
# CONFIGURAÇÃO
# ============================================================

PIXELS_TESTE = 100

user32 = ctypes.windll.user32

INPUT_MOUSE = 0
INPUT_KEYBOARD = 1

KEYEVENTF_KEYUP = 0x0002

VK_TAB = 0x09
VK_ENTER = 0x0D

MOUSEEVENTF_MOVE = 0x0001


# ============================================================
# ESTRUTURAS DO WINDOWS
# ============================================================

class KEYBDINPUT(ctypes.Structure):
    _fields_ = [
        ("wVk", ctypes.c_ushort),
        ("wScan", ctypes.c_ushort),
        ("dwFlags", ctypes.c_ulong),
        ("time", ctypes.c_ulong),
        ("dwExtraInfo", ctypes.POINTER(ctypes.c_ulong))
    ]


class MOUSEINPUT(ctypes.Structure):
    _fields_ = [
        ("dx", ctypes.c_long),
        ("dy", ctypes.c_long),
        ("mouseData", ctypes.c_ulong),
        ("dwFlags", ctypes.c_ulong),
        ("time", ctypes.c_ulong),
        ("dwExtraInfo", ctypes.POINTER(ctypes.c_ulong))
    ]


class INPUT_UNION(ctypes.Union):
    _fields_ = [
        ("ki", KEYBDINPUT),
        ("mi", MOUSEINPUT)
    ]


class INPUT(ctypes.Structure):
    _anonymous_ = ("u",)

    _fields_ = [
        ("type", ctypes.c_ulong),
        ("u", INPUT_UNION)
    ]


# ============================================================
# TECLADO
# ============================================================

def press_key(vk):
    extra = ctypes.c_ulong(0)

    inp = INPUT(
        type=INPUT_KEYBOARD,
        ki=KEYBDINPUT(
            wVk=vk,
            wScan=0,
            dwFlags=0,
            time=0,
            dwExtraInfo=ctypes.pointer(extra)
        )
    )

    user32.SendInput(
        1,
        ctypes.byref(inp),
        ctypes.sizeof(INPUT)
    )

    time.sleep(0.05)

    inp.ki.dwFlags = KEYEVENTF_KEYUP

    user32.SendInput(
        1,
        ctypes.byref(inp),
        ctypes.sizeof(INPUT)
    )


def write_text(text):
    for char in text:

        vk = ord(char.upper())

        extra = ctypes.c_ulong(0)

        inp = INPUT(
            type=INPUT_KEYBOARD,
            ki=KEYBDINPUT(
                wVk=vk,
                wScan=0,
                dwFlags=0,
                time=0,
                dwExtraInfo=ctypes.pointer(extra)
            )
        )

        user32.SendInput(
            1,
            ctypes.byref(inp),
            ctypes.sizeof(INPUT)
        )

        time.sleep(0.03)

        inp.ki.dwFlags = KEYEVENTF_KEYUP

        user32.SendInput(
            1,
            ctypes.byref(inp),
            ctypes.sizeof(INPUT)
        )


# ============================================================
# MOUSE
# ============================================================

def move_mouse_relative(x, y):

    extra = ctypes.c_ulong(0)

    inp = INPUT(
        type=INPUT_MOUSE,
        mi=MOUSEINPUT(
            dx=x,
            dy=y,
            mouseData=0,
            dwFlags=MOUSEEVENTF_MOVE,
            time=0,
            dwExtraInfo=ctypes.pointer(extra)
        )
    )

    user32.SendInput(
        1,
        ctypes.byref(inp),
        ctypes.sizeof(INPUT)
    )


# ============================================================
# CCC
# ============================================================

def executar_ccc():

    # Limpa o clipboard
    pyperclip.copy("")

    # Abre console
    press_key(VK_TAB)

    time.sleep(0.3)

    # Digita CCC
    write_text("CCC")

    time.sleep(0.3)

    # Executa
    press_key(VK_ENTER)

    # Espera o ARK atualizar o clipboard
    inicio = time.time()

    while time.time() - inicio < 5:

        time.sleep(0.2)

        try:

            texto = pyperclip.paste()

            partes = texto.strip().split()

            if len(partes) >= 5:

                yaw = float(partes[3])
                pitch = float(partes[4])

                return yaw, pitch

        except Exception:
            pass

    raise TimeoutError("Falha ao obter resposta do CCC.")


# ============================================================
# CALIBRAÇÃO
# ============================================================

def calibrar():

    print()
    print("======================================")
    print("       CALIBRADOR PIXEL / GRAU")
    print("======================================")
    print()
    print("Deixe o ARK focado.")
    print("Começando em 3 segundos...")
    print()

    time.sleep(3)

    # --------------------------------
    # PRIMEIRO CCC
    # --------------------------------

    print("Executando primeiro CCC...")

    yaw1, pitch1 = executar_ccc()

    print(f"Yaw inicial : {yaw1:.2f}")
    print(f"Pitch       : {pitch1:.2f}")

    time.sleep(0.5)

    # --------------------------------
    # MOVE PARA ESQUERDA
    # --------------------------------

    print()
    print(f"Movendo {PIXELS_TESTE} pixels para esquerda...")

    move_mouse_relative(-PIXELS_TESTE, 0)

    time.sleep(0.5)

    # --------------------------------
    # SEGUNDO CCC
    # --------------------------------

    print("Executando segundo CCC...")

    yaw2, pitch2 = executar_ccc()

    print(f"Yaw final   : {yaw2:.2f}")
    print(f"Pitch       : {pitch2:.2f}")

    # --------------------------------
    # CALCULO
    # --------------------------------

    diferenca_yaw = abs(yaw1 - yaw2)

    if diferenca_yaw <= 0:
        raise ValueError("O yaw não mudou.")

    pixels_por_grau = PIXELS_TESTE / diferenca_yaw

    graus_por_pixel = diferenca_yaw / PIXELS_TESTE

    # --------------------------------
    # RESULTADO
    # --------------------------------

    print()
    print("======================================")
    print("              RESULTADO")
    print("======================================")

    print(f"Yaw inicial     : {yaw1:.2f}°")
    print(f"Yaw final       : {yaw2:.2f}°")
    print(f"Diferença       : {diferenca_yaw:.4f}°")
    print()
    print(f"Pixels por grau : {pixels_por_grau:.6f}")
    print(f"Graus por pixel : {graus_por_pixel:.6f}")

    print("======================================")
    print()


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":

    try:

        calibrar()

    except Exception as e:

        print()
        print("ERRO:")
        print(e)