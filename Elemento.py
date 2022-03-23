class Elemento:
    def __init__(self, valor, anterior=None, proximo=None):
        self.__anterior = anterior
        self.__proximo = proximo
        self.__valor = valor

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, novo_valor: int):
        self.__valor = novo_valor

    @property
    def proximo(self):
        return self.__proximo

    @proximo.setter
    def proximo(self, novo_proximo):
        self.__proximo = novo_proximo

    @property
    def anterior(self):
        return self.__anterior

    @anterior.setter
    def anterior(self, novo_anterior):
        self.__anterior = novo_anterior