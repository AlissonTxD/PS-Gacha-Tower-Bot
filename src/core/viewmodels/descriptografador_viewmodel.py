from src.core.models.descriptografador_model import Descriptografador,ArquivoFaltando,ChaveInvalida

class DescriptografadorViewModel:
    def __init__(self):
        self.descriptografador = Descriptografador()

    def descriptografar(self):
        try:
            self.descriptografador.verificar_acesso()
            return {"success": True}
        except ArquivoFaltando as e:
            return {"success": False, "erro": str(e)}
        except ChaveInvalida as e:
            return {"success": False, "erro": str(e)}
        