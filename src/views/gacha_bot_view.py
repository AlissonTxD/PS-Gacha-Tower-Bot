from src.core.viewmodels.gacha_bot_viewmodel import GachaBotViewModel

class GachaBotView:

    def __init__(self):
        self.gachavm = GachaBotViewModel()

    def menu(self):

        while True:
            print("Menu do Bot de Gacha")
            print("nao esquece\ngamma 3, ini e base, inventory weight- asc")
            print("1. Iniciar Bot - First time")
            print("2. Inicial Bot - Feed Normal")
            print("3. Iniciar test de gachas")
            print("4. Sair")
            choice = input("Escolha uma opção: ")
            match choice:
                case "1":
                    print("Iniciando o Bot de Gacha...")
                    self.gachavm.start()
                case "2":
                    print("Iniciando o Bot de Gacha - Feed normal")
                    self.gachavm.start("normal")
                case "3":
                    print("Iniciando Test de Gachas")
                    self.gachavm.test_gachas()
                case "4":
                    break
                case _:
                    print("Opção inválida, tente novamente.")
