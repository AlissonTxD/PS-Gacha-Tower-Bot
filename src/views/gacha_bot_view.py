import os

from src.core.viewmodels.gacha_bot_viewmodel import GachaBotViewModel


class GachaBotView:
    def __init__(self):
        self.gachavm = GachaBotViewModel()

    def menu(self):

        while True:
            os.system("cls")
            print("Menu do Bot de Gacha")
            print("1. Iniciar Bot Trap")
            print("2. Iniciar test de gachas")
            print("3. Sair")

            choice = input("Escolha uma opção: ")
            match choice:
                case "1":
                    print("1")
                case "2":
                    print("2")
                case "3":
                    print("3")
                case _:
                    print("Opção inválida, tente novamente.")
