from src.core.viewmodels.gacha_bot_viewmodel import GachaBotViewModel

class GachaBotView:

    def __init__(self):
        self.gachavm = GachaBotViewModel()

    def menu(self):

        while True:
            print("Menu do Bot de Gacha")
            print("1. Iniciar Bot")
            print("2. Sair")
            choice = input("Escolha uma opção: ")
            match choice:
                case "1":
                    print("Iniciando o Bot de Gacha...")
                    self.gachavm.start()
                case "2":
                    break
                case _:
                    print("Opção inválida, tente novamente.")
