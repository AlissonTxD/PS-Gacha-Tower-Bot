import time
import mss
import tkinter as tk
from tkinter import messagebox


def cor_proxima(cor, alvo, tolerancia=10):
    return all(abs(c - a) <= tolerancia for c, a in zip(cor, alvo))


def esperar_pixel_infinito(x, y, cor_alvo, tolerancia=10):
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

            if cor_proxima(pixel, cor_alvo, tolerancia):
                return True

            time.sleep(0.05)
            

# ===== TESTE =====
if __name__ == "__main__":
    X = 42
    Y = 53
    COR_ALVO = (220, 220, 223)

    print("Esperando pixel aparecer...")

    esperar_pixel_infinito(X, Y, COR_ALVO)

    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("Detectado!", "Pixel encontrado!")
    root.destroy()