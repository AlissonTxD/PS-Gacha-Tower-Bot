import os

from src.core.viewmodels.gacha_bot_viewmodel import GachaBotViewModel


class GachaBotView:
    def __init__(self):
        self.gachavm = GachaBotViewModel()

    def menu(self):

        while True:
            print("Menu do Bot de Gacha\n")
            print("1. Iniciar Bot Trap")
            print("2. Iniciar test de gachas")
            print("3. Sair")

            choice = input("Escolha uma opção: ")
            os.system("cls")
            match choice:
                case "1":
                    print("voce escolheu o 1 \n")
                case "2":
                    print("voce escolheu o 2 \n")
                case "3":
                    print("voce escolheu o 3 \n")
                    break
                case _:
                    print("Opção inválida, tente novamente.")
