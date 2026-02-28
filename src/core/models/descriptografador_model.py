import os
import logging
MAIN_KEY = "primesurvivor"

class ArquivoFaltando(Exception):
    pass

class ChaveInvalida(Exception):
    pass

class Descriptografador:
    
    def verificar_acesso(self):
        if not os.path.exists("key.enc"):
            logging.info("Arquivo de criptografia Faltando")
            raise ArquivoFaltando("Arquivo de criptografia Faltando")
        
        with open("key.enc", "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read()
        
        descriptografado = self.__descriptografar(conteudo)
        if descriptografado == "senha":
            logging.info("Senha Valida")
            return
        logging.info(f"Senha Invalida - {descriptografado}")
        raise ChaveInvalida(f"Senha Invalida")

    def __descriptografar(self, texto, chave=MAIN_KEY):
        resultado = ""
        for i in range(len(texto)):
            resultado += chr(ord(texto[i]) ^ ord(chave[i % len(chave)]))
        return resultado
