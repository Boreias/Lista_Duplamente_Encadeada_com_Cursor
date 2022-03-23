from Elemento import Elemento

class Lista:
    def __init__(self, tamanho_maximo):
        self.__inicio = Elemento(None)
        self.__fim = Elemento(None)
        self.__inicio.proximo = self.__fim
        self.__fim.anterior = self.__inicio
        self.__cursor = None
        self.__tamanho_maximo = tamanho_maximo
        self.__quantidade_atual = 0

    def __listanaoVazia(self):
        if self.__cursor != None:
            return True
        else:
            print('A lista esta vazia')
            return False

    def acessarAtual(self):
        if self.__listanaoVazia():
            return self.__cursor

    def __irParaPrimeiro(self):
        if self.__listanaoVazia():
            self.__cursor = self.__inicio.proximo

    def __irParaUltimo(self):
        if self.__listanaoVazia():
            self.__cursor = self.__fim.anterior

    def __avancarKPosicoes(self, k):
        for i in range(k):
            if self.__cursor.proximo != self.__fim:
                self.__cursor = self.__cursor.proximo
            else:
                print('Valor de avanco maior que a lista, o cursor esta no ultimo elemento')
                break

    def __retrocederKPosicoes(self, k):
        for i in range(k):
            if self.__cursor.anterior != self.__inicio:
                self.__cursor = self.__cursor.anterior
            else:
                print('Valor de retrocesso maior que a lista, o cursor esta no primeiro elemento')
                break

    def Vazia(self):
        return self.__quantidade_atual == 0

    def Cheia(self):
        return self.__quantidade_atual >= self.__tamanho_maximo

    def posicaoDe(self, chave):
        self.__irParaPrimeiro()
        for i in range(1, self.__quantidade_atual):
            if self.__cursor.valor == chave:
                return i
            else:
                self.__cursor = self.__cursor.proximo
        else:
            print('Chave nao encontrada')
            #self.__cursor = self.__inicio.proximo

    def Buscar(self, chave):
        self.__irParaPrimeiro()
        for i in range(1, self.__quantidade_atual):
            if self.__cursor.valor == chave:
                return True
            else:
                self.__cursor = self.__cursor.proximo
        else:
            print('Chave nao encontrada')
            return False

    def InserirAntesDoAtual(self, novo):
        if self.__listanaoVazia() and not self.Cheia():
            elemento = Elemento(novo, self.__cursor.anterior, self.__cursor.proximo)
            self.__cursor.anterior.proximo = elemento
            self.__cursor.proximo.anterior = elemento
            self.__cursor = elemento
            self.__quantidade_atual += 1

    def InserirAposAtual(self, novo):
        if self.__listanaoVazia() and not self.Cheia():
            elemento = Elemento(novo, self.__cursor, self.__cursor.proximo)
            self.__cursor.proximo.anterior = elemento
            self.__cursor.proximo = elemento
            self.__cursor = elemento
            self.__quantidade_atual += 1

    def inserirNoFim(self, novo):
        if self.Vazia():
            self.__cursor = Elemento(novo, self.__inicio, self.__fim)
            self.__inicio.proximo = self.__cursor
            self.__fim.anterior = self.__cursor
            self.__quantidade_atual += 1
        elif self.__quantidade_atual >= self.__tamanho_maximo:
            print('A lista esta cheia')
        else:
            self.__irParaUltimo()
            self.__cursor.proximo = Elemento(novo, self.__cursor, self.__fim)
            self.__fim.anterior = self.__cursor.proximo
            self.__quantidade_atual += 1
        self.__irParaPrimeiro()

    def inserirNaFrente(self, novo):
        if self.Vazia():
            self.__cursor = Elemento(novo, self.__inicio, self.__fim)
            self.__inicio.proximo = self.__cursor
            self.__fim.anterior = self.__cursor
            self.__quantidade_atual += 1
        elif self.Cheia():
            print('A lista esta cheia')
        else:
            self.__irParaPrimeiro()
            self.__cursor.anterior = Elemento(novo, self.__inicio, self.__cursor)
            self.__inicio.proximo = self.__cursor.anterior
            self.__quantidade_atual += 1
        self.__irParaPrimeiro()

    def inserirNaPosicao(self, k, novo):
        if k <= self.__quantidade_atual:
            self.__irParaPrimeiro()
            for i in range(1, k):
                self.__cursor = self.__cursor.proximo
            self.InserirAntesDoAtual(novo)

    def ExcluirAtual(self):
        self.__cursor.anterior.proximo, self.__cursor.proximo.anterior = self.__cursor.proximo, self.__cursor.anterior
        self.__quantidade_atual -= 1
        self.__retrocederKPosicoes(1)

    def ExcluirPrim(self):
        if self.__listanaoVazia():
            self.__irParaPrimeiro()
            self.__inicio.proximo = self.__cursor.proximo
            self.__cursor.proximo = self.__inicio
            self.__quantidade_atual -= 1
            self.__irParaPrimeiro()

    def ExcluirUlt(self):
        if self.__listanaoVazia():
            self.__irParaUltimo()
            self.__fim.anterior = self.__cursor.anterior
            self.__cursor.anterior = self.__fim
            self.__quantidade_atual -= 1
            self.__irParaUltimo()

    def ExcluirElem(self, chave):
        if self.Buscar(chave):
            self.ExcluirAtual()

    def ExcluirDaPos(self, k):
        if k <= self.__quantidade_atual:
            self.__irParaPrimeiro()
            for i in range(1, k):
                self.__cursor = self.__cursor.proximo
            self.ExcluirAtual()
