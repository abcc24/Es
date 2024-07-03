class Pagamento:

    def __init__(self):
        pass

    def setPagamento(self, importo: float):
        if self.__importo == float:
            self.__importo = importo

    def getPagamento(self):
        return self.__importo

    def dettagliPagamento(self):
        print(f"Importo del pagamento: {round(self.__importo, 2)}")
    

class PagamentoContanti(Pagamento):

    def __init__(self):
        super().__init__()
        pass

    def dettagliPagamentoContanti(self):
        print (f"Importo in banconote è di {round(self.__importo,2)}")

    def inPezziDA(self):
        banconote = [500, 200, 100, 50, 20, 10, 5, 2, 1, 0.50, 0.20, 0.10, 0.05, 0.01]

        for x in banconote:
            if x+x = 