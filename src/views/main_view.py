from src.core.viewmodels.descriptografador_viewmodel import DescriptografadorViewModel


class View:
    
    def __init__(self):

        descrip = DescriptografadorViewModel()
        resposta = descrip.descriptografar()

        if resposta["success"]:
            print("Acesso Liberado")
        else:
            print(f"Erro {resposta["erro"]}")